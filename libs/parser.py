import yaml
from .models import Pod, Pod_Coordinates, Gate_Info, Gate

KNOWN_DOCUMENTS = ['Pods', 'Gates', 'Airlocks', 'Astronauts']

def parse_yaml(yaml_file_path="./facility.yaml"):
    """
    :param yaml_file_path: Path to the yaml file
    :return: List with all the documents
    """
    # Parsing the YAML file
    yaml_file_stream = open(yaml_file_path, 'r')
    all_docs = yaml.load_all(yaml_file_stream, Loader=yaml.FullLoader)
    return [*all_docs]

def make_pod(index, parsed_dict):
    formated_dict = dict()
    # Turn all key strings to lower case, so the dataclass can be
    # given a dict as a parameter
    parsed_dict = {key.lower() : value for key, value in parsed_dict.items()}
    
    # Adding Pod Index
    formated_dict["pod_index"] = int(index)
    
    # Constructing Coordinates
    formated_dict['coords'] = Pod_Coordinates(
        north=parsed_dict["North"],
        east=parsed_dict["East"],
        south=parsed_dict["South"],
        west=parsed_dict["West"]
    )
    
    # Turn 1s and 0s to bools
    for key, value in parsed_dict.items():
        if key not in ['north', 'east', 'south', 'west']:
            # Turn all the 1s and 0s to bools
            if isinstance(value, int):
                value = bool(value)
            formated_dict[key] = value
    return Pod(**formated_dict)

def make_gate(gate_id, parsed_dict):
    formated_dict = dict()
    parsed_dict = { key.lower(): value for key, value in parsed_dict.items() }
    formated_dict['gate_id'] = gate_id
    # Add gate info
    for gate_loc, gate_info in parsed_dict.items():
        # Changing all parameters to lower_case for the inner dict
        gate_info = { key.lower():value for key, value in gate_info.items() }
        
        # Making a Gate_Info obejct
        formated_dict[gate_loc] = Gate_Info(**gate_info)
    return Gate(**formated_dict)
        
    
