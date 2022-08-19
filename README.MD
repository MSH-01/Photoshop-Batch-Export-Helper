# Photoshop Batch Export

## Installation

To run this script ensure you have the following Python packages installed:
``os``,``xlsxwriter`` and ``shutil``.

## Usage

Once this is complete, you should place your images into either ``/img1``, ``/img2``, or ``/img3``. Where your images go depends on the position you want the individual images to be placed.

Next, run the script - you will be presented with 4 options: ``Create Spreadsheet``,``Copy images to originals``, ``Reset Program`` and ``Exit``.

**Create Spreadsheet** will take the images provided in the image folders and create an excel spreadsheet which maps image names to the image position defined by the image folder (1,2 or 3).

**Copy images to originals** will copy the images from the 'img' folders into the 'originals' folder.

**Reset Program** will delete all of the files in all of the directories inside the root folder.

**Exit** will quit the program.