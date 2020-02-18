#! utils/grid/__init__.py
#
# This file is part of utils.
# Copyright (C) 2020  Rainer Weinberger (rainer.weinberger@cfa.harvard.edu)
#
# Utils is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Utils is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with physics.  If not, see <https://www.gnu.org/licenses/>.

import numpy as np

class HealPix:
    """
        HEALPix Tesselation class,
        uses cache to calculate only 'new' tesselsations
    """

    def __init__(self):
        self.cache_z = {}
        self.cache_phi = {}

    def get_healpix(self, N_side):
        if N_side in self.cache_z.keys() and N_side in self.cache_phi.keys():
            return self.cache_z[N_side], self.cache_phi[N_side]
        else:
            z, phi = self.HEALPix(N_side)
            self.cache_z.update({N_side: z})
            self.cache_phi.update({N_side: phi})
            return z, phi

    def healpix(self, N_side, z=None, phi=None):
        ## HEALPix tesslation
        N_pix = 12 * N_side * N_side
        if z == None:
            z = []
        if phi == None:
            phi = []

        ## debug variable
        i_added = 0

        for p in np.arange(0, N_pix):
            ## polar cap:
            p_h = 0.5 * (p + 1.0)
            i = np.int(np.sqrt(p_h - np.sqrt(np.int(p_h)))) + 1
            j = p + 1 - 2 * i * (i - 1)
            if i >= 1 and i < N_side and j >= 1 and j <= 4 * i:
                Phi = np.pi / 2.0 / i * (j - 0.5)
                Z = 1.0 - i * i / 3.0 / N_side / N_side
                z.append(Z)
                phi.append(Phi)
                i_added += 1

                if i * i != 3 * N_side * N_side:  ## mirror at equator, unless cell is at equator
                    z.append(-Z)
                    phi.append(Phi)
                    i_added += 1
                continue
            ## equatorial belt:
            pprime = p - 2 * N_side * (N_side - 1)
            i = np.int(pprime / 4.0 / N_side) + N_side
            j = (pprime % (4 * N_side)) + 1
            if i >= N_side and i <= 2 * N_side and j >= 1 and j <= 4 * N_side:
                s = (i - N_side + 1) % 2
                Z = 4.0 / 3.0 - 2.0 * i / 3.0 / N_side
                Phi = np.pi / 2.0 / N_side * (j - 0.5 * s)
                z.append(Z)
                phi.append(Phi)
                i_added += 1
                if i != 2 * N_side:  ## mirror at equator
                    z.append(-Z)
                    phi.append(Phi)
                    i_added += 1

        if i_added != N_pix:
            print('ERROR: HEALPIX: incorrect number of cells added')
            print(i_added, ' instead of ', N_pix)
            exit(1)

        return z, phi
