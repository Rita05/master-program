import sys

import numpy as np
from beautifultable import BeautifulTable
import matplotlib.pyplot as plt

from model.analytics.commerical_bank import CommercialBank
from model.analytics.enterpreneur import Entrepreneur
from model.point import Point

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
        sysConsistency = max_stack_pr / J_bank_max
    else:
        sysConsistency = abs(max_stack_pr / J_bank_max)

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