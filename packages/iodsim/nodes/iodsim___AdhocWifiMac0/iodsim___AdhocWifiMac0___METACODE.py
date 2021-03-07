from NIENV import *

class %CLASS%(NodeInstance):
    def __init__(self, params):
        super(%CLASS%, self).__init__(params)

    def update_event(self, input_called=-1):
        d = {
            'name': "ns3::AdhocWifiMac",
            'attributes': []
        }

        if self.input(0): d["attributes"].append({"name": "BK_Txop", "value": self.input(0)})
        if self.input(1): d["attributes"].append({"name": "BE_Txop", "value": self.input(1)})
        if self.input(2): d["attributes"].append({"name": "VI_Txop", "value": self.input(2)})
        if self.input(3): d["attributes"].append({"name": "VO_Txop", "value": self.input(3)})
        if self.input(4): d["attributes"].append({"name": "Txop", "value": self.input(4)})
        if self.input(5): d["attributes"].append({"name": "ShortSlotTimeSupported", "value": bool(self.input(5))})
        if self.input(6): d["attributes"].append({"name": "BK_BlockAckInactivityTimeout", "value": int(self.input(6))})
        if self.input(7): d["attributes"].append({"name": "BE_BlockAckInactivityTimeout", "value": int(self.input(7))})
        if self.input(8): d["attributes"].append({"name": "VI_BlockAckInactivityTimeout", "value": int(self.input(8))})
        if self.input(9): d["attributes"].append({"name": "VO_BlockAckInactivityTimeout", "value": int(self.input(9))})
        if self.input(10): d["attributes"].append({"name": "BK_BlockAckThreshold", "value": int(self.input(10))})
        if self.input(11): d["attributes"].append({"name": "BE_BlockAckThreshold", "value": int(self.input(11))})
        if self.input(12): d["attributes"].append({"name": "VI_BlockAckThreshold", "value": int(self.input(12))})
        if self.input(13): d["attributes"].append({"name": "VO_BlockAckThreshold", "value": int(self.input(13))})
        if self.input(14): d["attributes"].append({"name": "BK_MaxAmpduSize", "value": int(self.input(14))})
        if self.input(15): d["attributes"].append({"name": "BE_MaxAmpduSize", "value": int(self.input(15))})
        if self.input(16): d["attributes"].append({"name": "VI_MaxAmpduSize", "value": int(self.input(16))})
        if self.input(17): d["attributes"].append({"name": "VO_MaxAmpduSize", "value": int(self.input(17))})
        if self.input(18): d["attributes"].append({"name": "BK_MaxAmsduSize", "value": int(self.input(18))})
        if self.input(19): d["attributes"].append({"name": "BE_MaxAmsduSize", "value": int(self.input(19))})
        if self.input(20): d["attributes"].append({"name": "VI_MaxAmsduSize", "value": int(self.input(20))})
        if self.input(21): d["attributes"].append({"name": "VO_MaxAmsduSize", "value": int(self.input(21))})
        if self.input(22): d["attributes"].append({"name": "CtsToSelfSupported", "value": bool(self.input(22))})
        if self.input(23): d["attributes"].append({"name": "QosSupported", "value": bool(self.input(23))})
        if self.input(24): d["attributes"].append({"name": "Ssid", "value": self.input(24)})

        self.set_output_val(0, d)

    def get_data(self):
        data = {}
        return data

    def set_data(self, data):
        pass

    def removing(self):
        pass
