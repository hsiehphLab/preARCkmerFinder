#!/usr/bin/env python

import argparse
import subprocess
import glob
import re
import os

parser = argparse.ArgumentParser()
parser.add_argument("--szDirectoryOfDatabases", required = True )
args = parser.parse_args()

def bash_command( szCommand ):
    print( f"about to execute: {szCommand}" )
    subprocess.call( szCommand, shell = True )

def bIntervalsIntersect( nLeftA, nRightA, nLeftB, nRightB ):
    if ( ( nLeftA <= nRightB ) and  ( nLeftB <= nRightA ) ):
        return True
    else:
        return False

def bIntersect( nALeft, nARight, nBLeft, nBRight ):

   nIntersectLeft = max( nALeft, nBLeft )
   nIntersectRight = min( nARight, nBRight )

   if (nIntersectLeft <= nIntersectRight):
     bOK = True
   else:
     bOK = False

   if ( bOK ):
       return( True, nIntersectLeft, nIntersectRight )
   else:
       return( False, -666, -666 )
    

aDatabases = glob.glob( args.szDirectoryOfDatabases + "/*.no_low_freq_kmers.meryl" )
print( "will process: ", aDatabases )

for szDatabase in aDatabases:
    szGenomescopeFile = re.sub( r".no_low_freq_kmers.meryl", "_genomescope", szDatabase ) + "/summary.txt"
    szErrorCutoff = ""
    with open( szGenomescopeFile, "r" ) as fSummary:
        for szLine in fSummary.readlines():
            if ( szLine.startswith( "Errror Kmers Cutoff" ) ):
                aWords = szLine.split()
                # looks like:
                # Error Kmers Cutoff            8
                # 0      1     2                3
                szErrorCutoff = aWords[3]
                break
    #with open( szGenomescopeFile, "r" ) as fSummary:

    # case in which genomescope didn't generate an error kmer cutoff
    if ( szErrorCutoff == "" ):
        continue
    
    szReplacementString = ".no_" + szErrorCutoff + "_freq_kmers.meryl"
    szNewDatabaseName = re.sub( r".no_low_freq_kmers.meryl", szReplacementString, szDatabase )


    print( f"will rename {szDatabase} to {szNewDatabaseName} " )
    os.rename( szDatabase, szNewDatabaseName )

    
