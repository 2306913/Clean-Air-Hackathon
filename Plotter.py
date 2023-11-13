
import csv
import re
import matplotlib.pyplot as plt
import numpy as np

def main():

    file = open(r'C:\Users\Benjamin Martin\Documents\University\Clean-Air-Hackathon\Data\sensor_data\SL005_Kirkstall_Valley_Primary\2023\11\2023-11-12.csv')
    type(file)

    csvReader = csv.reader(file)

    header = []
    header = next(csvReader)

    data = []

    for x in range(8, len(header), 2):

        res = header[x].split(" ")[0]
        res = res.replace("um", "")
        res = res.replace("PM", "")
        res = res + "um"

        data.append(res)

    yPlot = np.arange(1,13, 1)

    plt.plot(yPlot,data)
    plt.show()
if __name__ == "__main__": # This function executes "main" when this file is run directly as a script, but prevents automatic execution when imported.

    main()