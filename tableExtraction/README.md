# Automation of Table Extraction

## extraction-env

    To create python env, 
    * On Unix or MacOS, run:
        python3 -m venv extraction-env
        pip install pandas
        pip install lxml

    To activate python environment,
    * On Unix or MacOS, run: 
        source extraction-env/bin/activate

## Modules

* extractTable.py: grab html tables from url and print out the first one found
    usage: python3 extractTable.py [<targetURL>]

