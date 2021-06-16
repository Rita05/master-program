
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton, QTabWidget
from PyQt5.QtCore import Qt
from ui.controller import Controller


class BottomPanel(QWidget):
    def __init__(self, controller: Controller, tabs: QTabWidget):
        super().__init__()

        layout = QHBoxLayout()
        layout.setAlignment(Qt.AlignRight)
        self.setLayout(layout)

        button_compute = QPushButton("Рассчитать")
        button_compute.setFixedWidth(150)
        button_compute.clicked.connect(controller.on_button_compute_clicked)

        button_save = QPushButton("Сохранить")
        layout.addWidget(button_save)
        layout.addWidget(button_compute)
        button_save.clicked.connect(controller.on_button_save_clicked)

        self.button_compute = button_compute
        self.button_save = button_save

        tabs.currentChanged.connect(self.on_tab_changed)

    def on_tab_changed(self, index: int):
        if index == 0 or index == 1:
            self.button_compute.show()
            self.button_save.show()
        else:
            self.button_compute.hide()
            self.button_save.hide()
