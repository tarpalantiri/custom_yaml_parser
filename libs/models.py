from dataclasses import dataclass, field
from libs.exceptions import InvalidDoorAngleValue


@dataclass(frozen=True, order=True)
class Pod_Coordinates:
    North: list
    South: list
    West:  list
    East:  list

@dataclass
class Pod:
    Pod_index: int
    Type: str
    Has_Child: list
    Coordinates: Pod_Coordinates
    Contains_Astronaut: list
    Has_Life_Support: bool
    Critical_Life_Support_Active: bool
    Has_Fire: bool
    Fire_Suppression_Active: bool
    Has_Other_Hazard: bool
    Vent_Active: bool
    Warning_Alarm_Active: bool

@dataclass
class Gate_Info:
    Door_Open_Request : bool
    Door_Angle: int
    Door_Blocked: bool
    Manual_Override: bool
    Door_Locked: bool

    def __post_init__(self):
        # Validation & convertion of ints to bools
        if self.Door_Angle not in range(0, 136):
            raise InvalidDoorAngleValue(
                angle_value=self.Door_Angle,
                message="Gate Door_Angle must be between 0 and 135"
                )
        self.door_open_request = bool(self.Door_Open_Request)
        self.door_blocked = bool(self.Door_Blocked)
        self.manual_override = bool(self.Manual_Override)
        self.door_locked = bool(self.Door_Locked)

@dataclass
class Gate:
    Gate_id: str
    # Both are initialized to None so we can have the possiblity of
    # having only one gate info
    Int_gate: Gate_Info = None
    Ext_gate: Gate_Info = None

@dataclass
class Airlock:
    Extractor_Active: bool
    Vent_Active: bool
    Has_Fire: bool
    Fire_Suppression_Active: bool
    Has_Other_Hazard: bool
    Int_Gate: Gate_Info = None
    Ext_Gate: Gate_Info = None
    
@dataclass
class Astronaut:
    Name: str
    Location: str
    Biometrics: None
    Authorisation: None
    
    