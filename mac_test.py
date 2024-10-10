from macaddress import format_mac
from netaddr import EUI, AddrFormatError
from netaddr.strategy.eui48 import mac_eui48





mac = '6c3aff462c67'
mac2 = '6C-3A-FF-46-2C-67'
mac_obj = EUI(mac2, dialect=mac_lower)
formatted = format_mac(mac_obj, dialect=mac_lower)
pass
