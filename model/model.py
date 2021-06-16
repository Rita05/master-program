from numpy import arange

from model.config_imitation import ConfigImitation
from model.imitation.imitation import imitation
from model.analytics.analytics import analytics
from model.model_output import ModelOutput
from model.config_analytics import ConfigAnalytics
from typing import List, Callable


class Model:

    def compute_analytics(self, config: ConfigAnalytics) -> ModelOutput:
        if not config.has_range():
            return analytics(config)
        outputs = Model.__compute_range(config, analytics)
        return Model.__combine(config, outputs)

    def compute_imitation(self, config: ConfigImitation) -> ModelOutput:
        if not config.has_range():
            return imitation(config)
        outputs = Model.__compute_range(config, imitation)
        return Model.__combine(config, outputs)

    @staticmethod
    def __compute_range(config: ConfigAnalytics, method: Callable[[ConfigAnalytics], ModelOutput]) -> List[ModelOutput]:
        outputs: List[ModelOutput] = []
        for i in arange(config.range_from, config.range_to, config.range_step):
            updated_config = config.copy_put(config.range_property, i)
            outputs.append(method(updated_config))
        return outputs

    @staticmethod
    def __combine(config: ConfigAnalytics, outputs: List[ModelOutput]) -> ModelOutput:
        output = outputs[-1]
        output.business_points = []
        output.bank_points = []
        for res in outputs:
            config_prop_value = getattr(res.config, config.range_property)
            output.business_points.append([config_prop_value, res.j_business])
            output.bank_points.append([config_prop_value, res.j_bank])
        return output