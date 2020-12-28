from NIENV import *


# API METHODS --------------

# self.main_widget
# self.update_shape()

# Ports
# self.input(index)
# self.set_output_val(index, val)
# self.exec_output(index)

# self.create_new_input(type_, label, widget_name=None, widget_pos='under', pos=-1)
# self.delete_input(index)
# self.create_new_output(type_, label, pos=-1)
# self.delete_output(index)

# Logging
# mylog = self.new_log('Example Log')
# mylog.log('I\'m alive!!')
# self.log_message('hello global!', target='global')
# self.log_message('that\'s not good', target='error')

# --------------------------


class %CLASS%(NodeInstance):
    def __init__(self, params):
        super(%CLASS%, self).__init__(params)

        self.special_actions['add input'] = {'method': M(self.action_add_input)}
        self.num_data_inputs = 1
        self.special_actions[f'remove input {self.num_data_inputs}'] = {
            'method': M(self.action_remove_input),
            'data': self.num_data_inputs - 1 # -1 because index number
        }

    def action_add_input(self):
        self.create_new_input('data', '')
        self.num_data_inputs += 1
        self.special_actions[f'remove input {self.num_data_inputs}'] = {
            'method': M(self.action_remove_input),
            'data': self.num_data_inputs - 1 # -1 because index number
        }

    def action_remove_input(self, index):
        self.delete_input(index)

        # rebuilding special actions
        for i in range(self.num_data_inputs):
            del self.special_actions[f'remove input {i + 1}']
        self.num_data_inputs -= 1
        for i in range(self.num_data_inputs):
            self.special_actions[f'remove input {i + 1}'] = {
                'method': M(self.action_remove_input),
                'data': i
            }

    def update_event(self, input_called=-1):
        self.set_output_val(0, [_in.get_val() for _in in self.inputs])

    def get_data(self):
        data = {
            'num data inputs': self.num_data_inputs
        }
        return data

    def set_data(self, data):
        self.num_data_inputs = data['num data inputs']
        pass

    def removing(self):
        pass
