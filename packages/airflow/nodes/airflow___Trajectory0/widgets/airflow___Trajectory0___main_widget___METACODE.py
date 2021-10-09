from NIWENV import *
from PySide2.QtWidgets import QWidget, QVBoxLayout

import numpy as np

import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure
from qbstyles import mpl_style
from mpl_toolkits.mplot3d import Axes3D
from scipy.special import comb

class Point:
    """
    A high-level construct to manipulate and debug 3D points easily.
    """
    def __init__(self, arr=[0,0,0], interest_level=0):
        """
        Default constructor.

        Args:
            arr: Array of 3D coordinates, x, y, and z respectively.
            interest_level: Optional interest level.
        """
        self.x = arr[0]
        self.y = arr[1]
        self.z = arr[2]
        self.interest = interest_level

    def __repr__(self):
        """
        Debug information contained in this structure.

        Returns:
            A construct that summarizes the properties in space of this
            Point instance.
        """
        return f'Point(x:{self.x}; y:{self.y}; z:{self.z}; int:{self.interest})'


class %CLASS%(QWidget, MWB):
    def __init__(self, params):
        MWB.__init__(self, params)
        QWidget.__init__(self)

        self.setStyleSheet('''
            background-color: transparent;
        ''')
        mpl_style(dark=True)

        self.setLayout(QVBoxLayout())
        self.canvas = FigureCanvas(Figure())
        self.layout().addWidget(self.canvas)
        self.layout().setContentsMargins(0,0,0,0)
        self.layout().setSpacing(0)
        self.setFixedWidth(550)
        self.setFixedHeight(500)
        self.ax = self.canvas.figure.add_subplot(111, projection='3d')
        self.canvas.figure.subplots_adjust(left=0, right=1, bottom=0, top=1)

        self.ax.set_title('Drone Trajectory')
        self.ax.set_xlabel('[m]')
        self.ax.set_ylabel('[m]')
        self.ax.set_zlabel('[m]')

    def redraw(self, control_points):
        self.ax.clear()

        points = [Point(p['position'], p['interest']) for p in control_points]
        trajectory = self.build_drone_trajectory(points)
        self.build_drone_space(trajectory, points)

        self.ax.legend()
        self.ax.figure.canvas.draw()

    def build_drone_trajectory(self, drone_positions, step=0.01):
        """
        Build drone trajectory using Bézier Curve model.

        Args:
            drone_positions: Positions of the drone assumed, as an array of Point(s).
            step: Optional step for detailed curve generation.

        Returns:
            Modelled trajectory as an array of Point(s).
        """
        proto = []

        # fill the proto
        for p in drone_positions:
            l = p.interest if p.interest != 0 else 1
            for _ in range(l):
                proto.append(p)

        c = 0.001
        START = 0
        END = 1 + c

        B = [] # Bezier curve points

        for t in np.arange(START, END, step):
            sum_x = 0.0
            sum_y = 0.0
            sum_z = 0.0
            n = len(proto) - 1

            for i in range(n+1):
                a = comb(n, i, exact=True)
                b = (1 - t)**(n - i)
                c = t**i

                sum_x += a * b * c * proto[i].x
                sum_y += a * b * c * proto[i].y
                sum_z += a * b * c * proto[i].z

            B.append(Point([sum_x,sum_y,sum_z]))

        return B

    def build_drone_space(self, trajectory, control_points):
        """
        Draw Drone trajectory in 3D plot.

        Args:
            trajectory: Drone positions.
            control_points: Curve control points.
        """
        # Plot drones trajectories as 3D lines
        # a "o" indicates the start pos. of the drone
        # a "x" indicates the end pos. of the drone
        dx = [p.x for p in trajectory]
        dy = [p.y for p in trajectory]
        dz = [p.z for p in trajectory]

        cpx = [p.x for p in control_points]
        cpy = [p.y for p in control_points]
        cpz = [p.z for p in control_points]

        self.ax.scatter(dx[0], dy[0], dz[0], marker='.', label='Take off')
        self.ax.scatter(dx[-1], dy[-1], dz[-1], marker='x', label='Landing')
        # exclude first and last points because they are relevant to drone take off and landing
        self.ax.scatter(cpx[1:-1], cpy[1:-1], cpz[1:-1], marker='o', label='Control point')
        self.ax.plot(dx, dy, dz, label='Drone trajectory')

    def get_data(self):
        data = {}
        return data

    def set_data(self, data):
        pass

    def remove_event(self):
        pass
