from dataclasses import dataclass
from libs.exceptions import InvalidDoorAngleValue

YES = '🟢'
NO = '🔴'

@dataclass(frozen=True, order=True)
class Pod_Coordinates:
    North: list
    South: list
    West:  list
    East:  list
    
    def __str__(self):
        return f"""North: {self.North}
South: {self.South}
West:  {self.West}
East:  {self.East}"""

@dataclass(order=True, repr=True)
class Pod:
    Id:                           str
    Type:                         str
    Has_Child:                    list
    Coordinates:                  Pod_Coordinates
    Contains_Astronaut:           list
    Has_Life_Support:             bool
    Critical_Life_Support_Active: bool
    Has_Fire:                     bool
    Fire_Suppression_Active:      bool
    Has_Other_Hazard:             bool
    Vent_Active:                  bool
    Warning_Alarm_Active:         bool
    
    def __post_init__(self):
        # Validation
        self.Has_Life_Support = bool(self.Has_Life_Support)
        self.Critical_Life_Support_Active = bool(self.Critical_Life_Support_Active)
        self.Has_Fire = bool(self.Has_Fire)
        self.Fire_Suppression_Active = bool(self.Fire_Suppression_Active)
        self.Has_Other_Hazard = bool(self.Has_Other_Hazard)
        self.Vent_Active = bool(self.Vent_Active)
        self.Warning_Alarm_Active = bool(self.Warning_Alarm_Active)
        self.sort_index = self.Id

@dataclass(order=True)
class Gate_Info:
    Door_Open_Request : bool
    Door_Angle:         int
    Door_Blocked:       bool
    Manual_Override:    bool
    Door_Locked:        bool

    def __post_init__(self):
        # Validation
        if self.Door_Angle not in range(0, 136):
            raise InvalidDoorAngleValue(
                angle_value=self.Door_Angle,
                message="Gate Door_Angle must be between 0 and 135"
                )
        self.Door_Open_Request = bool(self.Door_Open_Request)
        self.Door_Blocked = bool(self.Door_Blocked)
        self.Manual_Override = bool(self.Manual_Override)
        self.Door_Locked = bool(self.Door_Locked)
    
    def __str__(self):
        return f"""Door Open Request: {YES if self.Door_Open_Request else NO}
Door Blocked:    {YES if self.Door_Blocked else NO}
Door Locked:     {YES if self.Door_Blocked else NO}
Manual Override: {YES if self.Manual_Override else NO}
Door Angle:      {self.Door_Angle}°"""

@dataclass(order=True)
class Gate:
    Id:  str
    # Both are initialized to None so we can have the possiblity of
    # having only one gate info
    Int_Gate: Gate_Info = None
    Ext_Gate: Gate_Info = None
    
    def __post_init__(self):
        self.sort_index = self.Id

@dataclass(order=True)
class Airlock:
    Id:                      str
    Extractor_Active:        bool
    Vent_Active:             bool
    Has_Fire:                bool
    Fire_Suppression_Active: bool
    Has_Other_Hazard:        bool
    Int_Gate:                Gate_Info = None
    Ext_Gate:                Gate_Info = None
    
    def __post_init__(self):
        # Validation
        self.Extractor_Active = bool(self.Extractor_Active)
        self.Vent_Active = bool(self.Vent_Active)
        self.Fire_Suppression_Active = bool(self.Fire_Suppression_Active)
        self.Has_Other_Hazard = bool(self.Has_Other_Hazard)
        self.sort_index = self.Id
    
@dataclass(order=True)
class Astronaut:
    Id:            str
    Name:          str
    Location:      str
    Biometrics:    list
    Authorisation: list
    
    def __post_init__(self):
        self.sort_index = self.Id
    
    