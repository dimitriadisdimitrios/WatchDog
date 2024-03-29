# Utilities Version 1.0
import os, sys, re

# If os.name == nt then the script runs on windows
def checkOSSystem(mPath):
    if os.name == "nt":                
        return re.sub(r"/", "\\\\", mPath)
    else:        
        return re.sub(r"\\", "/", mPath)

# Function which verifies that a file exist
def checkIfFileExists(filePath):
    if os.path.isfile(filePath):
        return True
    else:
        raise Exception("Given path ("+filePath+") of file doesn't exist. Please correct the given path and try again !")


# Function that takes a path of the file and returns only the path
def extractPath(mPath):    
    if os.name == "nt": # Windows                
        return "\\".join(mPath.split("\\")[0:-1])
    else: # Unix
        return "/".join(mPath.split("/")[0:-1])