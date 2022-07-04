# Automation of Table Extraction

## extraction-env

    To create python env, 
    * On Unix or MacOS, run:
        python3 -m venv extraction-env
        pip install pandas
        pip install lxml
        
        ### The following are required for extractPDFTable.py
        pip install tk
        pip install ghostscript
        pip install camelot-py <- depends on tk & ghostscript
            For Linux/Unix user: "brew install ghostscripts" also to ensure the C part of ghostscript (libgs) is available. 
        

    To activate/deactivate python environment,
    * On Unix or MacOS, run: 
        source extraction-env/bin/activate
        &&
        deactivate

## Modules

    * extractTable.py: grab html tables from url and print out the first one found
        usage: python3 extractTable.py [<targetURL>]

    * extractCSV.py: read a .csv file from a URL with Pandas
        usage: python3 extractCSV.py [<targetURL>] -- targetURL should be exact URL for .csv file.

    * extractPDFTable.py: extract tables from target PDF via Camelot, export TableList to .csv compressed into a .zip, then extract first table to standalone .csv file with temporary name.
        usage: python3 extractPDFTable.py [<targetPDF>]

## requirements.txt

    Generated via "pip freeze > requirements.txt"
    User can install the venv requirements listed here via:
       "python -m pip install -r requirements.txt" 