import wget
import glob
import os
import pymongo
import pprint
from googlecode import module


def Search(datlabel):
    client = pymongo.MongoClient()
    db = client.TwitterData
    data1 = db.TwitterData.find({})
    #print(data1)
    string = 'Label' + datlabel + 'is found in the following twitter handles:'
    print(string)
    for dat in data1:
        pictures = dat['Picture Details']
        for pic in pictures:
            labelzz = pic['Descirption labels']
            for i in labelzz:
                if i == datlabel:
                    print(dat['Twitter handle'])



def AddDataBase(text,name):
#This part reads the json file from the github link provided
#Then stores it in an array called data

#Now we demonstrate how to create that data in our own mongodb database
    sup = []
    client = pymongo.MongoClient()
    db = client.TwitterData
    counter = 1
    for i in text:
        sup.append({"Picture #" : i, "Descirption labels" : text[i]})
        counter = counter +1
    data = {"Twitter handle": name, "Picture Details": sup}
    db.TwitterData.insert(data)

    
if __name__ == '__main__':
   # os.system("mongod")
    print("Pick a number from the choices underneath\n")
    print("1. View current database\n")
    print("2. Add a twitter handle to the current database\n")
    print("3. Search for a particular label\n")
    choice = raw_input("Choice: ")
    if choice == '1':
        client = pymongo.MongoClient()
        db = client.TwitterData
        data1 = db.TwitterData.find({})
        for doc in data1:
            pprint.pprint(doc)
    else:
        if choice == '2':
            name = raw_input('What is the twitter handle you want to add: ')
            text = module(name, 20)
            AddDataBase(text, name)
        else: 
            specificlabel = raw_input('What is the label you want to search for: ')
            Search(specificlabel)
      


   
    print("\nDone\n")
