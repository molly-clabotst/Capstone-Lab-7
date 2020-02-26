import requests
from pprint import pprint

def main():
    numBit = userInput()
    dollhairs = convert(numBit, conversionFactor)
    display(dollhairs)

def userInput():
    while True:
        try:
            numBit = float(input('How many bit coin do you have? '))
            return numBit
        except:
            print('Please try again, only enter data in decimal form. ')

def getData():
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    bitcoin_data = requests.get(url).json()
    print(bitcoin_data)
    return bitcoin_data

def getConversionFactor():
    bitcoin_data = getData()
    return bitcoin_data['bpi']['USD']['rate_float']

def convert(numBit):
    conversionFactor = getConversionFactor()
    return numBit*conversionFactor

def display(dollhairs):
    print(f'You have, {dollhairs} dollhairs.')

if __name__ == '__main__':
    main()