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
        """
         Gets station with a certain name.

         | *Result*                 | * Keyword *                   |                               |                       |
         | ${station}               | *Get station*                 | _Aachen_                      |                       |
         |                          | *Should Be Equal As String*   | _Aachen_                      | _${station}[0][name]_ |
         |                          |                               |                               |                       |
         | ${not_existing_station}  | *Get station*                 | _Mordor_                      |                       |
         |                          | *Should Be Empty*             | _${not_existing_station}_     |                       |
        """
        all_stations = self.get_all_stations()
        stations = [s.copy() for s in all_stations if station_name == s['name']]
        if 2 <= len(stations):
            logger.warn(f'Got more than one station for ${station_name}:\t${stations}')
        if stations:
            return stations[0]
        return []

    @keyword(name="Get station closest to address")
    def get_nearest_station(self, address : str):
        """
         Gets station in Germany closest to any given address.

         | *Result*     | *Keyword*                       |                                   |                       |
         | ${station}   | *Get station closest to address*  | _Aachen_                          |                       |
         |              | *Should Be Equal As String*       | _Nordrhein_Westfalen_             | _${station}[state]_ |
         |              |                                   |                                   |                       |
         | ${station}   | *Get station closest to address*  | _Am Anger 33, 33332 Gütersloh_    |                       |
         |              | *Should Be Equal As String*       | _Nordrhein_Westfalen_             | _${station}[state]_ |
         |              |                                   |                                   |                       |
         | ${station}   | *Get station closest to address*  | _64807 Dieburg_                   |                       |
         |              | *Should Be Equal As String*       | _Hessen_                          | _${station}[state]_ |
         |              |                                   |                                   |                       |
         | ${station}   | *Get station closest to address*  | _Stockholm_                       |                       |
         |              | *Should Be Equal As String*       | _Mecklenburg-Vorpommern_          | _${station}[state]_ |
         |              | *Log*                             | _Closest station in Germany is very far away from 'Stockholm'._ | _WARN_ |

         """
        location = self._GEOLOCATOR.geocode(address)
        closest_station = self._DW_CLIENT.nearest_station(location.longitude, location.latitude)
        return closest_station
