from NIWENV import *
from PySide2.QtWidgets import QComboBox


class %CLASS%(QComboBox, IWB):
    def __init__(self, params):
        IWB.__init__(self, params)
        QComboBox.__init__(self)

        self.setStyleSheet('''
            QComboBox {
                background-color: transparent;
                border: 2px solid #404040;
                border-radius: 7px;
                color: #aaaaaa;
            }
        ''')

        self.addItems([
            '802.11a',
            '802.11b',
            '802.11g',
            '802.11p',
            '802.11a-holland',
            '802.11n-2.4GHz',
            '802.11n-5GHz',
            '802.11ac',
            '802.11ax-2.4GHz',
            '802.11ax-5GHz'
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
