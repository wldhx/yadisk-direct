Yandex.Disk direct links extractor
==================================

Get real direct links usable with tools like ``curl`` or ``wget`` for
files stored in `Yandex.Disk <https://disk.yandex.ru>`__.

Usage
-----

Install with:

.. code:: sh

    pip3 install wldhx.yadisk-direct

Get a real direct link:

.. code:: sh

    yadisk-direct https://yadi.sk/i/LKkWupFjr5WzR

Download a file with a one-liner:

.. code:: sh

    curl -L $(yadisk-direct https://yadi.sk/i/LKkWupFjr5WzR) -o my_local_filename

Disclaimer
----------

While this code depends on an open Yandex's
`API <https://tech.yandex.com/disk/api/reference/public-docpage/#download>`__,
I heartily recommend you to not use it in anything resembling production
environments.
