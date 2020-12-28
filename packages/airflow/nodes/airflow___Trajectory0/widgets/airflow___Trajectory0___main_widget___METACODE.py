from NIWENV import *
from PySide2.QtWidgets import QWidget, QVBoxLayout

import numpy as np

import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvas, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from qbstyles import mpl_style
from mpl_toolkits.mplot3d import Axes3D
from scipy.special import binom

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

        ''')
        mpl_style(dark=True)

        self.setLayout(QVBoxLayout())
        self.canvas = FigureCanvas(Figure(figsize=(5, 3)))
        self.layout().addWidget(self.canvas)
        self.setFixedWidth(550)
        self.setFixedHeight(500)
        self.ax = self.canvas.figure.add_subplot(111, projection='3d')
        
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
        # Interest = 0 => start/stop of a given trajectory, cut the Bézier Curve.
        trajectories = []
        trajectory = []

        # populate trajectories
        for pos in drone_positions:
            trajectory.append(pos)

            if pos.interest == 0 and len(trajectory) > 1:
                trajectories.append(trajectory)
                # clean up
                trajectory = [pos]

        # tolerance in case the user forgot to add the last point with interest = 0
        if len(trajectory) > 1:
            trajectories.append(trajectory)

        # construct trajectory
        B = []  # Bezier curve, our trajectory

        for tr in trajectories:
            for t in np.arange(0, 1, step):
                sum_x = 0.0
                sum_y = 0.0
                sum_z = 0.0
                n = len(tr)

                for i in range(n):
                    a = binom(n, i)
                    b = (1 - t)**(n - i)
                    c = t**i

                    sum_x += a * b * c * tr[i].x
                    sum_y += a * b * c * tr[i].y
                    sum_z += a * b * c * tr[i].z

                B.append(Point([sum_x, sum_y, sum_z]))

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
