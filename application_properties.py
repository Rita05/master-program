from PyQt5.QtGui import QFont

# DB_HOST = "192.168.31.108"
DB_HOST = "localhost"
DB_PORT = 5432
DB_USER = "postgres"
# DB_PASSWORD = "13467950"
DB_PASSWORD = "kiptorn5"
# DB_DATABASE_NAME = "postgres"
DB_DATABASE_NAME = "postgresdb"

FONT_FAMILY = "Monospace"
FONT_SIZE = 10
FONT_WEIGHT = QFont.Monospace
FONT_ITALIC = False
APP_FONT = QFont(FONT_FAMILY, FONT_SIZE, FONT_WEIGHT, FONT_ITALIC)

CHART_AXIS_X_PRECISION = 10
CHART_AXIS_Y_PRECISION = 10
CHART_BANK_COLOR = '#3399FF'
CHART_BUSINESS_COLOR = '#009999'
CHART_WIDTH=3