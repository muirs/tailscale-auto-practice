from typing import List, Dict
from dataclasses import dataclass

from models.client_supports import ClientSupports
from models.latency import Latency

@dataclass
class ClientConnectivity:
    endpoints: List[str]
    latency: Dict[str, Latency]
    mappingVariesByDestIP: bool
    clientSupports: ClientSupports