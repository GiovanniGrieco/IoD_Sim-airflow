from PySide2.QtCore import QObject, Signal, Qt
from PySide2.QtGui import QPen, QColor, QBrush

from custom_src.NodeInstancePainter import NIPainter_Light, NIPainter_Dark


class FlowTheme:
    """A FlowTheme holds all design information for the flow. And it defines what
    themes exist. Notice, that all drawing of NodeInstances and PortInstances
    is done by NIPainter classes, while for each FlowTheme there exists exactly
    one NIPainter class.

    HOW TO CREATE NEW THEMES
    - Create a new subclass of NIPainter in NodeInstancePainter.py, and implement
    all methods that are passed in NIPainter (take a look at the other already
    existing NIPainter subclasses there for reference)
    - Add a new theme entry to the flow_themes array of DesignContainer and
    reference the new NIPainter subclass for your new theme you just made"""

    def __init__(self, name,
                 flow_conn_exec_color, flow_conn_exec_width, flow_conn_exec_pen_style,
                 flow_conn_data_color, flow_conn_data_width, flow_conn_data_pen_style,
                 node_instance_painter,
                 flow_background_color=QColor('#fefefe')):
        self.name = name
        self.node_inst_painter = node_instance_painter

        self.flow_conn_exec_pen = QPen(flow_conn_exec_color, flow_conn_exec_width)
        self.flow_conn_exec_pen.setStyle(flow_conn_exec_pen_style)
        self.flow_conn_exec_pen.setCapStyle(Qt.RoundCap)

        self.flow_conn_data_pen = QPen(flow_conn_data_color, flow_conn_data_width)
        self.flow_conn_data_pen.setStyle(flow_conn_data_pen_style)
        self.flow_conn_data_pen.setCapStyle(Qt.RoundCap)

        self.flow_background_color = flow_background_color

    def get_flow_conn_pen_inst(self, connection_type):
        if connection_type == 'data':
            return self.flow_conn_data_pen.__copy__()
        else:
            return self.flow_conn_exec_pen.__copy__()

class DesignContainer(QObject):
    flow_themes = [
        FlowTheme('light',
                  QColor('#0000ff'),
                  2,
                  Qt.SolidLine,
                  QColor('#00ff00'),
                  2,
                  Qt.DashLine,
                  NIPainter_Light,
                  QColor('#fefefe')),
        FlowTheme('dark',
                  QColor('#ffffff'),
                  2,
                  Qt.SolidLine,
                  QColor('#ffffff'),
                  2,
                  Qt.DashLine,
                  NIPainter_Dark,
                  QColor('#1e1e1e'))
    ]

    start_flow_theme = flow_themes[-1]
    flow_theme = None  # initialized by MainWindow
    flow_theme_changed = Signal(str)
    performance_mode = 'pretty'

    def set_flow_theme(self, new_theme: str = None):
        self.flow_theme = new_theme if new_theme is not None else self.start_flow_theme
        self.flow_theme_changed.emit(self.flow_theme.name)

    def set_performance_mode(self, new_mode):
        self.performance_mode = new_mode
        if new_mode == 'fast':
            Design.node_instance_shadows_shown = False
        else:
            Design.node_instance_shadows_shown = True

        # the performance mode affects the flow's foreground theme
        self.flow_theme_changed.emit(self.flow_theme)

    ryven_stylesheet = None
    node_instance_shadows_shown = False
    animations_enabled = True


# I have to instantiate the Design in order to execute Qt Signals
Design = DesignContainer()
