from NIENV import *

class %CLASS%(NodeInstance):
    def __init__(self, params):
        super(%CLASS%, self).__init__(params)

    def update_event(self, input_called=-1):
        d = {
            'name': "ns3::LteEnbMac",
            'attributes': []
        }

        if self.input(0): d["attributes"].append({"name": "ComponentCarrierId", "value": int(self.input(0))})
        if self.input(1): d["attributes"].append({"name": "ConnEstFailCount", "value": int(self.input(1))})
        if self.input(2): d["attributes"].append({"name": "RaResponseWindowSize", "value": int(self.input(2))})
        if self.input(3): d["attributes"].append({"name": "PreambleTransMax", "value": int(self.input(3))})
        if self.input(4): d["attributes"].append({"name": "NumberOfRaPreambles", "value": int(self.input(4))})

        self.set_output_val(0, d)

    def get_data(self):
        data = {}
        return data

    def set_data(self, data):
        pass

    def removing(self):
        pass
