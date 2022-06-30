""" HTML Table(s) Extraction to Python list of Panda DataFrame(s)

This script prints out the first HTML table found on the url provided by the user.

This script accepts only one URL address per call. 

This script requires pandas and lxml be installed within the Python environment you are
runnint this script in. 

This file can also be imported as a module and contains the following functions.

    * extractTable -- returns list of Panda DataFrames representing HTML tables
    * main -- the main function of the script, calls extractTable and prints first table found

The expected usage of this script is as follows: 
    python3 extractTable.py [<targetURL>]

file: extractTable.py
Author: Caleb M. McLaren
email: kbmclaren@gmail.com
date: June, 2022
"""

import pandas as pd

def extractTable( targetURL:str ) -> list:
    """Get HTML tables and returns Python list of Panda Dataframes representing the same HTML tables.

    Parameters
    ----------
    targetURL : str
        Web address provided by the user
    
    Returns
    -------
    list
        list of Panda Dataframes representing the HTML tables found
    """
    
    targetList = []
    targetList = pd.read_html( targetURL )

    return targetList; 


def main( targetURL: str ):
    tableList = extractTable( targetURL )
    print( tableList[0] )

if __name__ == "__main__":
    import sys
    main( sys.argv[1] )
