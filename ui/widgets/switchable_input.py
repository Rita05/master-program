from PyQt5.QtWidgets import QHBoxLayout, QPushButton, QVBoxLayout, QGroupBox
from ui.widgets.once_value_input import OnceValueInput
from model.config_analytics import ConfigAnalytics
from ui.widgets.range_input import RangeInput


class SwitchableInput(QGroupBox):
    """Инпут с функцией переключения между вводом одного числа и вводом диапазона"""

    def __init__(self, default_value: str, tooltip: str, width: int, state: ConfigAnalytics, prop_to_edit: str,
                 on_range_edit_start_callback=None):
        super().__init__()

        self.setStyleSheet("QGroupBox { border: 1px outset gray; }")

        RANGE_INPUT_WIDTH = 280
        self.BUTTON_RANGE_WIDTH = 50

        self.on_range_edit_start_callback = on_range_edit_start_callback
        self.state = state
        self.is_range_input = False
        self.prop_to_edit = prop_to_edit
        self.button_switch_to_range = self.__create_button_range()

        layout_base = QVBoxLayout()
        layout_input_with_button = QHBoxLayout()

        once_value_input = OnceValueInput(default_value, tooltip, width, state, prop_to_edit)

        self.range_input = RangeInput(RANGE_INPUT_WIDTH, state)
        self.range_input.hide()

        layout_input_with_button.addWidget(once_value_input)
        layout_input_with_button.addWidget(self.button_switch_to_range)

        layout_base.addLayout(layout_input_with_button)
        layout_base.addWidget(self.range_input)

        self.setLayout(layout_base)

        self.set_edit_range(self.is_range_input)

    def set_edit_range(self, enable: bool, range_from: float = None, range_to: float = None, step: float = None):
        """Переключение между режимами ввода одного значения и ввода диапазона"""
        self.is_range_input = enable
        if enable:
            self.range_input.show()
            self.button_switch_to_range.setText("[*]")
            self.state.range_property = self.prop_to_edit
            if not (range_from is None):
                self.range_input.set_values(range_from, range_to, step)
        else:
            self.range_input.hide()
            self.button_switch_to_range.setText("[...]")

    def __create_button_range(self) -> QPushButton:
        """Кнопка для переключения режима ввода одного значения и диапазона значений"""
        button_range = QPushButton("[...]")
        button_range.setFixedWidth(self.BUTTON_RANGE_WIDTH)
        button_range.clicked.connect(self.__on_range_input_clicked)
        return button_range

    def __on_range_input_clicked(self):
        print(f'Ввод диапазона значений для свойств {self.prop_to_edit}')
        self.is_range_input = not self.is_range_input
        if self.is_range_input:
            if self.on_range_edit_start_callback is not None:
                self.on_range_edit_start_callback()
            self.set_edit_range(True)
        else:
            self.set_edit_range(False)
            self.state.range_property = None
