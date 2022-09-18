Development
===========

.. highlight:: bash

Getting the source code
-----------------------
The source code is maintained in the Git repository.::

  $ git clone https://github.com/MineralWare/Products.LocalFS.git

Setting up a development sandbox and testing
--------------------------------------------
Once you've obtained a source checkout, you can follow these
instructions to perform various development tasks.
All development requires that you run the buildout from the 
package root directory::

  $ python2.7 bootstrap.py
  $ bin/buildout

Once you have a buildout, the tests can be run as follows::

  $ bin/test

Building the documentation
--------------------------
The Sphinx documentation is built by doing the following from the
directory containing setup.py::

  $ cd docs
  $ make html

The finished HTML files are under `docs/_build/html`.
