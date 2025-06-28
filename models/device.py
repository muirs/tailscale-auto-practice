from typing import List
from dataclasses import dataclass

from models.client_connectivity import ClientConnectivity
from models.posture_identity import PostureIdentity

@dataclass
class Device:
    addresses: List[List[str]]
    id: str
    nodeId: str
    user: str
    name: str
    hostname: str
    clientVersion: str
    updateAvailable: bool
    os: str
    created: str
    lastSeen: str
    keyExpiryDisabled: bool
    expires: str
    authorized: bool
    isExternal: bool
    multipleConnections: bool
    machineKey: str
    nodeKey: str
    blocksIncomingConnections: bool
    enabledRoutes: List[str]
    advertisedRoutes: List[str]
    clientConnectivity: ClientConnectivity
    tags: List[str]
    tailnetLockError: str
    tailnetLockKey: str
    postureIdentity: PostureIdentity