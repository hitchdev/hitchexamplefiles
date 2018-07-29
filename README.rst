HitchExampleFiles
=================

A group of example files which can be used for testing.

E.g.

.. code:: python

  import hitchexamplefiles
  from path import Path

  >>> hitchexamplefiles.jpeg_large.copy(Path("/path/to/your/jpegname.jpeg"))
  >>> hitchexamplefiles.jpeg_small.copy(Path("/path/to/your/jpegname.jpeg"))
  >>> hitchexamplefiles.pdf_one_page.copy(Path("/path/to/your/pdf_one_page.pdf"))
  >>> hitchexamplefiles.png_large.copy(Path("/path/to/your/png_large.png"))
