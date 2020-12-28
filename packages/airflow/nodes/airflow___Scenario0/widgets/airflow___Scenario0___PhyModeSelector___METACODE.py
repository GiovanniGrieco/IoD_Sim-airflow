from NIWENV import *
from PySide2.QtWidgets import QComboBox


class %CLASS%(QComboBox, IWB):
    def __init__(self, params):
        IWB.__init__(self, params)
        QComboBox.__init__(self)

        self.setStyleSheet('''

        ''')

        self.addItems([
            'DsssRate1Mbps',
            'DsssRate2Mbps',
            'DsssRate5_5Mbps',
            'DsssRate11Mbps',
            'ErpOfdmRate6Mbps',
            'ErpOfdmRate9Mbps',
            'ErpOfdmRate12Mbps',
            'ErpOfdmRate18Mbps',
            'ErpOfdmRate24Mbps',
            'ErpOfdmRate36Mbps',
            'ErpOfdmRate48Mbps',
            'ErpOfdmRate54Mbps',
            'OfdmRate6Mbps',
            'OfdmRate9Mbps',
            'OfdmRate12Mbps',
            'OfdmRate18Mbps',
            'OfdmRate24Mbps',
            'OfdmRate36Mbps',
            'OfdmRate48Mbps',
            'OfdmRate54Mbps',
            'OfdmRate3MbpsBW10MHz',
            'OfdmRate4_5MbpsBW10MHz',
            'OfdmRate6MbpsBW10MHz',
            'OfdmRate9MbpsBW10MHz',
            'OfdmRate12MbpsBW10MHz',
            'OfdmRate18MbpsBW10MHz',
            'OfdmRate24MbpsBW10MHz',
            'OfdmRate27MbpsBW10MHz',
            'OfdmRate1_5MbpsBW5MHz',
            'OfdmRate2_25MbpsBW5MHz',
            'OfdmRate3MbpsBW5MHz',
            'OfdmRate4_5MbpsBW5MHz',
            'OfdmRate6MbpsBW5MHz',
            'OfdmRate9MbpsBW5MHz',
            'OfdmRate12MbpsBW5MHz',
            'OfdmRate13_5MbpsBW5MHz',
            'HtMcs0',
            'HtMcs1',
            'HtMcs2',
            'HtMcs3',
            'HtMcs4',
            'HtMcs5',
            'HtMcs6',
            'HtMcs7',
            'HtMcs8',
            'HtMcs9',
            'HtMcs10',
            'HtMcs11',
            'HtMcs12',
            'HtMcs13',
            'HtMcs14',
            'HtMcs15',
            'HtMcs16',
            'HtMcs17',
            'HtMcs18',
            'HtMcs19',
            'HtMcs20',
            'HtMcs21',
            'HtMcs22',
            'HtMcs23',
            'HtMcs24',
            'HtMcs25',
            'HtMcs26',
            'HtMcs27',
            'HtMcs28',
            'HtMcs29',
            'HtMcs30',
            'HtMcs31',
            'VhtMcs0',
            'VhtMcs1',
            'VhtMcs2',
            'VhtMcs3',
            'VhtMcs4',
            'VhtMcs5',
            'VhtMcs6',
            'VhtMcs7',
            'VhtMcs8',
            'VhtMcs9',
            'HeMcs0',
            'HeMcs1',
            'HeMcs2',
            'HeMcs3',
            'HeMcs4',
            'HeMcs5',
            'HeMcs6',
            'HeMcs7',
            'HeMcs8',
            'HeMcs9',
            'HeMcs10',
            'HeMcs11'
        ])

    def get_val(self):
        return self.currentText()

    def get_data(self):
        data = self.currentText()
        return data

    def set_data(self, data):
        self.setCurrentText(data)

    def remove_event(self):
        pass
