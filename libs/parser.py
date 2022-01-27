import yaml

KNOWN_DOCUMENTS = ['Pods', 'Gates', 'Airlocks', 'Astronauts']

def parse_yaml(yaml_file_path="./facility.yaml"):
    """
    :param yaml_file_path: Path to the yaml file
    :return: List with all the documents
    """
    yaml_file_stream = open(yaml_file_path, 'r')
    all_docs = yaml.load_all(yaml_file_stream, Loader=yaml.FullLoader)
    return [*all_docs]