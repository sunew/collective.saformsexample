# -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base

from zope import component

from z3c.saconfig.scopedsession import named_scoped_session
from z3c.saconfig.interfaces import IEngineFactory

# Each module should be self-contained, and has responsibility
# for the storage and handling of own data.
# To make it possible for modules to share databases,
# we use a table namespace for each module.
TABLE_NAMESPACE_DEMO = 'demo_'

Base = declarative_base()

# Define the Session factory here, for importing on other modules,
# where a session will be created from this factory.
Session = named_scoped_session("saconfigdemo_session")
# todo: what is the life time of session objects, in for instance a utility or a browserview?


def setup_db():
    factory = component.getUtility(IEngineFactory, name="saconfigdemo_engine")
    engine = factory()
    Base.metadata.create_all(engine)
