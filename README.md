> This project is not finished, yet.

# Summary
[Robot Framework](https://github.com/robotframework/robotframework) library for public weather service in Germany. Wraps original python implementation from [dwdweather2](https://github.com/hiveeyes/dwdweather2).

# Installation
## dwdweather2 fork
Clone our fork from [github](https://github.com/noordsestern/dwdweather2) switch to branch `feature/python3` and run `pip install .` in the projects directory.

You will need this fork in order to run with python3. Once done migrating to python3 we intend to merge this feature branch with the main project on [hiveeyes](https://github.com/hiveeyes/dwdweather2).

## robotframework-dwdweather
Clone this repository and run `pip install .`

# Usage
You can find example testcase in `tests/robot`