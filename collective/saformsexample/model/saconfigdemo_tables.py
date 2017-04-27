import sqlalchemy as sa
from sqlalchemy.sql import functions

from zope import schema as zs
from zope.interface import implements
from zope.interface import Interface

from collective.saformsexample import _
from .base import Base, TABLE_NAMESPACE_DEMO


class IDemoData(Interface):
    """
    """
    demo1 = zs.TextLine(title=_(u"Demo 1"),
                        required=True)
    demo2 = zs.TextLine(title=_(u"Demo 2"),
                        required=True)


class DemoData(Base):
    """"""
    implements(IDemoData)

    __tablename__ = TABLE_NAMESPACE_DEMO + "demodata"

    id = sa.Column("id", sa.Integer, primary_key=True)
    demo1 = sa.Column("demo1", sa.String(255))
    demo2 = sa.Column("damo2", sa.String(255))
    created = sa.Column(sa.DateTime, default=functions.now())
    updated = sa.Column(sa.DateTime, onupdate=functions.current_timestamp())
