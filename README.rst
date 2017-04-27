.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide_addons.html
   This text does not appear on pypi or github. It is a comment.

==============================================================================
collective.saformsexample
==============================================================================

A demo of using sqlalchemy objects as a basis for z3c.form based forms.

Database connections: z3c.saconfig

A sqlalchemy object is defined to implement a zope interface. The forms are generated from this interface.


Examples
--------

Setup:

1. First create the database and the database user with the sql script in the packages mysql_scripts/

2. Install the module in Plone. This creates the tabels defined in model/ in the database.

3. Go to demodata-view/ in your browser to begin adding data.

