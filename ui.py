#-------------------------------------------------------------------------------
# Name:        ui
# Purpose:
#
# Author:      Lorenzo Bolognese
#
# Created:     11/12/2019
# Copyright:   (c) Lorenzo Bolognese 2019
# Licence:     MIT
#-------------------------------------------------------------------------------

class Print(object):
    def __init__(self, dumpToStdOutput = True, dumpToFile = False, fileName = ""):
        self.dumpToStdOutput = dumpToStdOutput
        self.dumpToFile = dumpToFile
        if self.dumpToFile == True:
            self.f = open(fileName, "w+")

    def Out(self, message):
        if self.dumpToStdOutput == True: print(message)
        if self.dumpToFile == True: self.f.write(str(message) + "\n")

    def Close(self):
        if self.dumpToFile == True: self.f.close()

if __name__ == '__main__':
    main()
