# -*- coding: utf-8 -*-
import logging
from sqlalchemy.orm.exc import NoResultFound

from zExceptions import NotFound
from zope.interface import implements
from zope.component.hooks import getSite
# from zope.globalrequest import getRequest

from Products.CMFPlone.utils import log

from collective.saformsexample.interfaces import IDemoDataManager
from collective.saformsexample.model.saconfigdemo_tables import DemoData
from collective.saformsexample.model.base import Session


class DemoDataManagerUtility(object):
    """
    """

    implements(IDemoDataManager)

    def __init__(self):
        from ipdb import set_trace; set_trace()
        self._db_session = None

    @property
    def portal(self):
        return getSite()

    @property
    def db_session(self):
        from ipdb import set_trace; set_trace()
        if not self._db_session:
            self._db_session = Session()
        return self._db_session

    def create_demo_obj(self, data):
        return DemoData(**data)

    def persist_demo_obj(self, obj):
        # add to session - or whatever storage we use.
        session = self.db_session
        session.add(obj)

    def delete_demo_obj(self, obj):
        session = self.db_session
        session.delete(obj)

    def get_demo_obj(self, pk):
        session = self.db_session
        try:
            return session.query(DemoData).filter_by(id=pk).one()
        except NoResultFound:
            raise NotFound

    def get_data(self, batch_size=1000, page=1):
        results = (
            self.db_session.query(DemoData)
            .all()
        )

        return results
