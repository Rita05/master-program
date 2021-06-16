from typing import List

from model.config_analytics import ConfigAnalytics


class ModelOutput:

    def __init__(self, pr: float = 0, m: float = 0, j_bank: float = 0, j_business: float = 0, business_points: list = [[0, 0]],
                 bank_points: list = [[0, 0]], config: ConfigAnalytics = None):
        self.pr: float = pr
        self.m: float = m
        self.j_bank: float = j_bank
        self.j_business: float = j_business
        self.business_points: List[List[int]] = business_points
        self.bank_points: List[List[int]] = bank_points
        self.config: ConfigAnalytics = config
