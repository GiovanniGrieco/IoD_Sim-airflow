from NIENV import *

class %CLASS%(NodeInstance):
    def __init__(self, params):
        super(%CLASS%, self).__init__(params)

    def update_event(self, input_called=-1):
        d = {
            'name': "ns3::AcousticModemEnergyModel",
            'attributes': []
        }

        if self.input(0): d["attributes"].append({"name": "SleepPowerW", "value": float(self.input(0))})
        if self.input(1): d["attributes"].append({"name": "IdlePowerW", "value": float(self.input(1))})
        if self.input(2): d["attributes"].append({"name": "RxPowerW", "value": float(self.input(2))})
        if self.input(3): d["attributes"].append({"name": "TxPowerW", "value": float(self.input(3))})

        self.set_output_val(0, d)

    def get_data(self):
        data = {}
        return data

    def set_data(self, data):
        pass

    def removing(self):
        pass
