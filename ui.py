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
        if self.dumpToFile == True: self.__openTxt(fileName)

    def __openTxt(self, fileName):
        try: self.f = open(fileName, "w+")
        except Exception as e:
            self.dumpToFile = False
            print(e)

    def __writeTxt(self, message):
        try: self.f.write(str(message) + "\n")
        except Exception as e: print(e)

    def __closeTxt(self):
        try: self.f.close()
        except Exception as e: print(e)

    def Out(self, message):
        if self.dumpToStdOutput == True: print(message)
        if self.dumpToFile == True: self.__writeTxt(message)

    def Close(self):
        if self.dumpToFile == True: self.__closeTxt()

if __name__ == '__main__':
    pass
