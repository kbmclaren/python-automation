"""Read a .csv from a URL with Pandas

file: extractCSV.py
Author: Caleb M. McLaren
email: kbmclaren@gmail.com
date: June, 2022
"""

import pandas as pd

def extractCSV( targetURL: str ) -> pd.DataFrame:
    """Reads .csv file to Panda DataFrame

    Parameters
    ----------
    targetURL : str
        The URL address/file system of
    
    """
    targetDataFrame = pd.read_csv( targetURL )
    return targetDataFrame; 

def bigMain( targetURL: str):
    """Gets all .csv files found at URL link.

    Parameters
    ----------
    targetURL : str
        The URL address of multiple target .csv files

    Returns
    -------
    None
        bigMain()  
        but the return of main() is Python's special object for nothing "None".
    """
    #TODO: would be a lot of work if pandas/html.py is any indication. Other modules like BeautifulSoup, 
    # and urlparse look promising
    # ToRead: https://stackoverflow.com/questions/39033674/download-all-csv-files-from-url
    

def main( targetURL: str ):
    """Gets and prints target .csv file from URL link (or local file path).

    Parameters
    ----------
    targetURL : str
        The URL address of the single target .csv file

    Returns
    -------
    None
        main() prints out the first & last 5 rows of the target .csv, 
        but the return of main() is Python's special object for nothing "None".
    """
    targetDataFrame = extractCSV( targetURL )
    with pd.option_context('display.max_rows', 10,'display.max_columns', None,'display.precision', 3,):
        print( targetDataFrame )

if __name__ == "__main__":
    import sys
    main( sys.argv[1] )