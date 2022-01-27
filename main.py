from pprint import pprint
from libs.parser import parse_yaml, make_pod, make_gate, make_airlock

# Main File is for testing purposes only
# Later we'll add the final Interface
if __name__ == '__main__':
    p = parse_yaml("./facility.yaml")
    pods, gates, airlocks, astronauts = p
    
    for airlock_id, data in airlocks.items():
        print(airlock_id)
        print(make_airlock(airlock_id, data))
