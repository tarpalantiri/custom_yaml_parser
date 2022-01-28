import os
import yaml
from rich.table import Table
from rich.console import Console
from dataclasses import fields
from libs.parser import Custom_Parser

def show_table(dataclass_item):
    console = Console()
    table = Table(show_header=False)
    table.add_column('Name')
    table.add_column('Value')
    for field in fields(dataclass_item):
        name = field.name
        value = str(getattr(dataclass_item, field.name))
        table.add_row(
            name, value
        )
    console.print(table)
    

def main():
    filename = 'facility.yaml'
    # Getting file path
    current_dir = os.getcwd()
    yaml_path = os.path.join(current_dir, filename)
    
    # Parsing YAML File
    yaml_file_stream = open(yaml_path, 'r')
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
    
    while True:
        query = input('Query: [Pods, Gates, Airlocks, Astronauts]: ').lower()
        if query == 'pods':
            query_data = all_pods
        elif query == 'gates':
            query_data = all_gates
        elif query == 'airlocks':
            query_data = all_airlocks
        elif query == 'astronauts':
            query_data = all_astros
        else:
            print('Invalid Input')
            continue
        for item in query_data:
            show_table(item)
        continue
        

if __name__ == '__main__':
    main()