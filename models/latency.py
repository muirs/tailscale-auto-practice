from typing import List
from dataclasses import dataclass

@dataclass
class Latency:
    preferred: bool
    latencyMs: float