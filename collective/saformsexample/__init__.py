# -*- coding: utf-8 -*-
"""Init"""

import pkg_resources
from zope.i18nmessageid import MessageFactory

_ = MessageFactory('collective.saformsexample')

package_metadata = pkg_resources.get_distribution('danbio.api')
version = package_metadata.version

def initialize(context):
    """Initializer called when used as a Zope 2 product."""
