RTD-Dir-Reproducible-Example
==================================================

This is a reproducible example for https://github.com/sphinx-contrib/images/pull/31

-------------------

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore
magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

Images in _static (local)
-------------------------

.. thumbnail:: _static/black_234x60.gif
   :group: ex1
   :width: 32%

   1

.. thumbnail:: _static/grey_234x60.gif
   :group: ex2
   :width: 32%

   2

.. thumbnail:: _static/white_234x60.gif
   :group: ex3
   :width: 32%

   3

Remote Images (https)
---------------------

.. thumbnail:: https://www.lipsum.com/images/banners/black_234x60.gif
   :group: ex1
   :width: 32%

   1

.. thumbnail:: https://www.lipsum.com/images/banners/grey_234x60.gif
   :group: ex2
   :width: 32%

   2

.. thumbnail:: https://www.lipsum.com/images/banners/white_234x60.gif
   :group: ex3
   :width: 32%

   3

Vimeo Thumbnails (sphinxcontrib-youtube 1.2.0)
----------------------------------------------

.. vimeo:: 657905289
   :aspect: 4:3
   :width: 100%

.. vimeo:: 382251167
   :aspect: 3:2
   :width: 100%
