Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import xml.etree.ElementTree as ET

from datetime import timedelta, date

 

def test_exercise1 (x,y):

    Depart_dt = date.today() + timedelta(days=x)

    Return_dt  =  date.today() + timedelta(days=y)

    filename = "../payloads/IM/payload.xml"

    xmlTree = ET.parse(filename)

    rootElement = xmlTree.getroot()

    print(rootElement)

    for value1  in rootElement.iter("DEPART"):

        #print(value.text)

        value1.text = Depart_dt

    for value2  in rootElement.iter("RETURN"):

            #print(value.text)

            value2.text = Return_dt

           

    print(value1.text,value2.text)

 

test_exercise1(8,9)