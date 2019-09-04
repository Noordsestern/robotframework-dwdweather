[![Build Status](https://travis-ci.org/Noordsestern/robotframework-dwdweather.svg?branch=staging)](https://travis-ci.org/Noordsestern/robotframework-dwdweather)

# Summary
[Robot Framework](https://github.com/robotframework/robotframework) library for public weather service in Germany ([DWD](https://www.dwd.de/DE/leistungen/opendata/faqs_opendata.html)). Wraps original python implementation from [dwdweather2](https://github.com/hiveeyes/dwdweather2).

# Installation
## robotframework-dwdweather
You can install python projects directly from git with pip by calling `pip install git+https://github.com/Noordsestern/robotframework-dwdweather.git@<branch_name>` where you have to set `<branch_name>` with one of the following:
- `master`: latest stable version
- `staging` : edge version

# Usage

You can simply use keywords from this library by adding `DwdWeatherLibrary` to your suite:
```robot
*** Settings ***
Library    DwdWeatherLibrary
```
Refer to [keyword documentation](https://noordsestern.github.io/robotframework-dwdweather/) for details.


## Examples
You can find example testcase in `tests/robot`

# Dependencies

DwdWeatherLibrary requires an internet connection in order to collect stations, weather data and address from web services.
Internally it uses:
- [dwdweather2](https://github.com/hiveeyes/dwdweather2) : For accessing data from dwd weather service
- [geopy](https://github.com/geopy/geopy) : For handling locations