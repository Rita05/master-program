
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QLineEdit

from application_properties import APP_FONT
from model.config_analytics import ConfigAnalytics


class RangeInput(QWidget):
    """Ввод диапазона с определенным шагом"""
    def __init__(self, width: int, state: ConfigAnalytics):
        super().__init__()

        self.setStyleSheet("QWidget { border: none; }")

        self.state = state
        layout = QHBoxLayout()

        EDIT_WIDTH = 56

        edit_from = QLineEdit()
        edit_from.setStyleSheet("QWidget { border: 1px solid gray; }")
        edit_from.setFixedWidth(EDIT_WIDTH)

        edit_to = QLineEdit()
        edit_to.setStyleSheet("QWidget { border: 1px solid gray; }")
        edit_to.setFixedWidth(EDIT_WIDTH)

        edit_step = QLineEdit()
        edit_step.setStyleSheet("QWidget { border: 1px solid gray; }")
        edit_step.setFixedWidth(EDIT_WIDTH)

        edit_from.textChanged.connect(self.__on_edit_from_changed)
        edit_to.textChanged.connect(self.__on_edit_to_changed)
        edit_step.textChanged.connect(self.__on_edit_step_changed)

        layout.addWidget(QLabel("От"))
        layout.addWidget(edit_from)
        layout.addWidget(QLabel("До"))
        layout.addWidget(edit_to)
        layout.addWidget(QLabel("Шаг"))
        layout.addWidget(edit_step)

        self.setLayout(layout)
        self.setFixedWidth(width)

        self.edit_from = edit_from
        self.edit_to = edit_to
        self.edit_step = edit_step

    def set_values(self, range_from: float, range_to: float, step: float):
        self.edit_from.setText(str(range_from))
        self.edit_to.setText(str(range_to))
        self.edit_step.setText(str(step))

    def __on_edit_from_changed(self, value: str):
        self.state.range_from = float(self.fix(value))

    def __on_edit_to_changed(self, value: str):
        self.state.range_to = float(self.fix(value))

    def __on_edit_step_changed(self, value: str):
        self.state.range_step = float(self.fix(value))

    def fix(self, zero_str: str):
        return "0" if zero_str == "" else zero_str