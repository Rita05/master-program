from PyQt5.QtWidgets import QLabel

from model.model_output import ModelOutput


class ModelOutputWidget(QLabel):
    def __init__(self):
        super().__init__()

    def reset(self, output: ModelOutput):
        self.setStyleSheet("QWidget { border: 1px solid black; padding: 10px; }")
        self.setText(f'            Результаты вычислений\n'
                     f'pr = {output.pr}\n'
                     f'm = {output.m}\n'
                     f'j_bank = {output.j_bank}\n'
                     f'j_business = {output.j_business}')