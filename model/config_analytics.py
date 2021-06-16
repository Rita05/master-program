import copy

CHART_BUSINESS=0
CHART_BANK=1

class ConfigAnalytics:
    def __init__(self, a=0, d=0, c=0, l=0, k=0, alpha=0, betta=0, range_from=0, range_to=0, range_step=0, range_prop=None):
        self.A = a
        self.D = d
        self.C = c
        self.L = l
        self.k = k
        self.alpha = alpha
        self.betta = betta

        self.range_from = range_from
        self.range_to = range_to
        self.range_step = range_step
        self.range_property = range_prop  # свойство, для которого задан диапазон значений

        self.chart_mode = CHART_BUSINESS

    @staticmethod
    def new_from_row(row: list):
        return ConfigAnalytics(
            row[0],
            row[1],
            row[2],
            row[3],
            row[4],
            row[5],
            row[6],
            row[7],
            row[8],
            row[9],
            row[10]
        )

    def has_range(self):
        return not (self.range_property is None) and (self.range_property != "None")

    def put(self, prop: str, value: str):
        if value != '':
            self.__setattr__(prop, float(value))

    def copy_put(self, prop: str, value: str):
        changed = copy.deepcopy(self)
        changed.put(prop, value)
        return changed