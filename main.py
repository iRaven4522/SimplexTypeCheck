import os
import csv


def searchCSV(model):
    with open('simplex.csv', rb) as file:
        simplex = csv.reader(file, delimiter=",")
        for content in enumerate(simplex):
            if content[0] == model:
                return content[1]
            else:
                return None
            
def mainMethod():
    request = input(f'Enter a Simplex Model Number below:\n')
    result = searchCSV(request)
    if result is not None:
        if result == 'addressable':
            print(f"The device {request} is Addressable.")
        elif result == 'es':
            print(f"The device {request} is an ES device.")
        elif result == 'freerun':
            print(f"The device {request} is a FreeRun device.")
        elif result == 'selectable':
            print(f"The device {request} is an selectable.")
        elif result == 'smartsync':
            print(f"The device {request} is an SmartSync device")
        elif result == 'syncable':
            print(f"The device {request} is an Syncable device.")
        else:
            print(f"An error has occurred.")