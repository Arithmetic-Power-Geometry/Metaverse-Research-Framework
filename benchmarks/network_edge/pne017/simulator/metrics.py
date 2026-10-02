from dataclasses import dataclass

@dataclass
class MetricRecord:
    slot: int
    user_id: int
    latency_ms: float | None = None
    mtp_violation: bool | None = None
    sensor_information_age_ms: float | None = None
    device_power_w: float | None = None

def mtp_violation(latency_ms: float, threshold_ms: float = 20.0) -> bool:
    return latency_ms > threshold_ms
