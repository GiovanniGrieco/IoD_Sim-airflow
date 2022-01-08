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
    default_type = 'Residential'
    default_walls = 'ConcreteWithWindows'
    default_boundaries = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    default_floors = 1
    default_rooms = [1, 1]

    def __init__(self, params):
        super(%CLASS%, self).__init__(params)

    def update_event(self, input_called=-1):
        btype = self.input(0) if self.input(0) is not None else self.default_type
        bwalls = self.input(1) if self.input(1) is not None else self.default_walls
        boundaries = self.input(2) if self.input(2) is not None else self.default_boundaries
        floors = self.input(3) if self.input(3) is not None else self.default_floors
        rooms = self.input(4) if self.input(4) is not None else self.default_rooms

        self.set_output_val(0, {
            'type': btype,
            'walls': bwalls,
            'boundaries': boundaries,
            'floors': floors,
            'rooms': rooms
        })

    def get_data(self):
        data = {}
        return data

    def set_data(self, data):
        pass

    def removing(self):
        pass
