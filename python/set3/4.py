import requests
import xml.etree.ElementTree as ElementTree

def getdata():
        req = requests.get('https://www.w3schools.com/xml/simple.xml')
        root = ElementTree.fromstring(req.content)
        print("Food Menu")
        for food in root.findall('food'):
                name = food.find('name').text
                price = food.find('price').text
                print("Item     :",name)
                print("Price    :", price)
                print("******************************")

getdata()