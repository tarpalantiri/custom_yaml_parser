import os
import yaml
from libs.parser import Custom_Parser

FILE_NAME = 'facility.yaml'

def main(filename):
    # Getting file path
    current_dir = os.getcwd()
    yaml_path = os.path.join(current_dir, FILE_NAME)
    
    # Parsing YAML File
    yaml_file_stream = open('./facility.yaml', 'r')
    all_docs = yaml.load_all(yaml_file_stream, Loader=yaml.FullLoader)
    
    # Seperating into individual dicts
    pods_dict, gates_dict, airlocks_dict, astros_dict = all_docs
    
    # Closing the File Stream
    yaml_file_stream.close()
    
    # Generators of all objects.
    all_pods = (
        Custom_Parser.make_pod(index, data) for index, data in pods_dict.items()
    )
    all_gates = (
        Custom_Parser.make_gate(index, data) for index, data in
        gates_dict.items()
    )
    all_airlocks = (
        Custom_Parser.make_airlock(index, data) for index, data in
        airlocks_dict.items()
    )
    all_astros = (
        Custom_Parser.make_astronaut(index, data) for index, data in
        astros_dict.items()
    )

if __name__ == '__main__':
    main(FILE_NAME)