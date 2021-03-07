from NIENV import *

class %CLASS%(NodeInstance):
    def __init__(self, params):
        super(%CLASS%, self).__init__(params)

    def update_event(self, input_called=-1):
        d = {
            'name': "ns3::WaypointMobilityModel",
            'attributes': []
        }

        if self.input(0): d["attributes"].append({"name": "InitialPositionIsWaypoint", "value": bool(self.input(0))})
        if self.input(1): d["attributes"].append({"name": "LazyNotify", "value": bool(self.input(1))})
        if self.input(2): d["attributes"].append({"name": "WaypointsLeft", "value": self.input(2)})
        if self.input(3): d["attributes"].append({"name": "NextWaypoint", "value": self.input(3)})
        if self.input(4): d["attributes"].append({"name": "Velocity", "value": self.input(4)})
        if self.input(5): d["attributes"].append({"name": "Position", "value": self.input(5)})

        self.set_output_val(0, d)

    def get_data(self):
        data = {}
        return data

    def set_data(self, data):
        pass

    def removing(self):
        pass
