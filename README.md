# SDE Code Exercise : Platform Science Code Exercise
# assignShipmentToDrivers

&copy; Claudia Falcón Mata 

Script that assign drivers to address delivery according to a specific data science algorithm. 

The algorithm:



-  If the length of the shipment's destination street name is even, the base suitability score (SS) is the number of vowels in the driver’s name multiplied by 1.5.
- If the length of the shipment's destination street name is odd, the base SS is the number of consonants in the driver’s name multiplied by 1.
- If the length of the shipment's destination street name shares any common factors (besides 1) with the length of the driver’s name, the SS is increased by 50% above the base SS.

The script was written in python and is distribuited as self container script.

All code and files rated to this project you can find in the repository:

[**assignShipmentToDrivers**](https://github.com/claudiafalcon/logisticDataScienceAlgoritm)


***

## Installation Instructions

   1. Download ZIP File according to Operating System
        * **MACOS** [Download MacOs Distribution](https://github.com/claudiafalcon/logisticDataScienceAlgoritm/blob/main/dist_macos/assignShipmentToDrivers.zip "Download MACOS") 
        * **WINDOWS** [Download Windows Distribution](https://github.com/claudiafalcon/logisticDataScienceAlgoritm/blob/main/dist_windows/assignShipmentToDrivers.zip "Download Windows") 
        * **LINUX(UBUTU)** [Download Linux Distribution](https://github.com/claudiafalcon/logisticDataScienceAlgoritm/blob/main/dist_linux/assignShipmentToDrivers.zip "Download Linux")
    2. Unzip File in your preference dir
    3. Go to directory _assignShipmentToDrivers_.
    4. Run script assignShipmentToDrivers with extension _so_ or _exe_ according SO as Usage section describes.

***

## Usage


_usage: assignShipmentToDrivers [-h] driversFile [driversFile ...] streetsFile [streetsFile ...]_

* positional arguments:
    * **driversFile**  A newfile separeted file with the names of the drivers
    * **streetsFile**  A newfile separeted file with the names of the streets

* options:
    * **-h**  show this help message and exit

***

## Example of usage and output

NOTE: There are two sample files in the repo:

1. Drivers file [Drivers File test](https://github.com/claudiafalcon/logisticDataScienceAlgoritm/blob/main/drivers.txt "Download drivers file") 
2. Streets file [Streets File test](https://github.com/claudiafalcon/logisticDataScienceAlgoritm/blob/main/streets.txt "Download streets file") )

```
./assignShipmentToDrivers ../../OneDrive/LogisticDataScienceAlghoritm/drivers.txt ../../OneDrive/LogisticDataScienceAlghoritm/streets.txt

The optimal assignations are below : 
Driver              Street                    SS
------------------  ---------------------  -----
Maximillian Hinton  Abby Park Street       15.75
Harper Murphy       Danish Avenue          13.5
Nathanael Mata      Paul Hladovka Avenue   13.5
Diana Melendez      Southern Abby Avenue   13.5
Gunnar Francis      Mitch Cromwood Avenue  13.5
Dominik Terry       Zosnul Street          12
Jessica Guzman      Northern Abby Avenue   11.25
Simeon Chase        Impressionist Avenue   11.25
Elijah Yates        Hurbanova Street       11.25
Lillian Butler      Katrina Street         11.25
Aniyah Mccoy        Newhaven Avenue        10.5
Evelyn Garner       Barn Street             8
Yosef Clayton       Sylvania Avenue         8
Halle Roberts       Water-lily Avenue       8
Jaylen Bender       River Side Road         8




```
***

## **Build and distribution**

This script is distribuited as self container app, using pyinstaller to build.

The unique source file code is: _assignShipmentToDrivers.py_

### **DEPENDENCIES**

To re-build and generate distribution files, you need to have installed:

1. Python version +3.08 [Python Info](https://www.python.org/downloads/ "Python Download")
2. PIP package installer fro Python [PIP Info](https://pypi.org/project/pip/)
3. Tabulate project [Tabulate Info](https://pypi.org/project/tabulate "Tabulate info")
4. Pyinstaller [Pyinstaller Info](https://pyinstaller.org/en/stable)

All these are tools should be installed before build.
***
### **BUILD PROCESS**

1. Download python script _assignShipmentToDrivers.py_ [Download script](https://github.com/claudiafalcon/logisticDataScienceAlgoritm/blob/main/assignShipmentToDrivers.py)
2. On the root directory of _assignShipmentToDrivers.py_   run pyintsaller as:

```
pyinstaller assignShipmentToDrivers.py 
```
***
### **LOGGING PREFERENCE**

You can modify the level of trace, modifying the _assignShipmentToDrivers.py_  directry, changing the following code line for the level requered:

```
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.ERROR)


```

NOTE: Level DEBUG will print all the Suitability Score (SS) for each driver and street availables, and more details about the process. 


