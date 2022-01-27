from dataclasses import dataclass

@dataclass(frozen=True, order=True)
class Pod_Coordinates:
    north: float
    south: float
    west: float
    east: float
    

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
class Gate:
    gate_position: str
    door_open_request : bool
    door_angle: int
    door_blocked: bool
    manual_override: bool
    door_locked: bool

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
    
    