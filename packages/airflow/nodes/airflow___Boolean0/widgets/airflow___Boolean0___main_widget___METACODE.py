import pathlib

from NIWENV import *
package_path = pathlib.Path(widget_pp(__file__)).as_posix()

from PySide2.QtWidgets import QCheckBox

class %CLASS%(QCheckBox, MWB):
    def __init__(self, params):
        MWB.__init__(self, params)
        QCheckBox.__init__(self, "")

        print(package_path)

        self.setStyleSheet(f'''
        QCheckBox {{
            spacing: 90px;
            background-color: transparent;
        }}
        QCheckBox::indicator {{
            background-color: #bcbbf2;
        }}
        QCheckBox::indicator:checked {{
            image: url("{package_path}/resources/checkbox_checked.png");
        }}
        QCheckBox::indicator:unchecked {{
            image: url("{package_path}/resources/checkbox_unchecked.png");
        }}
        ''')

        self.clicked.connect(M(self.on_click))

    def on_click(self):
        state = self.isChecked()
        self.parent_node_instance.outputs[0].set_val(state)
        self.parent_node_instance.value = state

    def get_data(self):
        data = {}
        return data

    def set_data(self, data):
        pass

    def update_state(self, value):
        self.setChecked(value)
        state = value

    def remove_event(self):
        pass
