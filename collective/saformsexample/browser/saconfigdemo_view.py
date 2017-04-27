# -*- coding: utf-8 -*-
from zope import schema as zs
from zope.component import getUtility
from zExceptions import NotFound
from z3c.form import field
from z3c.form import form
from z3c.form.interfaces import HIDDEN_MODE
from Products.Five.browser import BrowserView
from plone.z3cform.layout import FormWrapper
from Products.statusmessages.interfaces import IStatusMessage
from Products.CMFCore.utils import getToolByName
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from sqlalchemy.orm.exc import NoResultFound

from collective.saformsexample import _
from collective.saformsexample.model.saconfigdemo_tables import IDemoData
from collective.saformsexample.model.saconfigdemo_tables import DemoData
from collective.saformsexample.interfaces import IDemoDataManager
from collective.saformsexample.model.base import Session


class ViewDemoData(BrowserView):
    """
    """
    template = ViewPageTemplateFile('templates/view-demodata.pt')

    def __init__(self, context, request):
        super(ViewDemoData, self).__init__(context, request)
        self._db_session = None

    @property
    def db_session(self):
        if not self._db_session:
            self._db_session = Session()
        return self._db_session

    def __call__(self, *args, **kwargs):
        return self.template()

    @property
    def portal(self):
        return getToolByName(self.context, 'portal_url').getPortalObject()

    @property
    def portal_url(self):
        return getToolByName(self.context, 'portal_url')()

    def get_data(self):
        # TODO: the paging is not yet used in the template.
        limit = int(self.request.get('limit', 0)) or 1000
        _page_number = int(self.request.get('page', 1))

        results = (
            self.db_session.query(DemoData)
            .all()
        )
        return results


# ##########  Add  ##############

class AddDemoDataForm(form.AddForm):

    # todo: specify template (overriding plone borders)

    label = _("Add demo data")
    description = _("Description.")
    ignoreContext = True
    ignoreRequest = True
    fields = field.Fields(IDemoData)

    def __init__(self, context, request):
        super(AddDemoDataForm, self).__init__(context, request)
        self._db_session = None

    @property
    def db_session(self):
        if not self._db_session:
            self._db_session = Session()
        return self._db_session

    def create(self, data):
        """
        :param data:
        :return:
        """
        return DemoData(**data)

    def add(self, obj):
        """
        :param obj:
        :return:
        """
        self.db_session.add(obj)

        messages = IStatusMessage(self.request)
        messages.addStatusMessage(
            _(u"Demo data created. Record saved successfully."), type="info")

    def nextURL(self):
        return getToolByName(self.context, 'portal_url')() + "/demodata-view"


class AddDemoDataFormView(FormWrapper):

    # index = ViewPageTemplateFile('templates/z3c.form/form-wrapper.pt')
    form = AddDemoDataForm

    @property
    def back_link(self):
        # todo: correct?
        return getToolByName(self.context,
                             'portal_url')() + '/demodata-view'


# ####  Edit  ##########

class DemoDataEditForm(form.EditForm):

    label = _("Edit Demo data")
    description = None
    fields = field.Fields(IDemoData)

    def __init__(self, context, request):
        super(AddDemoDataForm, self).__init__(context, request)
        self._db_session = None

    @property
    def db_session(self):
        if not self._db_session:
            self._db_session = Session()
        return self._db_session

    def getContent(self):
        """
        :return:
        """
        if self.pk is None:
            raise ValueError("id as PK query string is required")

        try:
            content = self.db_session.query(DemoData).filter_by(id=self.pk).one()
        except NoResultFound:
            raise NotFound
        return content

    @property
    def fields(self):
        """
        :return:
        """
        _fields = field.Fields(IDemoData).copy()
        _fields += field.Fields(self.pk_field())
        return _fields

    @property
    def pk(self):
        if self.request.has_key('id'):
            return int(self.request['id'].replace('.', ''))
        elif self.request.has_key('form.widgets.id'):
            return int(self.request['form.widgets.id'].replace('.', ''))

    def pk_field(self):
        """
        :return:
        """
        row_id_field = field.Field(
            zs.Int(__name__='id', required=False, title=u'ID'))

        return row_id_field

    def updateWidgets(self):
        """
        :return:
        """
        result = super(DemoDataEditForm, self).updateWidgets()
        self.widgets["id"].mode = HIDDEN_MODE
        return result

    def redirect(self, url=None):
        """
        :param url:
        :return:
        """
        url = url or getToolByName(
            self.context, 'portal_url')() + "/demodata-view"
        self.request.response.redirect(url)


class DemoDataEditFormView(FormWrapper):

    form = DemoDataEditForm

    @property
    def back_link(self):
        # todo: correct?
        return getToolByName(self.context,
                             'portal_url')() + '/demodata-view'
