from pyzip import PyZip
from pyfolder import PyFolder
import xml.etree.ElementTree as ET
import sys
	
# **********************************************************
# The actual work.
# **********************************************************

def findChild( nodes, name ):
	for node in nodes:
		if str( node.attrib["label"] ) == name:
			return (True,node)
	return (False,)

def pairwise():
	print( "" )
	print( "How far apart are the targets in each pair?" )
	distance = input( "Distance (meters): " )
	print( "" )
	print( "How accurate is that measurement?" )
	accuracy = input( "Accuracy (meters): " )
	print( "" )
	print( "Creating scalebars from pairs of targets..." )
	print( "" )
	nodes = PyFolder(path, interpret=False, auto_create_folder=False)
	chunks = nodes.index("chunk.zip")
	for chunk in chunks:
		print( "Found chunk: " + chunk )
		
		print( "Opening chunk..." )
		zip = PyZip().from_file( chunk )
		
		print( "	Parsing chunk..." )
		tree = ET.ElementTree(    ET.fromstring(  zip["doc.xml"]  )    )
		root = tree.getroot()
		
		print( "	Finding markers node..." )
		markers = ""
		for node in root:
			if node.tag == "markers" :
				print( "		" + str(node) )
				markers = node
		
		print( "	Finding scalebars node..." )
		scalebars = ""
		for node in root:
			if node.tag == "scalebars" :
				print( "		" + str(node) )
				scalebars = node
		if scalebars == "":
			scalebars = ET.Element("scalebars")
			scalebars.attrib["next_id"] = "0"
			root.append( scalebars )
		
		id = -1
		print( "	Adding scalebars..." )
		for node in markers:
			labelA	= str( node.attrib["label"] )
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
					bar = ET.Element("scalebar")
					bar.attrib["id"]		= str(id)
					bar.attrib["label"]		= str(labelA + "_" + labelB)
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
					scalebars.append(bar)
					print( "" )
					print( ET.tostring(bar) )
					print( "" )
		
		print ( "" )
		print ( "Writing to chunk file..." )
		print ( "" )
		
		xmlString = ET.tostring(root)
		print ( "" )
		print( xmlString )
		print ( "" )
		
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
	print( "" )
	print( "Exiting..." )
	sys.exit()
	print( "" )
if action == "a":
	print( "" )
	pairwise()
	print( "" )
if action == "c":
	print( "" )
	print( "We've got a wise-guy over here." )
	print( "" )



#pyzip = PyZip(PyFolder(path_to_compress, interpret=False))
#pyzip.save("compressed_folder.zip")