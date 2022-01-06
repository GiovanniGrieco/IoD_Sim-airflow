from NIWENV import *
from PySide2.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QFileDialog


class %CLASS%(QWidget, MWB):
    def __init__(self, params):
        MWB.__init__(self, params)
        QWidget.__init__(self)

        self.directory = ''

        # UI
        self.setLayout(QVBoxLayout())
        self.path_line_edit = QLineEdit()
        self.path_line_edit.setPlaceholderText('directory...')
        self.path_line_edit.textChanged.connect(M(self.set_directory_path))
        self.select_directory_button = QPushButton('select')
        self.select_directory_button.clicked.connect(M(self.select_directory_button_clicked))
        self.layout().addWidget(self.path_line_edit)
        self.layout().addWidget(self.select_directory_button)
        self.setFixedWidth(150)

    def select_directory_button_clicked(self):
        directory_path = QFileDialog.getExistingDirectory(self, 'Select Directory')
        if len(directory_path) > 0:
            self.set_directory_path(directory_path)

    def set_directory_path(self, new_directory_path):
        self.directory = new_directory_path
        self.path_line_edit.setText(self.directory)
        self.parent_node_instance.outputs[0].set_val(self.directory)
        self.parent_node_instance.value = self.directory

    def get_val(self):
        return self.directory

    def get_data(self):
        return self.get_val()

    def set_data(self, data):
        self.set_directory_path(data)

    # remove logs and stop threads and timers here
    def remove_event(self):
        pass
