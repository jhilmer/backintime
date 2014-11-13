#    Copyright (C) 2012-2014 Germar Reitze
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License along
#    with this program; if not, write to the Free Software Foundation, Inc.,
#    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import os

import configfile

class ProgressFile(configfile.ConfigFile):

    RSYNC           = 50

    def __init__(self, cfg, filename = None):
        super(ProgressFile, self).__init__()
        self.config = cfg
        self.filename = filename
        if self.filename is None:
            self.filename = self.config.get_take_snapshot_progress_file()

    def save(self):
        return super(ProgressFile, self).save(self.filename)

    def load(self):
        return super(ProgressFile, self).load(self.filename)

    def isFileReadable(self):
        return os.access(self.filename, os.R_OK)