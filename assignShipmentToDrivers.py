#record that will save the ponderation for every combination
import sys
import logging
import argparse
from os import system, name
from tabulate import tabulate




parser = argparse.ArgumentParser(prog='assignShipmentToDrivers')
parser.add_argument('driversFile',nargs='+', help='A newfile separeted file with the names of the drivers')
parser.add_argument('streetsFile',nargs='+', help='A newfile separeted file with the names of the streets')


try:
    arg = sys.argv[2]
except IndexError:
  parser.print_help()
  raise SystemExit()

if(sys.argv[1]=='-h' or sys.argv[2]=='-h' ) or len(sys.argv)>3:
    parser.print_help()
    raise SystemExit()


#configuring the Log settings
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.ERROR)




#class to save The ponderation of every combination
class recordAssignation:
    driverName = None
    streetName = None
    suitabilityScore = 0
    def __init__(self, driverName, streetName, suitabilityScore):
        self.driverName = driverName
        self.streetName = streetName
        self.suitabilityScore = suitabilityScore
 
    def __repr__(self):
        return  '[' +self.driverName + ', ' + self.streetName + ', ' + str(self.suitabilityScore) + ']' + '\n' 
    def __iter__(self):
        pass

def clear():
 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
 

#print factors of a integer

def isTherecommonFactors(x,y):
    xFactors = []
    yFactors = []
    isThereACommonFactor = False
    for i in range(2, x + 1):
        if x % i == 0:
           xFactors.append(i)
    for i in range(2, y + 1):
        if y % i == 0:
           yFactors.append(i)
    logging.debug('factors x %s', xFactors)
    logging.debug('factors y %s', yFactors)
    for value in xFactors:
        if value in yFactors:
            isThereACommonFactor = True
            break
    return isThereACommonFactor



# count number of vowels in a String
def countVowelsString(string):
    num_vowels = 0
    vowels = "aeiou"
    for v in vowels:
        num_vowels = num_vowels + string.lower().count(v)
    return num_vowels

#count consonets not the number there is no a vowel, just because maybe the string could containg special characters as colon, semicolon, etc
def countConsonantsString(string):
    num_ctes = 0
    ctes = "bcdfghjklmnpqrstvwxyz"
    for v in ctes:
        num_ctes = num_ctes + string.lower().count(v)
    return num_ctes

def isEvenLengthString(string):
    isEven = False
    if len(string)%2 == 0:
        isEven = True
    return isEven


class FileEmptyException(Exception):
    def __init__(self, message='FileIsEmpty'):
        # Call the base class constructor with the parameters it needs
        super(FileEmptyException, self).__init__(message)


try:
   
    driver_list =[]
    street_list=[]
    with open(sys.argv[1], "r") as file:
        driver_list=file.read().splitlines()
    file.close
    with open(sys.argv[2], "r") as file:
        street_list=file.read().splitlines()
    file.close

    #Removing any leading and trailing whitespaces

    driver_list = [i.strip() for i in driver_list]
    street_list = [i.strip() for i in street_list]
   
    #Remove empty lines
    while("" in driver_list):
        driver_list.remove("")
    
    while("" in street_list):
        street_list.remove("")


    if len(street_list) == 0 or len(driver_list)== 0:
        raise(FileEmptyException)

#for each line from the list, print the line
    ponderations = []
    for street in street_list:
        logging.debug("Street %s length %s ", street, len(street))
        isEven = isEvenLengthString(street)
        logging.debug (" Is the street %s Even? %s", street, isEven)
        for driver in driver_list:
            logging.debug("Driver %s length %s ", driver, len(driver))
            record = recordAssignation(driverName=driver,streetName=street,suitabilityScore=0)
            if isEven:
                record.suitabilityScore = 1.5 * countVowelsString(driver)
            else:
                record.suitabilityScore = countConsonantsString(driver)
           
            if isTherecommonFactors(len(driver),len(street)):
                record.suitabilityScore = record.suitabilityScore * 1.5
            ponderations.append(record)
    logging.debug('All ponderations: %s', ponderations)
    ponderations.sort(key=lambda x: x.suitabilityScore, reverse= True)
    logging.debug('All ponderations: %s', ponderations)

    result = []
    
    numDrivers = len(driver_list)
    logging.debug("# of drivers :: %i", numDrivers)

    tableHeaders= ['Driver','Street','SS']
    
    for x in range(len(driver_list)):
      
        if len(ponderations) > 0 :
            record = ponderations[:1][0]
            result.append([record.driverName, record.streetName, record.suitabilityScore])
            ponderations = [i for i in ponderations if i.driverName!=record.driverName and i.streetName != record.streetName]
    clear()
    print('The optimal assignations are below : ')

    print(tabulate(result, headers=tableHeaders))




except FileNotFoundError as e:
        logging.error("File not found!")
        parser.print_help()
except FileEmptyException as e:
        logging.error("One of the files is empty")
        parser.print_help()


        


