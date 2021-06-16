from PyQt5.QtWidgets import QWidget, QHBoxLayout, QRadioButton, QLabel

from model.config_analytics import CHART_BUSINESS, CHART_BANK, ConfigAnalytics


class ChartModeSelector(QWidget):
    def __init__(self, config: ConfigAnalytics):
        super().__init__()
        self.current_mode = config.chart_mode
        self.config = config

        layout = QHBoxLayout()

        layout.addWidget(QLabel("Тип графика:"))

        btn = QRadioButton("ИП")
        btn.setChecked(True if config.chart_mode == CHART_BUSINESS else False)
        btn.mode = CHART_BUSINESS
        btn.toggled.connect(self.on_clicked)
        layout.addWidget(btn)

        btn = QRadioButton("Банк")
        btn.setChecked(True if config.chart_mode == CHART_BANK else False)
        btn.mode = CHART_BANK
        btn.toggled.connect(self.on_clicked)
        layout.addWidget(btn)

        self.setLayout(layout)

    def on_clicked(self):
        b = self.sender()
        if b.isChecked():
            self.current_mode = b.mode
            self.config.put("chart_mode", b.mode)
