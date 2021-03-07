from NIENV import *

class %CLASS%(NodeInstance):
    def __init__(self, params):
        super(%CLASS%, self).__init__(params)

    def update_event(self, input_called=-1):
        d = {
            'name': "ns3::BurstErrorModel",
            'attributes': []
        }

        if self.input(0): d["attributes"].append({"name": "BurstSize", "value": self.input(0)})
        if self.input(1): d["attributes"].append({"name": "BurstStart", "value": self.input(1)})
        if self.input(2): d["attributes"].append({"name": "ErrorRate", "value": float(self.input(2))})
        if self.input(3): d["attributes"].append({"name": "IsEnabled", "value": bool(self.input(3))})

        self.set_output_val(0, d)

    def get_data(self):
        data = {}
        return data

    def set_data(self, data):
        pass

    def removing(self):
        pass
