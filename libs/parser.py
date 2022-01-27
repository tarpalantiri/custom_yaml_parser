import yaml
from .models import Pod, Pod_Coordinates, Gate_Info, Gate, Airlock


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
    
    # Adding Pod Index
    formated_dict["Pod_index"] = int(index)
    
    # Constructing Coordinates
    formated_dict['Coordinates'] = Pod_Coordinates(
        North=parsed_dict["North"],
        East=parsed_dict["East"],
        South=parsed_dict["South"],
        West=parsed_dict["West"]
    )
    
    # Turn 1s and 0s to bools
    for key, value in parsed_dict.items():
        if key not in ['North', 'East', 'South', 'West']:
            # Turn all the 1s and 0s to bools
            if isinstance(value, int):
                value = bool(value)
            formated_dict[key] = value
    return Pod(**formated_dict)

def make_gate(gate_id, parsed_dict):
    formated_dict = dict()
    formated_dict['Gate_id'] = gate_id
    # Add gate info
    for gate_loc, gate_info in parsed_dict.items():
        # Making a Gate_Info obejct
        formated_dict[gate_loc] = Gate_Info(**gate_info)
    return Gate(**formated_dict)

def make_airlock(airlock_id, parsed_dict):
    formated_dict = dict()
    # Extracting interior and exterior gate dicts
    int_gate_dict = parsed_dict.pop('Int_Gate', None)
    ext_gate_dict = parsed_dict.pop('Ext_Gate', None)
    if int_gate_dict is not None and ext_gate_dict is not None:
        formated_dict['Int_Gate'] = Gate_Info(**int_gate_dict)
        formated_dict['Ext_Gate'] = Gate_Info(**ext_gate_dict)
    
    # Merging other parameters
    formated_dict.update(parsed_dict)
    return Airlock(**formated_dict)
    