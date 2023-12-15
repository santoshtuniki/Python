#### Virtual Environment

##### While the *virtual environment* is active, any packages installed via pip will be specific to this environment.

##### Always launch virtual environment, after closing project & re-starting it.

##### Install package:

    sudo apt install python3-venv

##### Create command:

    python3 -m venv <directory>

        Ex: python3 -m venv venv

##### Activate command:

    source venv/bin/activate

##### Verify if activated: (In terminal, we find..)

    (venv) __path__

##### Install packages in venv:

    pip install package_name

##### DeActivate command:

    deactivate

##### Delete venv command:

    rm -rf venv

##### If we see list of packages available initially in venv:

    pip list

        Package    Version
        ---------- -------
        pip        22.0.2
        setuptools 59.6.0

##### To know the information of a package:

    pip show <package_name>

##### To let others know the packages we used in virtual environment, we have *requirements.txt* file.

    pip freeze > requirements.txt

##### Install "python-dotenv" globally outside venv to resolve error:

    Import "dotenv" could not be resolved Pylance

##### WEATHER:

    https://openweathermap.org/ > name > My API Keys

    https://openweathermap.org/api > Current Weather Data > API doc


##### python-dotenv to access data in .env file

##### use os.getenv(KEY) to write data of .env file