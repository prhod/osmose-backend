#!/usr/bin/env python
#-*- coding: utf-8 -*-

###########################################################################
##                                                                       ##
## Copyrights Frédéric Rodrigo 2016                                      ##
##                                                                       ##
## This program is free software: you can redistribute it and/or modify  ##
## it under the terms of the GNU General Public License as published by  ##
## the Free Software Foundation, either version 3 of the License, or     ##
## (at your option) any later version.                                   ##
##                                                                       ##
## This program is distributed in the hope that it will be useful,       ##
## but WITHOUT ANY WARRANTY; without even the implied warranty of        ##
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         ##
## GNU General Public License for more details.                          ##
##                                                                       ##
## You should have received a copy of the GNU General Public License     ##
## along with this program.  If not, see <http://www.gnu.org/licenses/>. ##
##                                                                       ##
###########################################################################

from Analyser_Osmosis import Analyser_Osmosis


sql10 = """
SELECT id, ST_AsText(geom)
FROM nodes
where tags->'highway' = 'bus_stop' and tags->'public_transport' = 'stop_position'
"""

class Analyser_Osmosis_Public_Transport_Stop_Position(Analyser_Osmosis):

    def __init__(self, config, logger = None):
        Analyser_Osmosis.__init__(self, config, logger)
        self.classs[1] = {"item": "1260", "level": 3, "tag": ["public_transport"], "desc": T_(u"This stop is not properly categorized") }
        self.callback10 = lambda res: {"class":1, "data":[self.id, self.positionAsText]}

    def analyser_osmosis_common(self):
        self.run(sql10, self.callback10)
