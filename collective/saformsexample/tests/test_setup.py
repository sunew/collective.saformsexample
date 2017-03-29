# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from collective.saformsexample.testing import COLLECTIVE_SAFORMSEXAMPLE_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that collective.saformsexample is properly installed."""

    layer = COLLECTIVE_SAFORMSEXAMPLE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.saformsexample is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'collective.saformsexample'))

    def test_browserlayer(self):
        """Test that ICollectiveSaformsexampleLayer is registered."""
        from collective.saformsexample.interfaces import (
            ICollectiveSaformsexampleLayer)
        from plone.browserlayer import utils
        self.assertIn(ICollectiveSaformsexampleLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_SAFORMSEXAMPLE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['collective.saformsexample'])

    def test_product_uninstalled(self):
        """Test if collective.saformsexample is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'collective.saformsexample'))
