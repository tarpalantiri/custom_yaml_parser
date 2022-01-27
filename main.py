from libs.parser import parse_yaml

if __name__ == '__main__':
    p = parse_yaml()
    _, gates, *y = p
    print(gates)