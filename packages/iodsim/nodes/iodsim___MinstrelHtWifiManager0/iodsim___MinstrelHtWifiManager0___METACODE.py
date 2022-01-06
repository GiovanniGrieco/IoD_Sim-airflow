from NIENV import *

class %CLASS%(NodeInstance):
    def __init__(self, params):
        super(%CLASS%, self).__init__(params)

    def update_event(self, input_called=-1):
        d = {
            'name': "ns3::MinstrelHtWifiManager",
            'attributes': []
        }

        if self.input(0): d["attributes"].append({"name": "PrintStats", "value": bool(self.input(0))})
        if self.input(1): d["attributes"].append({"name": "UseLatestAmendmentOnly", "value": bool(self.input(1))})
        if self.input(2): d["attributes"].append({"name": "PacketLength", "value": int(self.input(2))})
        if self.input(3): d["attributes"].append({"name": "SampleColumn", "value": int(self.input(3))})
        if self.input(4): d["attributes"].append({"name": "EWMA", "value": int(self.input(4))})
        if self.input(5): d["attributes"].append({"name": "LookAroundRate", "value": int(self.input(5))})
        if self.input(6): d["attributes"].append({"name": "LegacyUpdateStatistics", "value": float(self.input(6))})
        if self.input(7): d["attributes"].append({"name": "UpdateStatistics", "value": float(self.input(7))})
        if self.input(8): d["attributes"].append({"name": "HtProtectionMode", "value": self.input(8)})
        if self.input(9): d["attributes"].append({"name": "ErpProtectionMode", "value": self.input(9)})
        if self.input(10): d["attributes"].append({"name": "DefaultTxPowerLevel", "value": int(self.input(10))})
        if self.input(11): d["attributes"].append({"name": "NonUnicastMode", "value": self.input(11)})
        if self.input(12): d["attributes"].append({"name": "FragmentationThreshold", "value": int(self.input(12))})
        if self.input(13): d["attributes"].append({"name": "RtsCtsThreshold", "value": int(self.input(13))})
        if self.input(14): d["attributes"].append({"name": "MaxSlrc", "value": int(self.input(14))})
        if self.input(15): d["attributes"].append({"name": "MaxSsrc", "value": int(self.input(15))})

        self.set_output_val(0, d)

    def get_data(self):
        data = {}
        return data

    def set_data(self, data):
        pass

    def removing(self):
        pass
