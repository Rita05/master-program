from model.config_imitation import ConfigImitation
from model.imitation.algorithm_stackelberg_equilibrium import find_stackelberg_equilibrium
from model.imitation.commerical_bank import CommercialBank
from model.imitation.enterpreneur import Entrepreneur
from model.model_output import ModelOutput


def imitation(config: ConfigImitation) -> ModelOutput:
    bank = CommercialBank(config)
    entrepreneur = Entrepreneur(config)

    Jbank, Jip, point_equilibrium, sys_sogl = find_stackelberg_equilibrium(bank, entrepreneur)

    bank.display_info_()
    bank.get_bank_subfunctions(point_equilibrium.pr, point_equilibrium.m, entrepreneur)
    entrepreneur.display_info_()
    entrepreneur.get_entrepreneur_subfunctions(point_equilibrium.pr, point_equilibrium.m)

    return ModelOutput(point_equilibrium.pr, point_equilibrium.m, Jbank, Jip, [[0, 0]], [[0, 0]], config)