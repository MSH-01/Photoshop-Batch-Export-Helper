# Photoshop Batch Export

## Installation

To run this script ensure you have the following Python packages installed:
``os``,``csv`` and ``shutil``.

## Information

There is a given file structure to make usage easier.

- ``img1``, ``img2``,``img3`` are used to store the images you wish to be included in the CSV, these relate to the variables you have defined in photoshop.
- ``templates`` is used to store any photoshop templates you have created.
- ``psd`` is used to store .PSD files created by photoshop when exporting data sets as files.
- ``output`` is used to store the image files that photoshop creates when using the image processor (for example .jpg).

## Usage

Once this is complete, you should place your images into either ``/img1``, ``/img2``, or ``/img3``. Where your images go depends on the position you want the individual images to be placed.

Next, run the script - you will be presented with 4 options: ``Create CSV``, ``Reset Program`` and ``Exit``.

**Create CSV** will take the images provided in the image folders and create an excel spreadsheet which maps image names to the image position defined by the image folder (1,2 or 3).

**Reset Program** will delete all of the files in all of the directories inside the root folder.

**Exit** will quit the program.
