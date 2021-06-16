from PyQt5.QtChart import *
from PyQt5.QtCore import Qt
from typing import List

from PyQt5.QtGui import QPainter, QPen, QColor

from application_properties import CHART_AXIS_X_PRECISION, CHART_AXIS_Y_PRECISION, CHART_WIDTH


class TabChart(QChartView):
    """Виджет с графиком функции"""

    def __init__(self, points: List[List[int]], title: str):
        """
        :param points: Точки для построения графика
        :param title: Заголовок графика
        """
        super().__init__()
        self.setRenderHint(QPainter.Antialiasing)
        self.points = points
        self.chart = None
        self.reset(points, title)

    def reset(self, points: List[List[int]], title: str = "", axis_x_caption: str = "", axis_y_caption: str = "",
              color: str = '#009f9f'):
        """Перерисовывает график"""
        if self.chart is not None:
            # удаление старого графика
            self.chart.deleteLater()
        self.chart = TabChart.__create_chart(points, title, axis_x_caption, axis_y_caption, color)
        self.setChart(self.chart)

    @staticmethod
    def __create_chart(points: List[List[int]], title: str = "", axis_x_caption: str = "",
                       axis_y_caption: str = "", color: str = '#009f9f') -> QChart:
        # chart setting
        chart = QChart()
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTitle(title)
        chart.legend().hide()

        # points
        series = TabChart.__create_series(points, color)
        chart.addSeries(series)

        # axis X
        max_x_value = max(points, key=lambda p: p[0])[0]
        min_x_value = min(points, key=lambda p: p[0])[0]
        axis_x = TabChart.__create_axis(CHART_AXIS_X_PRECISION, min_x_value, max_x_value, axis_x_caption)
        chart.addAxis(axis_x, Qt.AlignBottom)

        # axis Y
        max_y_value = max(points, key=lambda p: p[1])[1]
        min_y_value = min(points, key=lambda p: p[1])[1]
        axis_y = TabChart.__create_axis(CHART_AXIS_Y_PRECISION, min_y_value, max_y_value, axis_y_caption)
        chart.addAxis(axis_y, Qt.AlignLeft)

        return chart

    @staticmethod
    def __create_series(points: List[List[int]], color: str) -> QLineSeries:
        """Преобразование списка точек в Qt структуру"""
        series = QLineSeries()
        for p in points:
            series.append(p[0], p[1])
        # series.setColor(QColor(color))
        pen = QPen()
        pen.setWidth(CHART_WIDTH)
        pen.setColor(QColor(color))
        series.setPen(pen)
        return series

    @staticmethod
    def __create_axis(count: int, min_value: int, max_value: int, caption: str = "") -> QValueAxis:
        """
        Создание оси координат
        :param count: количество точек
        :param min_value: минимальное значение оси
        :param max_value: максимальное значение оси
        """
        axis = QValueAxis()
        axis.setRange(min_value, max_value)
        axis.setTickCount(count)
        axis.setTitleText(caption)
        axis.setLabelFormat("%.2f")
        return axis
