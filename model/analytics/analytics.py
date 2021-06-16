from model.analytics.commerical_bank import CommercialBank
from model.analytics.enterpreneur import Entrepreneur
from model.analytics.stackelberg_analytics import find_stackelberg_equilibrium
from model.config_imitation import ConfigImitation
from model.model_output import ModelOutput


def analytics(config: ConfigImitation) -> ModelOutput:
    bank = CommercialBank(config)
    # bank.fill_random_parameters()

    entrepreneur = Entrepreneur(config)
    # entrepreneur.fill_random_parameters()

    Jbank, Jip, point_equilibrium, sys_sogl = find_stackelberg_equilibrium(bank, entrepreneur)

    bank.display_info_()
    bank.get_bank_subfunctions(point_equilibrium.pr, point_equilibrium.m, entrepreneur)
    entrepreneur.display_info_()
    entrepreneur.get_entrepreneur_subfunctions(point_equilibrium.pr, point_equilibrium.m)

    return ModelOutput(point_equilibrium.pr, point_equilibrium.m, Jbank, Jip, [[0, 0]], [[0, 0]], config)