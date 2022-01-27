class InvalidDoorAngleValue(Exception):
    def __init__(self, angle_value, message):
        self.angle = angle_value
        super().__init__(message)

if __name__ == "__main__":
    pass
