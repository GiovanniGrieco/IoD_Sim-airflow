# stdlib
import os
import re
import subprocess
import tempfile
from sys import platform

# Qt
from PySide2.QtCore import QFile, QObject, Signal
from PySide2.QtWidgets import QFileDialog, QMessageBox

# UI
from custom_src.code_gen.CodeGenerator import CodeGenerator
from ui.w_ui_script import WUIScript

from custom_src.Flow import Flow
from custom_src.Log import Logger
from custom_src.script_variables.VarsManager import VarsManager
from custom_src.source_code_preview.CodePreview_Widget import CodePreview_Widget
from custom_src.global_tools.Debugger import Debugger

class Script(QObject):

    name_changed = Signal(str)

    def __init__(self, main_window, name, config=None):
        super(Script, self).__init__()

        self.main_window = main_window
        self.widget = WUIScript()

        # GENERAL ATTRIBUTES
        self.logger = Logger(self)
        # self.variables = []
        self.vars_manager = None
        self.name = name
        self.flow = None
        self.thumbnail_source = ''  # URL to the Script's thumbnail picture
        self.code_preview_widget = CodePreview_Widget()

        if config:
            self.name = config['name']
            self.vars_manager = VarsManager(self, config['variables'])
            self.flow = Flow(main_window, self, config['flow'])
        else:
            self.flow = Flow(main_window, self)
            self.vars_manager = VarsManager(self)

        # variables list widget
        self.widget.ui.variables_scrollArea.setWidget(self.vars_manager.list_widget)
        self.widget.ui.add_variable_push_button.clicked.connect(self.add_var_clicked)
        self.widget.ui.new_var_name_lineEdit.returnPressed.connect(self.new_var_line_edit_return_pressed)

        # flow
        self.widget.ui.splitter.insertWidget(0, self.flow)

        # IoD Sim Toolbox
        self.tmp_dir = tempfile.mkdtemp()
        self.iodsim_location = None
        self.widget.ui.pushButton_IoDSimLocation.clicked.connect(self.set_iodsim_location_clicked)
        self.widget.ui.button_Build_IoDSimTools.clicked.connect(self.build_iodsim_scenario_clicked)
        self.widget.ui.button_Run_IoDSimTools.clicked.connect(self.run_iodsim_scenario_clicked)

    def show_NI_code(self, ni):
        """Called from Flow when the selection changed."""
        self.code_preview_widget.set_new_NI(ni)

    def add_var_clicked(self):
        self.vars_manager.create_new_var_and_update(self.widget.ui.new_var_name_lineEdit.text())

    def new_var_line_edit_return_pressed(self):
        self.vars_manager.create_new_var_and_update(self.widget.ui.new_var_name_lineEdit.text())

    def generate_code(self):
        """In production, no working prototype"""
        cg = CodeGenerator(self.main_window,
                           self.flow.all_node_instances,
                           self.vars_manager.config_data(),
                           self.flow.algorithm_mode)
        code = cg.generate()
        if code is None:
            print('couldn\'t generate code')
        else:
            print(code)


    def config_data(self):
        script_dict = {'name': self.name,
                       'variables': self.vars_manager.config_data(),
                       'flow': self.flow.config_data()}

        return script_dict

    def set_iodsim_location_clicked(self):
        dir_name = QFileDialog.getExistingDirectory(None, "Select IoD Sim Location",
                                                    "~/",
                                                    QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks)
        self.iodsim_location = dir_name
        Debugger.debug(f'IoD Sim Location set to {self.iodsim_location}')

    def build_iodsim_scenario_clicked(self):
        if self.iodsim_location is not None:
            scenario_config_path = self.get_temp_file('dry_run.json')
            self.main_window.on_export_scenario_triggered(scenario_config_path, is_dry_run=True)
            self.run_iodsim('Build', scenario_config_path)
        else:
            QMessageBox.warning(self.main_window, 'Error', 'Please select IoD Sim Location first!')

    def run_iodsim_scenario_clicked(self):
        if self.iodsim_location is not None:
            scenario_config_path = self.get_temp_file('scenario.json')
            self.main_window.on_export_scenario_triggered(scenario_config_path)
            self.run_iodsim('Build', scenario_config_path)
        else:
            QMessageBox.warning(self.main_window, 'Error', 'Please select IoD Sim Location first!')

    def get_temp_file(self, file_name):
        tmp_file_path = os.path.join(self.tmp_dir, file_name)
        tmp_file_path = tmp_file_path.replace('\\', '\\\\')
        Debugger.debug('Will save tmp file in', tmp_file_path)

        return tmp_file_path

    def run_iodsim(self, operation, scenario_config_path):
        # Check if we are under Linux or Windows
        if platform == "linux" or platform == "linux2":
            try:
                ret = subprocess.run(f'./waf --run \"iod-sim --config={scenario_config_path}\"',
                                        cwd=f'{self.iodsim_location}/ns3/',
                                        capture_output=True,
                                        check=True)

                print(f'\nIoD Sim {operation} SUMMARY\n{ret.stdout.decode()}')
            except subprocess.TimeoutExpired as e:
                QMessageBox.warning(self.main_window, 'Error', f'Timeout while running IoD Sim: {e.stderr.decode()}')
                Debugger.debug(e.output.decode())
                Debugger.debugerr(e.stderr.decode())
            except subprocess.CalledProcessError as e:
                msg = e.stderr.decode()
                if 'msg=' in msg:
                    msg = re.compile(r'msg="(.*)", file=').search(msg).group(1)

                QMessageBox.warning(self.main_window, 'Error', f'An error occurred while running IoD Sim: {msg}')
                Debugger.debug(e.output.decode())
                Debugger.debugerr(e.stderr.decode())
        elif platform == "win32":
            if '//wsl$/' in self.iodsim_location:
                try:
                    ret = subprocess.run(f'wsl wslpath {self.iodsim_location}',
                                            capture_output=True,
                                            check=True)
                    iodsim_linux_path = ret.stdout.decode().strip()

                    ret = subprocess.run(f'wsl wslpath {scenario_config_path}',
                                            capture_output=True,
                                            check=True)
                    config_linux_path = ret.stdout.decode().strip()

                    try:
                        ret = subprocess.run(f'bash -c "cd {iodsim_linux_path}/ns3 && '
                                             f'./waf --run \'iod-sim --config={config_linux_path}\'',
                                             capture_output=True,
                                             check=True)

                        print(f'\nIoD Sim {operation} SUMMARY\n{ret.stdout.decode()}')
                    except subprocess.TimeoutExpired as e:
                        QMessageBox.warning(self.main_window, 'Error', f'Timeout while running IoD Sim: {e.stderr.decode()}')
                        Debugger.debug(e.output.decode())
                        Debugger.debugerr(e.stderr.decode())
                    except subprocess.CalledProcessError as e:
                        msg = e.stderr.decode()
                        if 'msg=' in msg:
                            msg = re.compile(r'msg="(.*)", file=').search(msg).group(1)

                        QMessageBox.warning(self.main_window, 'Error', f'An error occurred while running IoD Sim: {msg}')
                        Debugger.debug(e.output.decode())
                        Debugger.debugerr(e.stderr.decode())
                except subprocess.CalledProcessError as e:
                    QMessageBox.warning(self.main_window, 'Error', 'Failed to run WSL. Please make sure WSL is correctly installed.')
                    Debugger.debug(e.stdout.decode())
                    Debugger.debugerr(e.stderr.decode())
            else:
                Debugger.debugerr(f'Invalid IoD Sim Path: {self.iodsim_location}')
                QMessageBox.warning(self.main_window, 'Error',
                                    'Windows is only supported with WSL enabled. '
                                    'Please provide a valid WSL path to reach IoD Sim.')
        elif platform == "darwin":
            QMessageBox.warning(self.main_window, 'Error', 'macOS is not supported, yet. Please use Linux or Windows OS.')
