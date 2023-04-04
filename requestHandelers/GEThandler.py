import os

def handle():

    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'files', 'index.html')

    with open(path, "r") as file:
            return file.read()