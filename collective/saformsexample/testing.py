# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import collective.saformsexample


class CollectiveSaformsexampleLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=collective.saformsexample)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.saformsexample:default')


COLLECTIVE_SAFORMSEXAMPLE_FIXTURE = CollectiveSaformsexampleLayer()


COLLECTIVE_SAFORMSEXAMPLE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_SAFORMSEXAMPLE_FIXTURE,),
    name='CollectiveSaformsexampleLayer:IntegrationTesting'
)


COLLECTIVE_SAFORMSEXAMPLE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_SAFORMSEXAMPLE_FIXTURE,),
    name='CollectiveSaformsexampleLayer:FunctionalTesting'
)


COLLECTIVE_SAFORMSEXAMPLE_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_SAFORMSEXAMPLE_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='CollectiveSaformsexampleLayer:AcceptanceTesting'
)
