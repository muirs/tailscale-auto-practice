from typing import List
from dataclasses import dataclass

from models.device import Device

@dataclass
class Devices:
    devices: List[Device]