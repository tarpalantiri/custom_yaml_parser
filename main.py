from pprint import pprint
from libs.parser import parse_yaml, make_pod

# Main File is for testing purposes only
# Later we'll add the final Interface
if __name__ == '__main__':
    p = parse_yaml("./facility.yaml")
    pods, gates, airclocks, astronauts = p
    
    for index, pod_dict in pods.items():
        pod = make_pod(index, pod_dict)
        pprint(pod)
