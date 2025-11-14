#!/usr/bin/env python

import argparse
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument("--szInputMerylHistogram", required = True )
parser.add_argument("--szOutputJellyfishHistogram", required = True )
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
    
nSumOverTenThousand = 0

with open( args.szInputMerylHistogram, "r" ) as fInput, open( args.szOutputJellyfishHistogram, "w" ) as fOutput:
    while True:
        szLine = fInput.readline()
        if ( szLine == "" ):
            break
        szLine = szLine.rstrip()
        if ( szLine == "" ):
            continue

        aWords = szLine.split()
        # looks like:
        # 
        nX = int( aWords[0] )
        if ( nX >= 10001 ):
            nY = int( aWords[1] )
            nSumOverTenThousand += nY
        else:
            szNewLine = " ".join( aWords )
            fOutput.write( szNewLine + "\n" )

    # while True:
    fOutput.write( f"10001 {nSumOverTenThousand}\n" )
    
            
            

           
