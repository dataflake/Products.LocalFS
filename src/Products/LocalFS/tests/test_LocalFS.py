##############################################################################
#
# Copyright (c) 1999 Jonothan Farr and contributors
# All rights reserved. Written by Jonothan Farr <jfarr@speakeasy.org>
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
# 3. The name of the author may not be used to endorse or promote products
#    derived from this software without specific prior written permission
#
# Disclaimer
#
#   THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
#   IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
#   OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
#   IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT,
#   INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
#   NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
#   DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
#   THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#   (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
#   THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# In accordance with the license provided for by the software upon
# which some of the source code has been derived or used, the following
# acknowledgement is hereby provided:
#
#      "This product includes software developed by Digital Creations
#      for use in the Z Object Publishing Environment
#      (http://www.zope.org/)."
#
##############################################################################
# Tests for the LocalFS class

import unittest

from ..LocalFS import _iswin32
from .helpers import LOCALFS_ROOT


class LocalFSTests(unittest.TestCase):

    def _getTargetClass(self):
        from ..LocalFS import LocalFS

        return LocalFS

    def _makeOne(self, *args):
        return self._getTargetClass()(*args)

    def _makeSimple(self):
        klass = self._getTargetClass()
        return klass('localfs', 'LocalFS Title', LOCALFS_ROOT, 'user', 'pw')

    def test_instantiation(self):
        lfs = self._makeSimple()
        self.assertEqual(lfs.getId(), 'localfs')
        self.assertEqual(lfs.title, 'LocalFS Title')
        self.assertEqual(lfs.basepath, LOCALFS_ROOT)

        # Only on Windows
        if _iswin32:
            self.assertEqual(lfs.username, 'user')
            self.assertEqual(lfs._password, 'pw')

    def test_factory(self):
        from OFS.Folder import Folder

        from ..LocalFS import manage_addLocalFS

        folder = Folder('test')

        manage_addLocalFS(folder, 'lfs', 'Local FS', LOCALFS_ROOT)

        self.assertEqual(folder.lfs.getId(), 'lfs')
        self.assertEqual(folder.lfs.title, 'Local FS')
        self.assertEqual(folder.lfs.basepath, LOCALFS_ROOT)

        # Only on Windows
        if _iswin32:
            self.assertEqual(folder.lfs.username, None)
            self.assertEqual(folder.lfs._password, None)
