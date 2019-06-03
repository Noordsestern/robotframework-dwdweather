from dwdweather import DwdWeather
from robot.api import logger
from robot.api.deco import keyword


class DwdWeatherLibrary(object):
    ROBOT_LIBRARY_VERSION = '0.0.1'
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    _DW_CLIENT: DwdWeather

    def __init__(self):
        _DW_CLIENT = DwdWeather()
        logger.debug('Intialized DwdWeather')

    @keyword(name="Get all stations")
    def get_all_stations(self):
        return self._DW_CLIENT.stations()
