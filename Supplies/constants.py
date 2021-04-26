from .models import Supply


class SupplyConstants:

    R_TYPE_TO_SUPPLIES_MAPPING = {
        'PAB': [Supply.PLASMA, Supply.BLOOD],
        'HBD': [Supply.HOSPITAL_BED, Supply.ICU_BED],
        'OXY': [Supply.OXYGEN],
        'FOD': [Supply.HOME_FOOD]
    }