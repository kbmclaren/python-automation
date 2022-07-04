"""PDF table extractor

This script allows the user to scrape tables from PDF documents (text based, not scans).

This script requires tk, ghostscript, and camelot-py to be installed in the Python env 
you are running this script in.

NB: https://winmundo.com/macos-python-ghostscript-runtimeerror-can-not-find-ghostscript-library-libgs/
Turns out, brew install ghostscript, i.e. "installing the C part of ghostscript" took care of the runtime error I was having.
This idea is supported by the library check found in the Camelot documentation and the libgs check finally returning something 
after the Brew install. See https://buildmedia.readthedocs.org/media/pdf/camelot-py/latest/camelot-py.pdf.


This file can also be imported as a module and contains the following functions:

    * extractPDF - Read targetPDF and return extracted TableList 

    * exportTableList - Export the list of tables to the .csv file format inside a .zip compression file

    * exportTargetTable - Export a target table from the given TableList to a .csv file.

file: extractPDFTable.py
Author: Caleb M. McLaren
email: kbmclaren@gmail.com
date: July, 2022
"""
import camelot

def exportTargetTable( tableList: camelot.core.TableList, targetTable: int):
    """Export a target table from the given TableList to a .csv file."""
    tableList[ targetTable ].to_csv( 'tableTempName.csv' )

def exportTableList( tableList: camelot.core.TableList ):
    """Export the TableList to the .csv file format inside a .zip compression file"""
    tableList.export( 'tableList.csv', f='csv', compress=True )

def extractPDF( targetPDF: str ) -> list:
    """Read targetPDF and return extracted TableList"""
    pdfTableList = camelot.read_pdf( targetPDF, pages='1', )
    return pdfTableList

def main( targetPDF: str ):
    targetTableList = extractPDF( targetPDF )   #good
    #print( targetTableList[0] )                # not what I expected
    exportTableList( targetTableList )          #good
    exportTargetTable( targetTableList, 0 )     #good

if __name__ == "__main__":
    import sys
    main( sys.argv[1] )