from NIENV import *

class %CLASS%(NodeInstance):
    def __init__(self, params):
        super(%CLASS%, self).__init__(params)

    def update_event(self, input_called=-1):
        d = {
            'name': "ns3::RvBatteryModel",
            'attributes': []
        }

        if self.input(0): d["attributes"].append({"name": "RvBatteryModelNumOfTerms", "value": self.input(0)})
        if self.input(1): d["attributes"].append({"name": "RvBatteryModelBetaValue", "value": float(self.input(1))})
        if self.input(2): d["attributes"].append({"name": "RvBatteryModelAlphaValue", "value": float(self.input(2))})
        if self.input(3): d["attributes"].append({"name": "RvBatteryModelCutoffVoltage", "value": float(self.input(3))})
        if self.input(4): d["attributes"].append({"name": "RvBatteryModelOpenCircuitVoltage", "value": float(self.input(4))})
        if self.input(5): d["attributes"].append({"name": "RvBatteryModelLowBatteryThreshold", "value": float(self.input(5))})
        if self.input(6): d["attributes"].append({"name": "RvBatteryModelPeriodicEnergyUpdateInterval", "value": float(self.input(6))})

        self.set_output_val(0, d)

    def get_data(self):
        data = {}
        return data

    def set_data(self, data):
        pass

    def removing(self):
        pass
