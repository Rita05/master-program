from PyQt5.QtWidgets import QWidget, QTabWidget, QMessageBox

from application_properties import CHART_BUSINESS_COLOR, CHART_BANK_COLOR
from model.model import Model
from model.config_analytics import ConfigAnalytics, CHART_BUSINESS
from model.config_imitation import ConfigImitation
from model.model_output import ModelOutput
from database import Database
from ui.tabs.tab_chart import TabChart
from ui.tabs.tab_config_analytics import TabConfigAnalytics
from ui.tabs.tab_config_imitation import TabConfigImitation

from ui.widgets.model_output_widget import ModelOutputWidget


class Controller(QWidget):
    def __init__(self, state_analytics: ConfigAnalytics, state_imitation: ConfigImitation, chart_analytics: TabChart,
                 chart_imitation: TabChart, database: Database, model: Model, tabs: QTabWidget,
                 output_analytics: ModelOutputWidget, output_imitation: ModelOutputWidget):
        super().__init__()

        self.model = model

        self.tabs = tabs

        self.database = database

        self.config_analytics = state_analytics
        self.config_imitation = state_imitation

        self.analytics_chart = chart_analytics
        self.imitation_chart = chart_imitation

        self.output_analytics = output_analytics
        self.output_imitation = output_imitation

        self.last_analytics_output = None
        self.last_imitation_output = None

    def on_button_compute_clicked(self):
        if self.tabs.currentIndex() == 0:
            self.compute_analytics()

        if self.tabs.currentIndex() == 1:
            self.compute_imitation()

    def compute_analytics(self):
        res: ModelOutput = self.model.compute_analytics(self.config_analytics)
        self.__reset_chart(self.config_analytics, self.analytics_chart, self.output_analytics, res)
        self.last_analytics_output = res

    def compute_imitation(self):
        res: ModelOutput = self.model.compute_imitation(self.config_imitation)
        self.__reset_chart(self.config_imitation, self.imitation_chart, self.output_imitation, res)
        self.last_imitation_output = res

    def __reset_chart(self, config: ConfigAnalytics, chart: TabChart, output_widget: ModelOutputWidget, model_output: ModelOutput):
        chart_points = model_output.business_points \
            if config.chart_mode == CHART_BUSINESS \
            else model_output.bank_points
        axis_y_caption = "J_ип" if config.chart_mode == CHART_BUSINESS else "J_кб"
        color = CHART_BUSINESS_COLOR if config.chart_mode == CHART_BUSINESS else CHART_BANK_COLOR
        chart.reset(chart_points, title="", axis_x_caption=config.range_property, axis_y_caption=axis_y_caption, color=color)
        output_widget.reset(model_output)

    def on_button_save_clicked(self):
        try:
            self.database.save_config_analytics(self.config_analytics, self.last_analytics_output or ModelOutput())
            self.database.save_config_imitation(self.config_imitation, self.last_imitation_output or ModelOutput())
        except Exception as ex:
            print(ex)
            QMessageBox.about(self, "Error", f"Ошибка сохранения конфигов: {str(ex)}")