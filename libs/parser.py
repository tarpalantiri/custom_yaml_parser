from .models import Pod, Pod_Coordinates, Gate_Info, Gate, Airlock, Astronaut

class Custom_Parser:
    @staticmethod
    def make_pod(index, parsed_dict):
        formated_dict = dict()
        # Adding Pod Index
        formated_dict["Id"] = int(index)
        # Constructing Coordinates
        formated_dict['Coordinates'] = Pod_Coordinates(
            North=parsed_dict.pop('North', None),
            East=parsed_dict.pop('East', None),
            South=parsed_dict.pop('South', None),
            West=parsed_dict.pop('West', None)
        )
        formated_dict.update(parsed_dict)
        return Pod(**formated_dict)
    
    @staticmethod
    def make_gate(gate_id, parsed_dict):
        formated_dict = dict()
        formated_dict['Id'] = gate_id
        # Add gate info
        for gate_loc, gate_info in parsed_dict.items():
            # Making a Gate_Info obejct
            formated_dict[gate_loc] = Gate_Info(**gate_info)
        return Gate(**formated_dict)
    
    @staticmethod
    def make_airlock(airlock_id, parsed_dict):
        formated_dict = dict()
        formated_dict['Id'] = airlock_id
        # Extracting interior and exterior gate dicts
        int_gate_dict = parsed_dict.pop('Int_Gate', None)
        ext_gate_dict = parsed_dict.pop('Ext_Gate', None)
        if int_gate_dict is not None and ext_gate_dict is not None:
            formated_dict['Int_Gate'] = Gate_Info(**int_gate_dict)
            formated_dict['Ext_Gate'] = Gate_Info(**ext_gate_dict)
        
        # Merging other parameters
        formated_dict.update(parsed_dict)
        return Airlock(**formated_dict)
    
    @staticmethod
    def make_astronaut(astro_id, parsed_dict):
        formated_dict = {
            'Id' : astro_id,
            'Name': parsed_dict['Name'],
            'Location': parsed_dict['Location'],
            'Biometrics': parsed_dict['Biometrics'],
            'Authorisation': parsed_dict['Authorisation']
        }
        return Astronaut(**formated_dict)