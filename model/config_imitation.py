from model.config_analytics import ConfigAnalytics


class ConfigImitation(ConfigAnalytics):
    def __init__(self, a=0, d=0, c=0, l=0, k=0, alpha=0, betta=0, gamma=0, delta=0, range_from=0, range_to=0, range_step=0, range_prop=None):
        super().__init__(a, d, c, l, k, alpha, betta, range_from, range_to, range_step, range_prop)

        self.gamma = gamma
        self.delta = delta

    @staticmethod
    def new_from_row(row: list):
        return ConfigImitation(
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
            row[10],
            row[11],
            row[12]
        )