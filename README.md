# phoster
Scalebar utility for Agisoft Photoscan



Background:

Agisoft Photoscan allows the use of coded targets, which are detected automatically with high accuracy. Any two targets can be used to create a scalebar, which stores the distance between the two targets. Scalebars allow scans to conform to the real-world dimensions of the scanned object, and may improve scan accuracy.



Phoster:

Creating large numbers of scalebars in Photoscan is labor-intensive. This utility can be used to add a large number of scalebars to a Photoscan project, instantly, making scalebars much more convenient. Scalebars can be created automatically if each of the scalebars have identical lengths. If there are scalebars of different lengths, a profile can be created for the set of scalebars that will allow the set to be added to projects by specifying the file containing the profile.



Usage Example - Profile-Based Scalebars:

1. Print some scalebars, then measure each scalebar. The scalebars can be different sizes.

2. Create a new text file and enter the the scalebar information into the file. The file must be JSON formatted. An example file is available alongside the uncompiled script, and more information can be found at the end of this README. It's prety simple.

2. Place the coded target strips around the obect to be scanned, then take photographs as usual.

3. Create a new Agisoft Photoscan project and load the photos.

4. Choose Tools > Markers > Detect Markers to detect the coded targets on the strips.

5. Once the markers have been detected, save and close the project.

6. Drag the <project name>.files directory for your Photoscan project onto phoster.exe, or run:
phoster.exe C:\path\to\project\project.files

7. Choose option "b", for profile-based scalebar creation.

8. Drag the JSON-formatted scalebar profile that you want to use onto the command window, or type the path to the file, then hit Enter.

9. Re-open the project in Agisoft Photoscan.



Usage Example - Pairwise Scalebars:

If you don't want to create a JSON file by hand, pairwise scalebar creation may be easier.

1. Print 50 pairs of coded targets. Coded targets should be paired sequentially. e.g. "target 1" should be on the same strip as "target 2" and "target 3" should be on the same strip as "target 4". The distance between each pair of coded targets should be identical. e.g. "target 2" and "target 3" should be the same distance from each other as "target 1" and "target 2".

2. Place the coded target strips around the obect to be scanned, then take photographs as usual.

3. Create a new Agisoft Photoscan project and load the photos.

4. Choose Tools > Markers > Detect Markers to detect the coded targets on the strips.

5. Once the markers have been detected, save and close the project.

6. Drag the <project name>.files directory for your Photoscan project onto phoster.exe, or run:
phoster.exe C:\path\to\project\project.files

7. Choose option "a", for pairwise scalebar creation.

8. Enter a single distance value to be applied to each scalebar.

9. Enter a single accuracy value to be applied to each scalebar.

10. Re-open the project in Agisoft Photoscan.

You should now see 50 scalebars in your project. They'll all have the same distance and accuracy. You're ready to align your photos, as usual.



Installation:

Easy: Download the ZIP in the dist folder, extract the ZIP, and run the .exe in the extracted folder.

Hard:

Install Python 3.x

> pip install pyzip<BR>
> pip install pyfolder<BR>
> python phoster.py C:\path\to\Photoscan\project\file<BR>

I've only tested the .py version in Windows, but as far as I know it should run on Linux.



Future plans:

None. Profiles were once the future goal. They were easy. I can't think of anything else I want it to do.



JSON Formatting:

The JSON format is pretty simple. The progile below describes two scalebars, "My One Meter Scalebar" and "My Two Meter Scalebar". The "start" line and "end" line should be the names of the two targets that compose the scalebar. The distance is the distance between the two targets in meters, and the accuracy is the accuracy of that distance measurement in meters. The name can be anything, but should be unqiue. To add more scalebars, just copy the last scalebar (including the curly-braces and the comma that preceeds it), paste a new copy right after the closing curly brace of the last scalebar (after the closing curly brace, but before the closing square brace), then update the information in the new block to describe the scalebar you're adding.
{
	"scalebars":[
		{
			"name":"My One Meter Bar",
			"start":"target 1",
			"end":"target 3",
			"distance":"1.0",
			"accuracy":"0.01"
		},
		{
			"name":"My Two Meter Bar",
			"start":"target 2",
			"end":"target 4",
			"distance":"2.0",
			"accuracy":"0.01"
		}
	]
}



Warnings:

This program modifies your project file. It was written hastily for personal use, and is designed to be run on a brand new project right after marker detection. Don't run it on a project with data you don't want to lose.
