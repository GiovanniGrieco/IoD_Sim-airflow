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

        self.value = False

    def update_event(self, input_called=-1):
        self.set_output_val(0, self.value)

    def get_data(self):
        data = {
            "value": self.value
        }
        return data

    def set_data(self, data):
        self.value = data['value']
        self.main_widget.update_state(self.value)

    def removing(self):
        pass
