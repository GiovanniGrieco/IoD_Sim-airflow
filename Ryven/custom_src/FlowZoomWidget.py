from PySide2.QtWidgets import QWidget, QPushButton, QHBoxLayout


class FlowZoomWidget(QWidget):
    def __init__(self, flow):
        super(FlowZoomWidget, self).__init__()

        self.flow = flow

        self.zoom_in_button = QPushButton('+')
        self.zoom_in_button.clicked.connect(self.on_zoom_in_button_clicked)
        self.zoom_out_button = QPushButton('-')
        self.zoom_out_button.clicked.connect(self.on_zoom_out_button_clicked)

        main_horizontal_layout = QHBoxLayout()

        main_horizontal_layout.addWidget(self.zoom_out_button)
        main_horizontal_layout.addWidget(self.zoom_in_button)
        self.setLayout(main_horizontal_layout)


        self.setStyleSheet('''
            background: transparent;
            border: none;
        ''')

        self.zoom_in_button.setStyleSheet('''
            QPushButton {
                background-color: #eef4f9;
                border: 1px solid #dce1e5;
                border-radius: 8px;
                color: #191919;
                height: 35px;
                width: 35px;
                font-size: 28px;
                vertical-align: middle;
            }
            QPushButton:hover:pressed {
                background-color: #e6ebf0;
            }
        ''')

        self.zoom_out_button.setStyleSheet('''
            QPushButton {
                background-color: #eef4f9;
                border: 1px solid #dce1e5;
                border-radius: 8px;
                color: #191919;
                height: 35px;
                width: 35px;
                font-size: 28px;
                vertical-align: middle;
            }
            QPushButton:hover:pressed {
                background-color: #e6ebf0;
            }
        ''')


    def on_zoom_in_button_clicked(self):
        self.flow.zoom_in(250)

    def on_zoom_out_button_clicked(self):
        self.flow.zoom_out(250)