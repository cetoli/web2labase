from sqlobject import *

from turbogears.database import PackageHub

hub = PackageHub("mepeer")
__connection__ = hub

# class YourDataClass(SQLObject):
#     pass

