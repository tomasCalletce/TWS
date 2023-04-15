import os

def getFile(fileName,mode):

    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'files',fileName)

    with open(path, mode) as file:
            return file.read()
    
      