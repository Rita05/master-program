from beautifultable import BeautifulTable
import matplotlib.pyplot as plt
import numpy as np

from algorithm_stackelberg_equilibrium import find_stackelberg_equilibrium
from commerical_bank import CommercialBank
from enterpreneur import Entrepreneur

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
    # # step = (500000 - 200000) / 10
    # for credit_C in np.arange(200000, 530000, 30000):
    #     entrepreneur.C = credit_C
    #     print("__________________________________________________")
    #     print(f"Парамерт корреляции кредитного \n долга на процентную ставку C = {credit_C} ")
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
    # plt.plot(x, y1, color="c", linewidth = 3)
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
    #     print(f"Степень привлекательности процентной ставки кредита alpha= {alpha} ")
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
    # for A_factor in range(3000, 6300, 300):
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
    # plt.xlabel('A')
    # plt.ylabel('Jип')
    # plt.plot(x, y, color="c", linewidth=3)
    # plt.show()

    # table = BeautifulTable()
    # x = []
    # y = []
    # table.column_headers = ['D', 'Fbank', 'Fbusinessman', 'pr', 'm', 'sys_cons']
    # #  step = (270 - 50) / 10
    # for D_factor in range(50, 270, 20):
    # # for D_factor in np.arange(50, 270, step):
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
    # table.column_headers = ['gamma', 'Fbank', 'Fbusinessman', 'pr', 'm', 'sys_cons']
    # # step = (5.45 - 0.5) / 10
    # for gamma_degree in np.arange(0.5, 5.45, 0.45):
    # # for gamma_degree in np.arange(0.5, 5.45, step):
    #     entrepreneur.gamma = gamma_degree
    #     print("__________________________________________________")
    #     print(f"Степень зависимости наценки от затрат на хранение товара gamma  = {gamma_degree} ")
    #     print("__________________________________________________")
    #     J_bank, J_businessman, equilibrium_point, sys_sogl = find_stackelberg_equilibrium(bank, entrepreneur)
    #     bank.get_bank_subfunctions(equilibrium_point.pr, equilibrium_point.m, entrepreneur)
    #     entrepreneur.get_entrepreneur_subfunctions(equilibrium_point.pr, equilibrium_point.m)
    #     x.append(gamma_degree)
    #     y.append(J_businessman)
    #     table.append_row([gamma_degree, J_bank, J_businessman, equilibrium_point.pr, equilibrium_point.m, sys_sogl])
    # print('\n', table)
    # plt.title('Зависимость прибыли ИП от параметра gamma')
    # plt.xlabel('gamma')
    # plt.ylabel('Jип')
    # plt.plot(x, y, color="c", linewidth=3)
    # plt.show()

    # table = BeautifulTable()
    # x = []
    # y = []
    # table.column_headers = ['betta', 'Fbank', 'Fbusinessman', 'pr', 'm', 'sys_cons']
    # for betta_degree in np.arange(0.3, 0.51, 0.02):
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
    # # step = (100000 - 21000) / 10
    # for L_factor in np.arange(21000, 107900, 7900):
    # # for L_factor in np.arange(21000, 100000, step):
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
    # table.column_headers = ['delta', 'Fbank', 'Fbusinessman', 'pr', 'm', 'sys_cons']
    # # step = (3.3 - 0.1) / 10
    # # for delta_degree in np.arange(0.1, 3.3, 0.3):
    # for delta_degree in np.arange(0.1, 3.3, step):
    #     bank.delta = delta_degree
    #     print("__________________________________________________")
    #     print(f"Степень влияния процентной ставки по кредиту на рекламные расходы delta = {delta_degree} ")
    #     print("__________________________________________________")
    #     J_bank, J_businessman, equilibrium_point, sys_sogl = find_stackelberg_equilibrium(bank, entrepreneur)
    #     bank.get_bank_subfunctions(equilibrium_point.pr, equilibrium_point.m, entrepreneur)
    #     entrepreneur.get_entrepreneur_subfunctions(equilibrium_point.pr, equilibrium_point.m)
    #     x.append(delta_degree)
    #     y.append(J_bank)
    #     table.append_row([delta_degree, J_bank, J_businessman, equilibrium_point.pr, equilibrium_point.m, sys_sogl])
    # print('\n', table)
    # plt.title('Зависимость прибыли Банка от параметра delta')
    # plt.xlabel('delta')
    # plt.ylabel('Jкб')
    # plt.plot(x, y, color="cornflowerblue", linewidth=3)
    # plt.show()

    # table = BeautifulTable()
    # x = []
    # y = []
    # table.column_headers = ['L', 'Fbank', 'Fbusinessman', 'pr', 'm', 'sys_cons']
    # for L_factor in range(10000, 109000, 9000):
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
    #     print(f"Cтавка риска заемщика k  = {k_factor} ")
    #     print("__________________________________________________")
    #     J_bank, J_businessman, equilibrium_point, sys_sogl = find_stackelberg_equilibrium(bank, entrepreneur)
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
    # for D_factor in range(200, 600, 40):
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
    # for betta_degree in np.arange(0.3, 0.51, 0.02):
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

    # table = BeautifulTable()
    # x = []
    # y = []
    # table.column_headers = ['delta', 'Fbank', 'Fbusinessman', 'pr', 'm', 'sys_cons']
    # # step = (3.3 - 0.1) / 10
    # for delta_degree in np.arange(0.1, 3.3, 0.3):
    # # for delta_degree in np.arange(0.1, 3.3, step):
    #     bank.delta = delta_degree
    #     print("__________________________________________________")
    #     print(f"Степень влияния процентной ставки по кредиту на рекламные расходы delta = {delta_degree} ")
    #     print("__________________________________________________")
    #     J_bank, J_businessman, equilibrium_point, sys_sogl = find_stackelberg_equilibrium(bank, entrepreneur)
    #     bank.get_bank_subfunctions(equilibrium_point.pr, equilibrium_point.m, entrepreneur)
    #     entrepreneur.get_entrepreneur_subfunctions(equilibrium_point.pr, equilibrium_point.m)
    #     x.append(delta_degree)
    #     y.append(equilibrium_point.pr)
    #     table.append_row([delta_degree, J_bank, J_businessman, equilibrium_point.pr, equilibrium_point.m, sys_sogl])
    # print('\n', table)
    # plt.title('Зависимость ставки Банка от параметра delta')
    # plt.xlabel('delta')
    # plt.ylabel('pr')
    # plt.plot(x, y, color="cornflowerblue", linewidth=3)
    # plt.show()
