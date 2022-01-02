from PySide2.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QPlainTextEdit, QLabel, QLayout
from PySide2.QtGui import QFont

from custom_src.global_tools.strings import shorten


class Logger(QWidget):

    def __init__(self, script):
        super(Logger, self).__init__()

    def log_message(self, message: str, target=''):
        pass

    def new_log(self, new_sender, title):
        pass

class Log(QWidget):
    def __init__(self, sender, title=''):
        super(Log, self).__init__()

    def log(self, *args):
        pass

    def clear(self):
        pass

    def disable(self):
        pass

    def enable(self):
        pass

    def remove_clicked(self):
        pass
