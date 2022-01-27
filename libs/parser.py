import yaml
from .models import Pod, Pod_Coordinates

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
    sanitized = dict()
    # Turn all key strings to lower case, so the dataclass can be
    # given a dict as a parameter
    parsed_dict = {key.lower() : value for key, value in parsed_dict}
    
    # Adding Pod Index
    sanitized["pod_index"] = int(index)
    
    # Constructing Coordinates
    sanitized['coords'] = Pod_Coordinates(
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
            sanitized[key] = value
    return Pod(**sanitized)

    
    
    
