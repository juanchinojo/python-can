"""
ipy_profile_pycanlib.py: part of pycanlib, used to load the pycanlib
ipython extensions when the pycanlib ipython profile is used.

Copyright (C) 2010 Dynamic Controls

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

Contact details
---------------

Postal address:
    Dynamic Controls
    17 Print Place
    Addington
    Christchurch 8024
    New Zealand

E-mail: bpowell AT dynamiccontrols DOT com
"""

import IPython.ipapi
import pycanlib.ipython

ip_engine = IPython.ipapi.get()
ip_engine.options.autocall = 2
pycanlib.ipython.doIPythonImports(ip_engine)