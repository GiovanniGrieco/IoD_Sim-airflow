from NIENV import *

class %CLASS%(NodeInstance):
    def __init__(self, params):
        super(%CLASS%, self).__init__(params)

    def update_event(self, input_called=-1):
        d = {
            'name': "ns3::ItuR1411NlosOverRooftopPropagationLossModel",
            'attributes': []
        }

        if self.input(0): d["attributes"].append({"name": "BuildingSeparation", "value": float(self.input(0))})
        if self.input(1): d["attributes"].append({"name": "BuildingsExtend", "value": float(self.input(1))})
        if self.input(2): d["attributes"].append({"name": "StreetsWidth", "value": float(self.input(2))})
        if self.input(3): d["attributes"].append({"name": "StreetsOrientation", "value": float(self.input(3))})
        if self.input(4): d["attributes"].append({"name": "RooftopLevel", "value": float(self.input(4))})
        if self.input(5): d["attributes"].append({"name": "CitySize", "value": self.input(5)})
        if self.input(6): d["attributes"].append({"name": "Environment", "value": self.input(6)})
        if self.input(7): d["attributes"].append({"name": "Frequency", "value": float(self.input(7))})

        self.set_output_val(0, d)

    def get_data(self):
        data = {}
        return data

    def set_data(self, data):
        pass

    def removing(self):
        pass
