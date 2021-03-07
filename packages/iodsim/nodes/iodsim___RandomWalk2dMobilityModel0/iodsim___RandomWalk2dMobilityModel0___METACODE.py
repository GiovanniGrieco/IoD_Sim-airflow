from NIENV import *

class %CLASS%(NodeInstance):
    def __init__(self, params):
        super(%CLASS%, self).__init__(params)

    def update_event(self, input_called=-1):
        d = {
            'name': "ns3::RandomWalk2dMobilityModel",
            'attributes': []
        }

        if self.input(0): d["attributes"].append({"name": "Speed", "value": self.input(0)})
        if self.input(1): d["attributes"].append({"name": "Direction", "value": self.input(1)})
        if self.input(2): d["attributes"].append({"name": "Mode", "value": self.input(2)})
        if self.input(3): d["attributes"].append({"name": "Distance", "value": float(self.input(3))})
        if self.input(4): d["attributes"].append({"name": "Time", "value": float(self.input(4))})
        if self.input(5): d["attributes"].append({"name": "Bounds", "value": self.input(5)})
        if self.input(6): d["attributes"].append({"name": "Velocity", "value": self.input(6)})
        if self.input(7): d["attributes"].append({"name": "Position", "value": self.input(7)})

        self.set_output_val(0, d)

    def get_data(self):
        data = {}
        return data

    def set_data(self, data):
        pass

    def removing(self):
        pass
