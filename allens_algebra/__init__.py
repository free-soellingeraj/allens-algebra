#!/usr/bin/env python

from __future__ import absolute_import
import sys

from pbr.version import VersionInfo

_v = VersionInfo('allens_algebra').semantic_version()
__version__ = _v.release_string()
version_info = _v.version_tuple()

__author__ = "Aaron Soellinger"
__copyright__ = "Copyright 2020-, Aaron Soellinger"
__email__ = "asoellin@gmail.com"
__status__ = "Alpha"
__all__ = ('allens_algebra, __version__')

if sys.hexversion < 0x02050000:
    sys.exit("Python 2.5 or newer is required by tendo module.")
