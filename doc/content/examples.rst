===============
Output Examples
===============

Figures
*******
The output below was generated from figures included within this document.

.. _fig-list:

List (Default)
~~~~~~~~~~~~~~
.. rst-example::

   .. list-items:: figures

.. _fig-table:

Table
~~~~~
.. rst-example::

   .. list-items:: figures
      :table:

.. _fig-custom-table:

Custom Table
~~~~~~~~~~~~

.. rst-example::

   .. list-items:: figures
      :table: id, caption


Tables
******
The output below was generated from tables included within this document.

.. _table-list:

List (Default)
~~~~~~~~~~~~~~
.. rst-example::

   .. list-items:: tables

.. _table-table:

Table
~~~~~
.. rst-example::

   .. list-items:: tables
      :table:

.. _table-custom-table:

Custom Table
~~~~~~~~~~~~
.. rst-example::

   .. list-items:: tables
      :table: id, caption


Versions
********
The following examples demonstrate listing Sphinx version directives, table/list output, version filtering, and custom columns.


.. _version-list:

List (Default)
~~~~~~~~~~~~~~
.. rst-example::

   .. list-items:: versionadded
      :list:

   .. list-items:: versionchanged
      :list:

   .. list-items:: deprecated
      :list:

   .. list-items:: versionremoved
      :list:


.. _version-table:

Table
~~~~~
.. rst-example::

   .. list-items:: versionadded
      :table:


.. _version-filtered-table:

Filtered Table
~~~~~~~~~~~~~~
.. rst-example::

   .. list-items:: versionadded
      :table:
      :version: 0.0.2


.. _version-custom-table:

Custom Table
~~~~~~~~~~~~
.. rst-example::

   .. list-items:: versionchanged
      :table: version, text