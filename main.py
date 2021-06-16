from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTabWidget, QMessageBox

import sys

from ui.controller import Controller
from model.config_analytics import ConfigAnalytics
from model.config_imitation import ConfigImitation
from ui.tabs.tab_chart import TabChart
from ui.tabs.tab_config_analytics import TabConfigAnalytics
from ui.tabs.tab_config_imitation import TabConfigImitation
from ui.widgets.bottom_panel import BottomPanel
from database import Database

from application_properties import *
from ui.widgets.model_output_widget import ModelOutputWidget

from model.model import Model


def start_application():
    application = QApplication(sys.argv)
    QApplication.setFont(APP_FONT)

    # главное окно
    window = QMainWindow()
    window.setWindowTitle("Модель банка и ИП")

    window_layout = QVBoxLayout()

    central_widget = QWidget()
    central_widget.setLayout(window_layout)
    window.setCentralWidget(central_widget)

    tabs = QTabWidget()

    output_analytics = ModelOutputWidget()
    output_imitation = ModelOutputWidget()

    db: Database = Database(DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_DATABASE_NAME)
    connect_database(db)
    config_analytics, config_imitation = load_configs(db)

    input_analytics_tab = TabConfigAnalytics(config_analytics, output_analytics)
    input_imitation_tab = TabConfigImitation(config_imitation, output_imitation)

    chart_analytics_tab = TabChart([[0, 0]], "График аналитики")
    chart_imitation_tab = TabChart([[0, 0]], "График имитации")

    tabs.addTab(input_analytics_tab, "Аналитика")
    tabs.addTab(input_imitation_tab, "Имитация")
    tabs.addTab(chart_analytics_tab, "График аналитики")
    tabs.addTab(chart_imitation_tab, "График имитации")

    model: Model = Model()

    controller = Controller(state_analytics=config_analytics, state_imitation=config_imitation,
                            chart_analytics=chart_analytics_tab, chart_imitation=chart_imitation_tab,
                            database=db, model=model, tabs=tabs, output_analytics=output_analytics,
                            output_imitation=output_imitation)

    bottom_control_panel = BottomPanel(controller, tabs)

    window_layout.addWidget(tabs)
    window_layout.addWidget(bottom_control_panel)

    # controller.compute_analytics()
    # controller.compute_imitation()

    window.show()
    sys.exit(application.exec())


def load_configs(db: Database):
    try:
        return db.load_config_analytics(), db.load_config_imitation()
    except Exception as ex:
        print(ex)
        return ConfigAnalytics(), ConfigImitation()


def connect_database(db: Database):
    try:
        db.connect()
        db.check_connection()
    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    start_application()


