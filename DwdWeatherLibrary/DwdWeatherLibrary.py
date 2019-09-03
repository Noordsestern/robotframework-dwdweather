from dwdweather import DwdWeather
from robot.api import logger
from robot.api.deco import keyword
from geopy.geocoders import Nominatim


class DwdWeatherLibrary(object):
    ROBOT_LIBRARY_VERSION = '0.0.1'
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    _DW_CLIENT: DwdWeather
    _GEOLOCATOR = Nominatim(user_agent="robotframework-dwdweather")

    def __init__(self):
        self._DW_CLIENT = DwdWeather('hourly')
        logger.debug('Intialized DwdWeather')

    @keyword(name="Get all stations")
    def get_all_stations(self):
        """
        Returns all available stations as dictionairy
        """
        return self._DW_CLIENT.stations()

    @keyword(name="Get station")
    def get_station(self, station_name : str):
        all_stations = self.get_all_stations()
        stations = [s.copy() for s in all_stations if station_name == s['name']]
        if 2 <= len(stations):
            logger.warn(f'Got more than one station for ${station_name}:\t${stations}')
        return stations

    @keyword(name="Get station closest to address")
    def get_nearest_station(self, address : str):
        location = self._GEOLOCATOR.geocode(address)
        closest_station = self._DW_CLIENT.nearest_station(location.longitude, location.latitude)
        return closest_station
