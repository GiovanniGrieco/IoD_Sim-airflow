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

        self.key_lookup = {
            'Name': 'name',
            'Log on File': 'logOnFile',
            'Duration': 'duration',
            'Results Path': 'resultsPath',
            'Log Components': 'logComponents',
            'World': "world",
            'ns3 Config': 'staticNs3Config',
            'PHY Layers': 'phyLayer',
            'MAC Layers': 'macLayer',
            'NET Layers': 'networkLayer',
            'Drone List': 'drones',
            'ZSP List': 'ZSPs',
            'Remote List': 'remotes'
        }

        # self.special_actions['action name'] = {'method': M(self.action_method)}
        # ...

    def update_event(self, input_called=-1):
        pass

    def get_data(self):
        return {self.key_lookup[x.label_str]: x.get_val() for x in self.inputs}

    def set_data(self, data):
        pass

    def removing(self):
        pass
