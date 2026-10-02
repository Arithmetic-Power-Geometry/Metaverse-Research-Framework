from dataclasses import dataclass, field
from typing import List

@dataclass(frozen=True)
class Timing:
    fps: int = 100
    slot_ms: float = 10.0
    mtp_threshold_ms: float = 20.0
    prediction_window_slots: int = 5

@dataclass
class UserState:
    foreground_queue: List[object] = field(default_factory=list)
    background_queue: List[object] = field(default_factory=list)
    sensor_information_age_ms: float = 0.0
    device_power_w: float = 0.0

@dataclass
class SystemState:
    slot: int = 0
    users: List[UserState] = field(default_factory=list)

class UnresolvedSourceEquation(RuntimeError):
    pass
