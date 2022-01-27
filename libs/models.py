from dataclasses import dataclass, field
from libs.exceptions import InvalidDoorAngleValue


@dataclass(frozen=True, order=True)
class Pod_Coordinates:
    north: list
    south: list
    west:  list
    east:  list

@dataclass
class Pod:
    pod_index: int
    type: str
    has_child: list
    coords: Pod_Coordinates
    contains_astronaut: list
    has_life_support: bool
    critical_life_support_active: bool
    has_fire: bool
    fire_suppression_active: bool
    has_other_hazard: bool
    vent_active: bool
    warning_alarm_active: bool

@dataclass
class Gate_Info:
    door_open_request : bool
    door_angle: int
    door_blocked: bool
    manual_override: bool
    door_locked: bool

    def __post_init__(self):
        # Validation & convertion of ints to bools
        if self.door_angle not in range(0, 136):
            raise InvalidDoorAngleValue(
                angle_value=self.door_angle,
                message="Gate Door_Angle must be between 0 and 135"
                )
        self.door_open_request = bool(self.door_open_request)
        self.door_blocked = bool(self.door_blocked)
        self.manual_override = bool(self.manual_override)
        self.door_locked = bool(self.door_locked)

@dataclass
class Gate:
    gate_id: str
    int_gate: Gate_Info = None
    ext_gate: Gate_Info = None

@dataclass
class Airlock:
    extractor_active: bool
    vent_active: bool
    has_fire: bool
    fire_suppression_active: bool
    has_other_hazard: bool
    gate: Gate

@dataclass
class Astronaut:
    name: str
    location: str
    biometrics: None
    authorisation: None
    
    