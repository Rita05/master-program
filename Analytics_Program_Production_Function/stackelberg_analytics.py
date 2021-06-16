import sys
from point import Point
import numpy as np
from beautifultable import BeautifulTable
import matplotlib.pyplot as plt

from commerical_bank import CommercialBank
from enterpreneur import Entrepreneur

PR_MIN, PR_MAX, PR_STEP = 0.08, 0.17, 0.01
M_MIN, M_MAX, M_STEP = 1, 10, 1


def find_stackelberg_equilibrium(bank: CommercialBank, entrepreneur: Entrepreneur):
    max_stack_pr = -sys.maxsize
    point_max_pr = Point()
    # entrepreneur.display_info_()
    # bank.display_info_()
    for pr in np.linspace(PR_MIN, PR_MAX, 101, endpoint=True):
        max_stack_m = -sys.maxsize
        point_max_m = Point()

        # for m in np.linspace(M_MIN, M_MAX, 5001, endpoint=True):
        for m in np.linspace(M_MIN, M_MAX, 5001, endpoint=True):
            if entrepreneur.objective_function(pr, m) > max_stack_m:
                max_stack_m = entrepreneur.objective_function(pr, m)
                point_max_m = Point(pr, m)
                # print(f"New point_max_m {point_max_m.pr}, {point_max_m.m} ,"
                #       f" {entrepreneur.objective_function(pr, m)} ")

        if bank.object_function(point_max_m.pr, point_max_m.m, entrepreneur) > max_stack_pr:
            max_stack_pr = bank.object_function(point_max_m.pr, point_max_m.m, entrepreneur)
            point_max_pr = point_max_m
            # print(f"New point_max_pr {point_max_pr.pr}, {point_max_pr.m}, "
            #       f"{bank.object_function(point_max_m.pr, point_max_m.m, entrepreneur)} ")

    # print(f"Risk costs {max_risk_cost}")
    print(f"Jbank = {max_stack_pr}")
    print(f"Jentrepreneur = {max_stack_m}")
    print(f"Point Equilibrium = ( {point_max_pr.pr} , {point_max_pr.m} )")
    J_bank_max, point_max_bank = get_global_max_J_bank(bank, entrepreneur)
    if J_bank_max < 0:
        sysConsistency = abs(max_stack_pr / J_bank_max)
    else:
        sysConsistency = max_stack_pr / J_bank_max

    print("Коэффициент системной согласованности: ", sysConsistency)
    print("Точка глобального максимума:", point_max_bank)
    print("Point_max_bank=", point_max_bank, " J_max_bank=", J_bank_max)

    return max_stack_pr, max_stack_m, point_max_pr, max_stack_pr / J_bank_max


def get_global_max_J_bank(bank: CommercialBank, entrepreneur: Entrepreneur):
    point = []
    max_J_0 = -sys.maxsize
    for pr in np.linspace(PR_MIN, PR_MAX, 10, endpoint=True):
        for m in np.linspace(M_MIN, M_MAX, 10, endpoint=True):
            if bank.object_function(pr, m, entrepreneur) > max_J_0:
                max_J_0 = bank.object_function(pr, m, entrepreneur)
                point = [pr, m]

    return max_J_0, point


