import time


class GroundStationObject(object):
    def __init__(self):
        self.create_timestamp = time.gmtime()
        self.payload = ""
