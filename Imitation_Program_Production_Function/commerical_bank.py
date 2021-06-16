import random

from enterpreneur import Entrepreneur


class CommercialBank:
    def __init__(self):
        # Коэффициент корректировки затрат на рекламу банка
        # self.L = 20000 #10000-100000
        self.L = 21000
        # степень влияния процентной ставки по кредиту на рекламные расходы
        # self.delta = 1 / 4
        self.delta = 0.6 #0.1-3.1
        # другие доходы банка
        # self.OBIn = 400000
        self.OBIn = 400000
        # другие расходы банка
        self.PExp = 100000
        #Коэффициент кредитоспособности ИП
        # self.k = 0.15 #0.1-0.5
        self.k = 0.15

    def display_info_(self):
        print("__________________________________________________")
        print("Значения параметров ВЕДУЩЕГО:")
        print("__________________________________________________")
        print(f"Коэффициент корректировки затрат на рекламу банка L = {self.L}")
        print(f"Степень влияния процентной ставки по кредиту на рекламные расходы delta = {self.delta}")
        print(f"Cтавка риска заемщика k = {self.k}")
        print(f"Другие источники дохода банка = {self.OBIn}")
        print(f"Прочие расходы банка = {self.PExp}", "\n")

    def fill_random_parameters(self):
        self.L = random.randrange(10000, 100000)
        self.delta = random.randrange(1, 11)
        self.OBIn = 400000
        self.PExp = 100000

    # функция кредита ИП - S(pr, KR)
    def credit_income(self, pr, m, entrepreneur: Entrepreneur):
        alpha = entrepreneur.alpha
        return (1 + pr) * (entrepreneur.C / ((1 + pr) ** alpha))

    # функция затрат на оценку риска банком - R(m, KR)
    def risk_costs(self, pr, m, entrepreneur: Entrepreneur):
        alpha = entrepreneur.alpha
        return entrepreneur.C * (pr**2 + 1) * m * self.k

    # функция затрат на рекламу банком - Ad(pr)
    def advertising_costs(self, pr):
        return self.L * ((1 + pr) ** self.delta)

    def object_function(self, pr, m, entrepreneur: Entrepreneur):
        credit_income = self.credit_income(pr, m, entrepreneur)
        credit_risk_costs = self.risk_costs(pr, m, entrepreneur)
        advertising_costs = self.advertising_costs(pr)

        return self.OBIn + credit_income - credit_risk_costs -advertising_costs - self.PExp

    def get_bank_subfunctions(self, stack_point_pr, stack_point_m, entrepreneur: Entrepreneur):
        credit_income = self.credit_income(stack_point_pr, stack_point_m, entrepreneur)
        credit_risk_costs = self.risk_costs(stack_point_pr, stack_point_m, entrepreneur)
        advertising_costs = self.advertising_costs(stack_point_pr)

        print(f"ЗНАЧЕНИЯ ФУНКЦИОНАЛОВ ВЕДУЩЕГО: ")
        print("__________________________________________________")
        print(f"Доход банка от кредита ИП = {credit_income}")
        print(f"Затраты на оценку риска банком = {credit_risk_costs}")
        print(f"Затраты банка на рекламу = {advertising_costs}")
