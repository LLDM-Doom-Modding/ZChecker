#
# (c) Morthimer McMare  a.k.a. JSO_x, 2023
#
# Base file:
#   https://github.com/DRRP-Team/DRRP/blob/master/tools/updateOldLocalization.py
#

import csv
import sys


# Constants:

const_DIR = "./"

#const_LocalizationFileTypes = [ ".core", ".tips" ]
const_LocalizationFileTypes = [ "" ]

const_InputFile = "LANGUAGE.gzdoom400"
const_InputFilesPostfix = [ i + ".csv" for i in const_LocalizationFileTypes ]


const_OutputFile = "LANGUAGE.gzdoom330"
const_OutputFilesLanguages = [ ".enu", ".rus" ] 	# Other languages converting not supported yet.
const_OutputFilesPostfix = [ i for i in const_LocalizationFileTypes ]


# Files and functions:

loczFiles = []


def handleSpecialSequences( text: str ) -> str:
	return text.replace( '"', '\\"' ).replace( '\n', '\\\n' ).replace( "ё", "е" ).replace( "—", "-" )


def writeout( fmt: str, loczText = [], toall = False ):
	global loczFiles

	if len( loczText ) == 0:
		for outfile in loczFiles:
			outfile.write( fmt )

	elif toall:
		locztext = loczText[ 0 ]

		for outfile in loczFiles:
			outfile.write( fmt % locztext )

	else:
		for i in range( len( loczText ) ):
			if ( loczText[ i ] is not None ):
				loczFiles[ i ].write( fmt % loczText[ i ] )



# Main cycle:

for localizationType in range( len( const_LocalizationFileTypes ) ):

	# Opening output files:
	loczPrefix = const_DIR + const_OutputFile
	loczPostfix = const_OutputFilesPostfix[ localizationType ]

	loczFiles = [
		open( loczPrefix + const_OutputFilesLanguages[ 0 ] + loczPostfix, 'w', newline='' ),
		open( loczPrefix + const_OutputFilesLanguages[ 1 ] + loczPostfix, 'w', encoding='cp1251', errors='replace', newline='' )
	]

	# Write headers:
	writeout( "%s\n\n", [ "[enu default]", "[rus]" ] )


	with open( const_DIR + const_InputFile + const_InputFilesPostfix[ localizationType ], encoding='utf-8' ) as _in:
		rows = csv.reader( _in )
		rows.__next__()

		for currow in rows:
			_, cellRemark, cellID, cellEn, cellRu = currow

			if ( not cellRemark and not cellID ):
				writeout( "\n" )

			elif ( cellRemark and not cellID ):
				writeout( "// %s\n", [ ( cellRemark ) ], True )

			else:
				isRusText = True if ( len( cellRu ) != 0 ) else False

				rusTextCortage = ( cellID, handleSpecialSequences( cellRu ) ) if isRusText else None

				writeout( "%-37s = \"%s\";", [
					( cellID, handleSpecialSequences( cellEn ) ),
					rusTextCortage
				] )

				if ( cellRemark ):
					writeout( " // %s", [ cellRemark, cellRemark if isRusText else None ] )

				writeout( "%s", [ "\n", "\n" if isRusText else None ] )


	for outfile in loczFiles:
		writeout( "\n" )
		print( "File " + outfile.name + " updated successfully." )

	for outfile in loczFiles:
		outfile.close()


print( "Updated successfully." )

