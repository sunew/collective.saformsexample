# -*- coding: utf-8 -*-
""""""

from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class ICollectiveSaformsexampleLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IDemoDataManager(Interface):
    """ The data manager utility interface.
    """
    # todo
