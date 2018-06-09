class File:
    def __init__(self, filePath, filename, numberLines, pythonFileCount, avg):
        self._filename = filename
        self._numberLines = numberLines
        self._pythonFileCount = pythonFileCount
        self._avg = avg
    def getlines(self):
        return self._numberLines
    def setlines(self, newvalue):
        self._numberLines = newvalue
    def __str__(self):
        outstring = "Number of Python files = " + str(self._pythonFileCount) + " Average: " + str(self._avg)
        return outstring