# -*- coding: utf-8 -*-
#
# Copyright © 2015 Hasan Yavuz Özderya
#
# This file is part of ecad-3d-model-generator.
#
# ecad-3d-model-generator is free software: you can redistribute it
# and/or modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation, either version 3 of
# the License, or (at your option) any later version.
#
# ecad-3d-model-generator is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with ecad-3d-model-generator.  If not, see
# <http://www.gnu.org/licenses/>.

# Dimensions are from Microchip Packaging Specifications

from e3dmg.generators.qfn import QFNGen

QFN16 = QFNGen(
    D = 3.0,
    E = 3.0,
    A = 0.90,
    A1 = 0.02,
    b = 0.25,
    e = 0.5,
    npx = 4,
    npy = 4,
    epad = (1.7, 1.7)
)