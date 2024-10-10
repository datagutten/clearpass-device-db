from netaddr.strategy.eui48 import mac_eui48


class mac_lower(mac_eui48):
    """A bare (no delimiters) MAC address dialect class."""

    word_size = 48
    num_words = 48 // word_size
    word_sep = ''
    word_fmt = '%.12x'
    word_base = 16