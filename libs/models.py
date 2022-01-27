from dataclasses import dataclass

@dataclass(frozen=True)
class Pod:
    type: str
    has_child: list
    coords: dict
    contains_astronaut: list
    has_life_support: bool
    critical_life_support_active: bool
    has_fire: bool
    fire_suppression_active: bool
    has_other_hazard: bool
    vent_active: bool
    warning_alarm_active: bool

@dataclass(frozen=True)
class Gate:
    gate_position: str
    door_open_request : bool
    door_angle: bool
    door_blocked: bool
    manual_override: bool
    door_locked: bool

@dataclass(frozen=True)
class Airlock:
    extractor_active: bool
    vent_active: bool
    has_fire: bool
    fire_suppression_active: bool
    has_other_hazard: bool
    gate: Gate

@dataclass(frozen=True)
class Astronaut:
    name: str
    location: str
    biometrics: None
    authorisation: None
    
    