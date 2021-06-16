import psycopg2

from model.config_analytics import ConfigAnalytics
from model.config_imitation import ConfigImitation
from model.model_output import ModelOutput

TB_ANALYTICS = "analytics"
TB_IMITATION = "imitation"


class Database:
    def __init__(self, host: str, port: int, user: str, password: str, db_name: str):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db_name = db_name

        self.connection = None
        self.cursor = None
        self.is_connected = False

    def connect(self):
        self.connection = psycopg2.connect(host=self.host, port=self.port, user=self.user, password=self.password,
                                           dbname=self.db_name)
        self.cursor = self.connection.cursor()
        self.is_connected = True
        self.__initialize_tables()

    def __initialize_tables(self):
        self.cursor.execute(f"create table if not exists {TB_ANALYTICS} "
                            f"(a real, d real, c real, l real, k real, alpha real, betta real,"
                            f"range_from real, range_to real, step real, prop text, pr real, m real, j_bank real, j_business real);")
        self.connection.commit()

        self.cursor.execute(f"create table if not exists {TB_IMITATION} "
                            f"(a real, d real, c real, l real, k real, alpha real, betta real, gamma real, delta real,"
                            f"range_from real, range_to real, step real, prop text, pr real, m real, j_bank real, j_business real);")
        self.connection.commit()

    def check_connection(self):
        print("Database connected. Fetching version...")
        self.cursor.execute("select version();")
        print(f'Database version {self.cursor.fetchone()}')

    def load_config_analytics(self) -> ConfigAnalytics:
        self.cursor.execute(f"select * from {TB_ANALYTICS};")
        row = self.cursor.fetchall()[-1]
        return ConfigAnalytics.new_from_row(row)

    def load_config_imitation(self) -> ConfigImitation:
        self.cursor.execute(f"select * from {TB_IMITATION};")
        row = self.cursor.fetchall()[-1]
        return ConfigImitation.new_from_row(row)

    def save_config_analytics(self, conf: ConfigAnalytics, out: ModelOutput):
        self.cursor.execute(
            f"insert into {TB_ANALYTICS} (a, d, c, l, k, alpha, betta, range_from, range_to, step, prop, pr, m, j_bank, j_business)"
            f" values ({conf.A}, {conf.D}, {conf.C}, {conf.L}, {conf.k}, {conf.alpha}, {conf.betta},"
            f" {conf.range_from}, {conf.range_to}, {conf.range_step}, '{conf.range_property}', {out.pr}, {out.m}, {out.j_bank}, {out.j_business});")
        self.connection.commit()

    def save_config_imitation(self, conf: ConfigImitation, out: ModelOutput):
        self.cursor.execute(
            f"insert into {TB_IMITATION} (a, d, c, l, k, alpha, betta, gamma, delta, range_from, range_to, step, prop, pr, m, j_bank, j_business)"
            f" values ({conf.A}, {conf.D}, {conf.C}, {conf.L}, {conf.k}, {conf.alpha}, {conf.betta}, {conf.gamma}, {conf.delta},"
            f" {conf.range_from}, {conf.range_to}, {conf.range_step}, '{conf.range_property}', {out.pr}, {out.m}, {out.j_bank}, {out.j_business});")
        self.connection.commit()
