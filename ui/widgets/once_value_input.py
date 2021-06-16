
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QLineEdit
from PyQt5.QtCore import Qt
from model.config_analytics import ConfigAnalytics


class OnceValueInput(QWidget):
    """Ввод параметра модели"""
    def __init__(self, default_value: str, tooltip: str, width: int, state: ConfigAnalytics, prop_to_edit: str):
        super().__init__()

        self.state = state

        # название свойства, которое редактируется
        self.prop_to_edit = prop_to_edit

        layout = QHBoxLayout()
        layout.setAlignment(Qt.AlignLeft)

        label = QLabel(tooltip)
        label.setStyleSheet("QWidget { border: none; }")

        self.edit = QLineEdit()
        self.edit.setFixedWidth(100)
        self.edit.setText(default_value)
        self.edit.textChanged.connect(self.__on_edit_changed)

        layout.addWidget(label)
        layout.addWidget(self.edit)

        self.setLayout(layout)
        self.setFixedWidth(width)

    def __on_edit_changed(self, value):
        """
        Вызывается при изменении значения инпута
        :param value: текущее значение инпута
        """
        print(f'Изменнение значение {self.prop_to_edit} на {value}')
        self.state.put(self.prop_to_edit, value)