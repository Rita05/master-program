from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QBoxLayout, QSizePolicy
from model.config_analytics import ConfigAnalytics
from ui.widgets.chart_mode_selector import ChartModeSelector
from ui.widgets.model_output_widget import ModelOutputWidget
from ui.widgets.switchable_input import SwitchableInput
from PyQt5.QtCore import Qt


class TabConfigAnalytics(QWidget):
    def __init__(self, config: ConfigAnalytics, model_output_widget: ModelOutputWidget):
        super().__init__()

        WIDTH = 200

        # храним поля ввода, чтобы скрывать ввод диапазона всех полей когда открываем ввод диапазона одного поля
        self.inputs = []
        self.config = config

        # левый столбец
        layout_left = QVBoxLayout()
        # правый столбец
        layout_right = QVBoxLayout()
        layout_right.setAlignment(Qt.AlignTop)

        layout_base = QHBoxLayout()
        layout_base.addLayout(layout_left)
        layout_base.addLayout(layout_right)
        layout_base.setAlignment(Qt.AlignTop)

        self.setLayout(layout_base)
        self.layout_left = layout_left
        self.layout_right = layout_right
        self.WIDTH = WIDTH

        layout_left.addWidget(ChartModeSelector(config))

        # левый стоблец
        self.add_input(layout_left, config.A, 'A', WIDTH, config, 'A')
        self.add_input(layout_left, config.C, 'C', WIDTH, config, 'C')
        self.add_input(layout_left, config.D, 'D', WIDTH, config, 'D')
        self.add_input(layout_left, config.L, 'L', WIDTH, config, 'L')

        self.add_input(layout_left, config.k, 'k', WIDTH, config, 'k')
        self.add_input(layout_right, config.alpha, 'alpha', WIDTH, config, 'alpha')
        self.add_input(layout_right, config.betta, 'betta', WIDTH, config, 'betta')

        layout_right.addWidget(model_output_widget)

        self.expand_selected_range()

    def expand_selected_range(self):
        for w in self.inputs:
            if w.prop_to_edit == self.config.range_property:
                w.set_edit_range(True, self.config.range_from, self.config.range_to, self.config.range_step)
            else:
                w.set_edit_range(False)

    def add_input(self, layout: QBoxLayout, default_value: str, tooltip: str, width: int, config: ConfigAnalytics,
                  prop: str):
        """Добавляет инпут в заданый столбец"""
        new_input = SwitchableInput(str(default_value), tooltip, width, config, prop, self.on_range_input_enabled)
        self.inputs.append(new_input)
        layout.addWidget(new_input)

    def on_range_input_enabled(self):
        """Когда открываем у какого-то инпута ввод диапазона, скрываем даиапзон у всех остальных
        инпутов (чтобы не получилось, что вводим одновременно два инпута)"""
        for w in self.inputs:
            w.set_edit_range(False)
