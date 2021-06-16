import math

import random


class Entrepreneur:
    def __init__(self):
        # Коэффициет факторной производительности A
        # self.A = 4000  # 3000-6000
        self.A = 4000
        # Коэффициент влияния факторов на кредитную ставку alpha
        self.alpha = 0.7  # 0.1-0.9
        # Коэффициент эластичности по кредиту на закупку товара betta
        self.betta = 0.35 # 0.35-0.5 не включая 0.5
        # Степень зависимости наценки от затрат на единицу складской мощности gamma
        self.gamma = 3
        # Парамерт корреляции кредитного долга на процентную ставку C
        self.C = 350000  # 100000-500000
        # self.D = 300 # от 300 - 900
        # Коэффициент себестоимости хранения товаров на складе D
        self.D = 50
        # w-размер налоговой ставки на прибыль
        self.w = 0.2

    def display_info_(self):
        print("__________________________________________________")
        print("Значения параметров ВЕДОМОГО:")
        print("__________________________________________________")
        print(f"Коэффициет факторной производительности A = {self.A} ")
        print(f"Коэффициент эластичности по кредиту на закупку товара betta = {self.betta}")
        print(f"Степень привлекательности процентной ставки кредита для ИП alpha = {self.alpha}")
        print(f"Величина налоговой ставки на прибыль ИП = {self.w}")
        print(f"Коэффициент себестоимости хранения товаров на складе D = {self.D}")
        print(f"Парамерт, от которого зависит величина кредита C = {self.C}")
        print(f"Степень зависимости наценки от затрат на единицу складской мощности gamma = {self.gamma}", "\n")

    def fill_random_parameters(self):
        self.A = random.randint(800, 5000)
        self.alpha = random.uniform(0.1, 0.9)
        self.betta = random.uniform(0.3, 0.4)
        # self.gamma = random.random()
        self.gamma = 3
        self.w = 0.2
        self.C = random.randrange(30000, 400000)
        self.D = random.randrange(300, 900)

    # кол-во товаров функция - Q(KR)
    def compute_quantity_goods(self, pr):
        C = self.C
        betta = self.betta
        alpha = self.alpha
        return (C / ((1 + pr) ** alpha)) ** betta

    # функция прибыли ИП - B(m, KR)
    def profite_sale_goods(self, pr, markup):
        quantity_goods = self.compute_quantity_goods(pr)
        return (1 - self.w) * markup * self.A * quantity_goods
        # return markup * self.A * quantity_goods

    # функция кредита - S(pr, KR)
    def sum_credit_bank(self, pr, markup):
        alpha = self.alpha
        return (1 + pr) * (self.C / ((1 + pr) ** alpha))

    # функция затрат на хранение товара - G(m, KR)
    def storage_costs(self, pr, markup):
        quantity_goods = self.compute_quantity_goods(pr)
        # return self.D * (markup ** self.gamma) * quantity_goods
        return self.D * (markup ** self.gamma) * quantity_goods

    def objective_function(self, pr, markup):
        """
        Целевая функция предпринимателя
        :param markup: наценка
        :param pr: процентная ставка по кредиту
        :return: float
        """
        income = self.profite_sale_goods(pr, markup)
        debt_bank = self.sum_credit_bank(pr, markup)
        storage_costs = self.storage_costs(pr, markup)

        return income - debt_bank - storage_costs

    def get_entrepreneur_subfunctions(self, stack_point_pr, stack_point_m):
        income = self.profite_sale_goods(stack_point_pr, stack_point_m)
        debt_bank = self.sum_credit_bank(stack_point_pr, stack_point_m)
        storage_costs = self.storage_costs(stack_point_pr, stack_point_m)
        quantity_goods = self.compute_quantity_goods(stack_point_pr)
        print(f"ЗНАЧЕНИЯ ФУНКЦИОНАЛОВ ВЕДОМОГО: ")
        print("__________________________________________________")
        print(f"Прибыль ИП = {income}")
        print(f"Кредит ИП = {debt_bank}")
        print(f"Затраты ИП на хранение товара = {storage_costs}")
        print(f"Количество закупаемого товара ИП = {quantity_goods}")
        print("__________________________________________________")
