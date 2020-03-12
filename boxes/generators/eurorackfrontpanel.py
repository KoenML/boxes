#!/usr/bin/env python3
# Copyright (C) 2013-2017 Florian Festi
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

from boxes import *


class EurorackFrontPanel(Boxes):
    """Closed box with screw on top and mounting holes"""

    ui_group = "Misc"
    x=5.00
    
    def __init__(self):
        Boxes.__init__(self)
        self.addSettingsArgs(edges.FingerJointSettings)
        self.buildArgParser()
        self.argparser.add_argument(
            "--hp", action="store", type=int, default=2,
            help="Width in HP")

    def mountingholes(self):
        
        self.hole(2.54 , 125.5 , d=3.0)
        self.hole(2.54, 3, d=3.0)
        if (self.hp >= 5):
            self.rectangularHole(2.54 +(self.hp - 1.5) * 5.08 , 125.5 , 5.08, 3, 3)
            self.rectangularHole(2.54 +(self.hp - 1.5) * 5.08 , 3, 5.08, 3, 3)
            
    
        
    def render(self):

        t = self.thickness
        h = 128.45
        hp = self.hp
        self.x = (float)(hp * 5.08 * 10) // 10
        

        self.rectangularWall(self.x, h, "eeee", callback=[self.mountingholes])
        ###if not self.outsidemounts:
        #    self.rectangularWall(x, y, "FFFF", callback=[
        #    lambda:self.hole(hd, hd, d=d3)] *4, move="right")
        #else:
        #    self.flangedWall(x, y, edges="FFFF",
        #                     flanges=[0.0, 2*hd, 0., 2*hd], r=hd,
        #                     callback=[
        #            lambda:self.hole(hd, hd, d=d3)] * 4, move='up')
        #self.rectangularWall(x, y, callback=[
        



