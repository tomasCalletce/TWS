
import json
def getLogger():
    # try:
    with open('./files/logger.json', 'r') as file:
        return json.load(file)
    file.close()
    # except :
    #     print("exception occured when reading")

def writeLogger(data):
    # try:
    with open('./files/logger.json', 'w') as file:
        json.dump(data, file,indent=3)
    file.close()
    # except:
    #     print("exception occured when writing")