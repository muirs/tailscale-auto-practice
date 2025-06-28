from typing import List, Dict
from dataclasses import dataclass

@dataclass
class ClientSupports:
    hairPinning: bool
    ipv6: bool
    pcp: bool
    pmp: bool
    udp: bool
    upnp: bool