#! utils/movie.py
#
# This file is part of utils.
# Copyright (C) 2020  Rainer Weinberger (rainer.weinberger@cfa.harvard.edu)
#
# Physics is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Physics is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with physics.  If not, see <https://www.gnu.org/licenses/>.

from subprocess import call
import os


def make_movie(figures: str = './fig_%03d.png',
               filename: str = './movie.mp4',
               r: int = 50,
               pix_fmt: str = 'yuv420p'):
    """
        ffmpeg movie generation wrapper;
        note that it forces removing filename!
    """
    call(['rm', '-rf', filename])

    # todo: refactor
    filedir = os.path.dirname(filename)
    if not os.path.exists(filedir):
        os.makedirs(filedir)

    return call(['ffmpeg', '-r', str(r), '-i', figures, '-pix_fmt', pix_fmt, '-vf', '"pad=ceil(iw/2)*2:ceil(ih/2)*2"',
                 filename])