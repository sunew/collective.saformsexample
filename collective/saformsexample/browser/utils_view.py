# -*- coding: utf-8 -*-
from App.config import getConfiguration
from Products.Five.browser import BrowserView


class UtilsView(BrowserView):

    def plone_debug_mode(self):
        zconfig = getConfiguration()
        return zconfig.debug_mode
