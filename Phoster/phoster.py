from pyzip import PyZip
from pyfolder import PyFolder
import xml.etree.ElementTree as ET
import sys

# **********************************************************
# Dumb utilities for my weird output formatting preferences.
# **********************************************************

def verboseInput( description, query ):
	print( "" )
	print( description )
	return input( query )

def padPrint( output ):
	print( "" )
	print( output )
	print( "" )

# **********************************************************
# The actual work.
# **********************************************************


#*** Finds a child node with the given "label" attribute value.
def findChild( nodes, name ):
	for node in nodes:
		if str( node.attrib["label"] ) == name:
			return (True,node)
	return (False,)


#*** Searches the given XML node for a child node with the given tag.
def findNode( nodes, tag ):
	for node in nodes:
		if node.tag == tag :
			print( "		" + str(node) )
			return node
	return False


#*** Create a scalebar element.
def createScalebar( id, label, idA, idB, distance, accuracy ):
	bar = ET.Element("scalebar")
	bar.attrib["id"]		= str(id)
	bar.attrib["label"]		= str(label)
	epA = ET.Element("endpoint")
	epA.attrib["marker_id"]	= str(idA)
	epB = ET.Element("endpoint")
	epB.attrib["marker_id"]	= str(idB)
	ref = ET.Element("reference")
	ref.attrib["d"]			= str(distance)
	ref.attrib["accuracy"]	= str(accuracy)
	ref.attrib["enabled"]	= "true"
	bar.append(epA)
	bar.append(epB)
	bar.append(ref)
	return bar


#*** Performs pairwise scalebar creation
def pairwise():
	distance = verboseInput( "How far apart are the targets in each pair?"	, "Distance (meters): " )
	accuracy = verboseInput( "How accurate is that measurement?"			, "Accuracy (meters): " )
	
	padPrint( "Creating scalebars from pairs of targets..." )
	
	nodes = PyFolder(path, interpret=False, auto_create_folder=False)
	chunks = nodes.index("chunk.zip")
	
	for chunk in chunks:
		
		print( "Parsing chunk..." )
		zip		= PyZip().from_file( chunk )
		tree	= ET.ElementTree(    ET.fromstring(  zip["doc.xml"]  )    )
		root	= tree.getroot()
		
		print( "	Finding markers node..." )
		markers		= findNode( root, "markers" )
		
		print( "	Finding scalebars node..." )
		scalebars	= findNode( root, "scalebars" )
		if not scalebars:
			scalebars = ET.Element("scalebars")
			scalebars.attrib["next_id"] = "0"
			root.append( scalebars )
		
		id = -1
		print( "	Adding scalebars..." )
		for node in markers:
			labelA	= str( node.attrib["label"] )
			print( str( node.attrib["label"] ) )
			numA	= int( labelA.split()[1] )
			if numA % 2 == 1:
				numB = numA + 1
				labelB	= "target " + str( numB )
				idA = node.attrib["id"]
				print( "		Found: " + labelA )
				print( "			Seeking: " + labelB )
				partner = findChild( markers, labelB )
				if partner[0]:
					partner = partner[1]
					print( "				Found: " + labelB )
					print( "				Creating scalebar..." )
					id = id + 1
					scalebars.attrib["next_id"] = str( id+1 )
					idB = partner.attrib["id"]
					bar = createScalebar( id, (labelA + "_" + labelB), idA, idB, distance, accuracy )
					scalebars.append(bar)
					padPrint( ET.tostring(bar) )
		
		padPrint ( "Writing to chunk file..." )
		
		xmlString = ET.tostring(root)
		padPrint( xmlString )
		
		zip["doc.xml"] = xmlString
		zip.save(chunk)
					
	
# **********************************************************
# The setup.
# **********************************************************

path = ""

if len( sys.argv ) < 2:
	print( "" )
	print( "Please supply a .files directory to be processed." )
	print( "Example:" )
	print( "C:\\>phoster.exe C:\\scans\\rock\\rock.files" )
	print( "" )
	sys.exit()

fedPath = str(sys.argv[1])
if ( fedPath[-6:] == ".files" ):
	path = fedPath
else:
	print( "" )
	print( "Please supply a .files directory to be processed." )
	print( "Example:" )
	print( "C:\\>phoster.exe C:\\scans\\rock\\rock.files" )
	print( "" )
	sys.exit()
	
# **********************************************************
# .files directory given. But what do we want to do with it?
# **********************************************************

action = "";

print( "" )
print( "Would you like to create scalebars:" )
print( "	a: Pairwise (1&2, 3&4... All pairs have the same distance. )" )
print( "	b: From a profile - not yet supported." )
print( "	c: Nevermind." )
print( "" )

while action == "":
	action = input( "Selection: " )

if action == "c":
	padPrint( "Exiting..." )
	sys.exit()
	print( "" )
if action == "a":
	pairwise()
if action == "c":
	padPrint( "We've got a wise-guy over here." )


	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	