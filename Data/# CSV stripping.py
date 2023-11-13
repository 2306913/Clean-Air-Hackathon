# CSV stripping

import csv
import re

def main():

    file = open(r'C:\Users\Benjamin Martin\Documents\University\Clean-Air-Hackathon\Data\sensor_data\SL005_Kirkstall_Valley_Primary\2023\11\2023-11-12.csv')
    type(file)

    csvReader = csv.reader(file)

    header = []
    header = next(csvReader)

    data = []

    for x in range(8, len(header)):

        res = header[x].split(" ")[0]
        res = res.replace("um", "")
        res = res.replace("PM", "")
        res = res + "um"

        data.append(res)

    print(data)
 
if __name__ == "__main__": # This function executes "main" when this file is run directly as a script, but prevents automatic execution when imported.

    main()