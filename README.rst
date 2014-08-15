Installation
=============

Debian packages::

    # apt-get install libyaml-dev libsqlite3-dev build-essential libzmq-dev libfreetype6-dev r-base-core python-dev python-numpy gfortran libopenblas-dev liblapack-dev

Buildout::

    $ python2.7 bootstrap.py
    $ bin/buildout

Use supervisord::

    $ bin/notebookd
    $ bin/notebookctl status

Info::

This install a notebook server which all requireds package needed at the technical college FFHS.



