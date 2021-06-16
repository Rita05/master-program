from model.config_imitation import ConfigImitation
from ui.tabs.tab_config_analytics import TabConfigAnalytics
from ui.widgets.model_output_widget import ModelOutputWidget


class TabConfigImitation(TabConfigAnalytics):
    def __init__(self, config: ConfigImitation, output_imitation: ModelOutputWidget):
        super().__init__(config, output_imitation)

        self.add_input(self.layout_right, config.gamma, 'gamma', self.WIDTH, config, 'gamma')
        self.add_input(self.layout_right, config.delta, 'delta', self.WIDTH, config, 'delta')

        self.layout_right.removeWidget(output_imitation)
        self.layout_right.addWidget(output_imitation)