if __name__ == "__main__":
    bank = CommercialBank()
    # bank.fill_random_parameters()

    entrepreneur = Entrepreneur()
    # entrepreneur.fill_random_parameters()

    Jbank, Jip, point_equilibrium, sys_sogl = find_stackelberg_equilibrium(bank, entrepreneur)

    bank.display_info_()
    bank.get_bank_subfunctions(point_equilibrium.pr, point_equilibrium.m, entrepreneur)
    entrepreneur.display_info_()
    entrepreneur.get_entrepreneur_subfunctions(point_equilibrium.pr, point_equilibrium.m)

    #### ПАРАМЕТРЫ ЦЕЛЕВЫХ ФУНКЦИЙ ###########
    # table = BeautifulTable()
    # x = []
    # y1 = []
    # y2 = []
    # table.column_headers = ['С', 'Fbank', 'Fbusinessman', 'pr', 'm', 'sys_cons']
    # for credit_C in range(200000, 530000, 30000):
    #     entrepreneur.C = credit_C
    #     print("__________________________________________________")
    #     print(f"Парамерт, влияющий на размер основного долга ИП по кредиту C = {credit_C} ")
    #     print("__________________________________________________")
    #     J_bank, J_businessman, equilibrium_point, sys_sogl = find_stackelberg_equilibrium(bank, entrepreneur)
    #     bank.get_bank_subfunctions(equilibrium_point.pr, equilibrium_point.m, entrepreneur)
    #     entrepreneur.get_entrepreneur_subfunctions(equilibrium_point.pr, equilibrium_point.m)
    #     x.append(credit_C)
    #     y1.append(J_businessman)
    #     y2.append(J_bank)
    #     table.append_row([credit_C, J_bank, J_businessman, equilibrium_point.pr, equilibrium_point.m, sys_sogl])
    # print('\n', table)
    # plt.title('Зависимость прибыли ИП от параметра C')
    # plt.xlabel('С')
    # plt.ylabel('Jип')
    # plt.plot(x, y1, color="c", linewidth=3)
    # plt.show()
    # plt.title('Зависимость прибыли Банка от параметра C')
    # plt.xlabel('С')
    # plt.ylabel('Jкб')
    # plt.plot(x, y2, color="cornflowerblue", linewidth=3)
    # plt.show()

    # table = BeautifulTable()
    # x = []
    # y1 = []
    # y2 = []
    # table.column_headers = ['alpha', 'Fbank', 'Fbusinessman', 'pr', 'm', 'sys_cons']
    # for alpha in np.arange(0.1, 1, 0.1):
    #     entrepreneur.alpha = alpha
    #     print("__________________________________________________")
    #     print(f"Коэффициент эластичности по кредиту на закупку товара alpha = {alpha} ")
    #     print("__________________________________________________")
    #     J_bank, J_businessman, equilibrium_point, sys_sogl = find_stackelberg_equilibrium(bank, entrepreneur)
    #     bank.get_bank_subfunctions(equilibrium_point.pr, equilibrium_point.m, entrepreneur)
    #     entrepreneur.get_entrepreneur_subfunctions(equilibrium_point.pr, equilibrium_point.m)
    #     x.append(alpha)
    #     y1.append(J_businessman)
    #     y2.append(J_bank)
    #     table.append_row([alpha, J_bank, J_businessman, equilibrium_point.pr, equilibrium_point.m, sys_sogl])
    # print('\n', table)
    # 2 графика на 2 окне
    # plt.plot(x, y1,"c", x, y2, "cornflowerblue" , linewidth=3)
    # plt.show()
    #
    #2 графика в разных окнах
    # plt.title('Зависимость прибыли ИП от параметра alpha')
    # plt.xlabel('alpha')
    # plt.ylabel('Jип')
    # plt.plot(x, y1, color="c", linewidth=3)
    # plt.show()
    #
    # plt.title('Зависимость прибыли Банка от параметра alpha')
    # plt.xlabel('alpha')
    # plt.ylabel('Jкб')
    # plt.plot(x, y2, color="cornflowerblue", linewidth=3)
    # plt.show()

    # 2 графика в разных окнах на 1 линии (subplot)
    # plt.figure(figsize=(15, 8))
    # plt.subplot(2, 2, 1)
    # plt.title('Зависимость прибыли ИП от параметра alpha')
    # plt.xlabel('alpha')
    # plt.ylabel('Jип')
    # plt.plot(x, y1, "c", linewidth=3)
    # plt.subplot(2, 2, 2)
    # plt.title('Зависимость прибыли Банка от параметра alpha')
    # plt.xlabel('alpha')
    # plt.ylabel('Jкб')
    # plt.plot(x, y2, "cornflowerblue", linewidth=3)
    # plt.show()

    # table = BeautifulTable()
    # x = []
    # y = []
    # table.column_headers = ['A', 'Fbank', 'Fbusinessman', 'pr', 'm', 'sys_cons']
    # for A_factor in range(3200, 6280, 280):
    #     entrepreneur.A = A_factor
    #     print("__________________________________________________")
    #     print(f"Коэффициет факторной производительности A = {A_factor} ")
    #     print("__________________________________________________")
    #     J_bank, J_businessman, equilibrium_point, sys_sogl = find_stackelberg_equilibrium(bank, entrepreneur)
    #     bank.get_bank_subfunctions(equilibrium_point.pr, equilibrium_point.m, entrepreneur)
    #     entrepreneur.get_entrepreneur_subfunctions(equilibrium_point.pr, equilibrium_point.m)
    #     x.append(A_factor)
    #     y.append(J_businessman)
    #     table.append_row([A_factor, J_bank, J_businessman, equilibrium_point.pr, equilibrium_point.m, sys_sogl])
    # print('\n', table)
    # plt.title('Зависимость прибыли ИП от параметра A')
    # # plt.figure(figsize=(6, 6))
    # plt.xlabel('A')
    # plt.ylabel('Jип')
    # plt.plot(x, y, color="c", linewidth=3)
    # plt.show()

    # table = BeautifulTable()
    # x = []
    # y = []
    # table.column_headers = ['D', 'Fbank', 'Fbusinessman', 'pr', 'm', 'sys_cons']
    # for D_factor in range(200, 530, 30):
    #     entrepreneur.D = D_factor
    #     print("__________________________________________________")
    #     print(f"Коэффициент себестоимости хранения товаров на складе D  = {D_factor} ")
    #     print("__________________________________________________")
    #     J_bank, J_businessman, equilibrium_point, sys_sogl = find_stackelberg_equilibrium(bank, entrepreneur)
    #     bank.get_bank_subfunctions(equilibrium_point.pr, equilibrium_point.m, entrepreneur)
    #     entrepreneur.get_entrepreneur_subfunctions(equilibrium_point.pr, equilibrium_point.m)
    #     x.append(D_factor)
    #     y.append(J_businessman)
    #     table.append_row([D_factor, J_bank, J_businessman, equilibrium_point.pr, equilibrium_point.m, sys_sogl])
    # print('\n', table)
    # plt.title('Зависимость прибыли ИП от параметра D')
    # plt.xlabel('D')
    # plt.ylabel('Jип')
    # plt.plot(x, y, color="c", linewidth=3)
    # plt.show()

    # table = BeautifulTable()
    # x = []
    # y = []
    # table.column_headers = ['betta', 'Fbank', 'Fbusinessman', 'pr', 'm', 'sys_cons']
    # for betta_degree in np.arange(0.33, 0.517, 0.017):
    #     entrepreneur.betta = betta_degree
    #     print("__________________________________________________")
    #     print(f"Коэффициент эластичности по кредиту на закупку товара betta  = {betta_degree} ")
    #     print("__________________________________________________")
    #     J_bank, J_businessman, equilibrium_point, sys_sogl = find_stackelberg_equilibrium(bank, entrepreneur)
    #     bank.get_bank_subfunctions(equilibrium_point.pr, equilibrium_point.m, entrepreneur)
    #     entrepreneur.get_entrepreneur_subfunctions(equilibrium_point.pr, equilibrium_point.m)
    #     x.append(betta_degree)
    #     y.append(J_businessman)
    #     table.append_row([betta_degree, J_bank, J_businessman, equilibrium_point.pr, equilibrium_point.m, sys_sogl])
    # print('\n', table)
    # plt.title('Зависимость прибыли ИП от параметра betta')
    # plt.xlabel('betta')
    # plt.ylabel('Jип')
    # plt.plot(x, y, color="c", linewidth=3)
    # plt.show()

    # table = BeautifulTable()
    # x = []
    # y = []
    # table.column_headers = ['L', 'Fbank', 'Fbusinessman', 'pr', 'm', 'sys_cons']
    # for L_factor in np.arange(21000, 107900, 7900):
    #     bank.L = L_factor
    #     print("__________________________________________________")
    #     print(f"Коэффициент корректировки затрат на рекламу банка L = {L_factor} ")
    #     print("__________________________________________________")
    #     J_bank, J_businessman, equilibrium_point, sys_sogl = find_stackelberg_equilibrium(bank, entrepreneur)
    #     bank.get_bank_subfunctions(equilibrium_point.pr, equilibrium_point.m, entrepreneur)
    #     entrepreneur.get_entrepreneur_subfunctions(equilibrium_point.pr, equilibrium_point.m)
    #     x.append(L_factor)
    #     y.append(J_bank)
    #     table.append_row([L_factor, J_bank, J_businessman, equilibrium_point.pr, equilibrium_point.m, sys_sogl])
    # print('\n', table)
    # plt.title('Зависимость прибыли Банка от параметра L')
    # plt.xlabel('L')
    # plt.ylabel('Jкб')
    # plt.plot(x, y, color="cornflowerblue", linewidth=3)
    # plt.show()


    # table = BeautifulTable()
    # x = []
    # y = []
    # table.column_headers = ['L', 'Fbank', 'Fbusinessman', 'pr', 'm', 'sys_cons']
    # for L_factor in range(21000, 107900, 7900):
    #     bank.L = L_factor
    #     print("__________________________________________________")
    #     print(f"Коэффициент корректировки затрат на рекламу банка L = {L_factor}  ")
    #     print("__________________________________________________")
    #     J_bank, J_businessman, equilibrium_point, sys_sogl = find_stackelberg_equilibrium(bank, entrepreneur)
    #     bank.get_bank_subfunctions(equilibrium_point.pr, equilibrium_point.m, entrepreneur)
    #     entrepreneur.get_entrepreneur_subfunctions(equilibrium_point.pr, equilibrium_point.m)
    #     x.append(L_factor)
    #     y.append(equilibrium_point.pr)
    #     table.append_row([L_factor, J_bank, J_businessman, equilibrium_point.pr, equilibrium_point.m, sys_sogl])
    # print('\n', table)
    # plt.title('Зависимость ставки по кредиту Банка от параметра L')
    # plt.xlabel('L')
    # plt.ylabel('pr')
    # plt.plot(x, y, color="cornflowerblue", linewidth=3)
    # plt.show()


    # table = BeautifulTable()
    # x = []
    # y = []
    # table.column_headers = ['PExp', 'Fbank', 'Fbusinessman', 'pr', 'm', 'sys_cons']
    # for PExp in range(10000, 109000, 9000):
    #     bank.PExp = PExp
    #     print("__________________________________________________")
    #     print(f"Другие постоянные расходы Банка PExp = {PExp} ")
    #     print("__________________________________________________")
    #     J_bank, J_businessman, equilibrium_point, sys_sogl = find_stackelberg_equilibrium(bank, entrepreneur)
    #     bank.get_bank_subfunctions(equilibrium_point.pr, equilibrium_point.m, entrepreneur)
    #     entrepreneur.get_entrepreneur_subfunctions(equilibrium_point.pr, equilibrium_point.m)
    #     x.append(PExp)
    #     y.append(J_bank)
    #     table.append_row([PExp, J_bank, J_businessman, equilibrium_point.pr, equilibrium_point.m, sys_sogl])
    # print('\n', table)
    # plt.title('Зависимость прибыли Банка от параметра PExp')
    # plt.xlabel('PExp')
    # plt.ylabel('Jкб')
    # plt.plot(x, y, color="cornflowerblue", linewidth=3)
    # plt.show()

    # table = BeautifulTable()
    # x = []
    # y = []
    # table.column_headers = ['k', 'Fbank', 'Fbusinessman', 'pr', 'm', 'sys_cons']
    # for k_factor in np.arange(0.1, 0.408, 0.028):
    #     bank.k = k_factor
    #     print("__________________________________________________")
    #     print(f"Коэффициент кредитоспособности ИП k  = {k_factor} ")
    #     print("__________________________________________________")
    #     J_bank, J_businessman, equilibrium_point, sys_sogl = find_stackelberg_equilibrium(bank, entrepreneur)
    #     bank.get_bank_subfunctions(equilibrium_point.pr, equilibrium_point.m, entrepreneur)
    #     entrepreneur.get_entrepreneur_subfunctions(equilibrium_point.pr, equilibrium_point.m)
    #     x.append(k_factor)
    #     y.append(J_bank)
    #     table.append_row([k_factor, J_bank, J_businessman, equilibrium_point.pr, equilibrium_point.m, sys_sogl])
    # print('\n', table)
    # plt.title('Зависимость прибыли Банка от параметра k')
    # plt.xlabel('k')
    # plt.ylabel('Jкб')
    # plt.plot(x, y, color="cornflowerblue", linewidth=3)
    # plt.show()

    # table = BeautifulTable()
    # x = []
    # y = []
    # table.column_headers = ['D', 'Fbank', 'Fbusinessman', 'pr', 'm', 'sys_cons']
    # for D_factor in range(300, 960, 60):
    #     entrepreneur.D = D_factor
    #     print("__________________________________________________")
    #     print(f"Коэффициент себестоимости хранения товаров на складе D = {D_factor}  ")
    #     print("__________________________________________________")
    #     J_bank, J_businessman, equilibrium_point, sys_sogl = find_stackelberg_equilibrium(bank, entrepreneur)
    #     bank.get_bank_subfunctions(equilibrium_point.pr, equilibrium_point.m, entrepreneur)
    #     entrepreneur.get_entrepreneur_subfunctions(equilibrium_point.pr, equilibrium_point.m)
    #     x.append(D_factor)
    #     y.append(equilibrium_point.m)
    #     table.append_row([D_factor, J_bank, J_businessman, equilibrium_point.pr, equilibrium_point.m, sys_sogl])
    # print('\n', table)
    # plt.title('Зависимость наценки ИП от параметра D')
    # plt.xlabel('D')
    # plt.ylabel('m')
    # plt.plot(x, y, color="c", linewidth=3)
    # plt.show()

    # table = BeautifulTable()
    # x = []
    # y = []
    # table.column_headers = ['betta', 'Fbank', 'Fbusinessman', 'pr', 'm', 'sys_cons']
    # for betta_degree in np.arange(0.33, 0.517, 0.017):
    #     entrepreneur.betta = betta_degree
    #     print("__________________________________________________")
    #     print(f"Коэффициент эластичности по кредиту на закупку товара betta  = {betta_degree} ")
    #     print("__________________________________________________")
    #     J_bank, J_businessman, equilibrium_point, sys_sogl = find_stackelberg_equilibrium(bank, entrepreneur)
    #     bank.get_bank_subfunctions(equilibrium_point.pr, equilibrium_point.m, entrepreneur)
    #     entrepreneur.get_entrepreneur_subfunctions(equilibrium_point.pr, equilibrium_point.m)
    #     x.append(betta_degree)
    #     y.append(equilibrium_point.m)
    #     table.append_row([betta_degree, J_bank, J_businessman, equilibrium_point.pr, equilibrium_point.m, sys_sogl])
    # print('\n', table)
    # plt.title('Зависимость наценки ИП от параметра betta')
    # plt.xlabel('betta')
    # plt.ylabel('m')
    # plt.plot(x, y, color="c", linewidth=3)
    # plt.show()