# Installation

## Prerequisites

The following Python packages are required:

* numpy
* scipy
* pytest

## Getting the Source Code

You can either download the source as a ZIP file and extract the contents, or clone the MachUp repository using Git. If your system does not already have a version of Git installed, you will not be able to use this second option unless you first download and install Git. If you are unsure, you can check by typing `git --version` into a command prompt.

### Downloading source as a ZIP file

1. Open a web browser and navigate to [https://github.com/usuaero/MachUpX](https://github.com/usuaero/MachUpX)
2. Make sure the Branch is set to `Master`
3. Click the `Clone or download` button
4. Select `Download ZIP`
5. Extract the downloaded ZIP file to a local directory on your machine

### Cloning the Github repository

1. From the command prompt navigate to the directory where MachUp will be installed
2. `git clone https://github.com/usuaero/MachUpX`

## Installing

Navigate to the root (MachUpX/) directory and execute

`python3 setup.py install`

Please note that any time you update the source code, the above command will need to be run.

## Testing the Installation

Once the installation is complete, run

`py.test test/`

to verify MachUpX is working properly on your machine.