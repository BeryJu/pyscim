# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.default_api import DefaultApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from pyscim.api.default_api import DefaultApi
from pyscim.api.discovery_api import DiscoveryApi
from pyscim.api.fido2_devices_api import Fido2DevicesApi
from pyscim.api.fido_devices_api import FidoDevicesApi
from pyscim.api.global_search_api import GlobalSearchApi
from pyscim.api.group_api import GroupApi
from pyscim.api.user_api import UserApi
