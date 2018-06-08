# phoster
Scalebar utility for Agisoft Photoscan



Background:

Agisoft Photoscan allows the use of coded targets, which are detected automatically with high accuracy. Any two targets can be used to create a scalebar, which stores the distance between the two targets. Scalebars allow scans to conform to the real-world dimensions of the scanned object, and may improve scan accuracy.




Phoster:

Creating large numbers of scalebars in Photoscan is labor-intensive. This utility can be used to create a large number of identical scalebars using pairs of coded targets.




Usage example:

1. Print 50 pairs of coded targets. Coded targets should be paired sequentially. e.g. "target 1" should be on the same strip as "target 2" and "target 3" should be on the same strip as "target 4". The distance between each pair of coded targets should be identical. e.g. "target 2" and "target 3" should be the same distance from each other as "target 1" and "target 2".

2. Place the coded target strips around the obect to be scanned, then take photographs as usual.

3. Create a new Agisoft Photoscan project and load the photos.

4. Choose Tools > Markers > Detect Markers to detect the coded targets on the strips.

5. Once the markers hasve been detected, save and close the project.

6. Drag the <project name>.files directory for your Photoscan project onto phoster.exe, or run:
phoster.exe C:\path\to\project\project.files

7. Choose option "a", for pairwise scalebar creation. I probably should have removed the non-functional option. It's there to inspire me.

8. Enter a single distance value to be applied to each scalebar.

9. Enter a single accuracy value to be applied to each scalebar.

10. Re-open the project in Agisoft Photoscan.

You should now see 50 scalebars in your project. They'll all have the same distance and accuracy. You're ready to align your photos, as usual.




Installation:
Easy: Download the ZIP in the dist folder, extract the ZIP, and run the .exe in the extracted folder.
Hard:
Install Python 3.x
> pip install pyzip
> pip install pyfolder
> python phoster.py C:\path\to\file

I've only tested the .py version in Windows, but as far as I know it should run on Linux.




Future plans:
I'm hoping to create a version that can access stored scalebar profiles. For example, a profile in which "target 1" and "target 2" are always 2 meters apart, but "target 3" and "target 4" are always 50cm apart. This would allow the user to select groups of coded targets for projects at specific scales, or mix scalebar sizes on projects that need good accuracy on both large and small scales.




Warnings:
This program modifies your project file. It was written hastily for personal use, and is designed to be run on a brand new project right after marker detection. Don't run it on a project with data you don't want to lose.
