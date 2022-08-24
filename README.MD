# Photoshop Batch Export

## Installation

To use this script ensure you have the installed the requied python modules. To do this run ``pip install -r requirements.txt``.

## Usage

Run the script - you will be presented with 4 options: ``Create CSV``, ``Reset Program``, ``Create Directories`` and ``Exit``.

**Create CSV** will take the images provided in the image folders and create an excel spreadsheet which maps image names to the image position defined by the image folder (1,2 or 3).

**Reset Program** will delete all of the files in all of the directories inside the root folder.

**Create Directories** is what you should run when you first clone the repo. This will ask you how many image folders you need (how many images will be on each row of the csv)

**Exit** will quit the program.

## Information

There is a given file structure to make usage easier.

- ``img1``, ``img2``,``img3`` etc. are used to store the images you wish to be included in the CSV, these relate to the variables you have defined in photoshop.
- ``templates`` is used to store any photoshop templates you have created.
  