"""
DS3002 Project1 
By Emily Feng (ejf9kwf)

This repository is created for DS 3002 Project 1 only.
"""
import pandas as pd
import csv
import requests
import os
import json
import re

"""
The dataset named "Pokemon with stats" is useful for Pokemon lovers and Pokemon games players.
It contains detailed information including name, type, HP, speed of each Pokemon.
The data table is expressed in a csv file. All data are acquired from official websites such as pokemon.com

Information of this dataset
Name: Pokemon with stats
Author: Alberto Barradas
Where: Kaggle
URL:https://www.kaggle.com/abcsds/pokemon
"""

'''
# Benchmark 1 (No.1): Retrieve a remote data file by URL
The code belowed is how we grab dataset using API. 
Hoever, since api key will be expired weekly, I decide to use local file

## Get URL from Kaggles
url='https://storage.googleapis.com/kagglesdsdata/datasets/121/280/Pokemon.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20211026%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20211026T195458Z&X-Goog-Expires=259199&X-Goog-SignedHeaders=host&X-Goog-Signature=8e0e61b48d8276d0d4c5794acfbd64793f0c21e89457f700932d288534cb6849c508d4681ec8308f4e6a8c0d95d50f4c9b9b369c704064c59d5910b3d76ffe705270944af5aa2fb798c453b0545ca77c5df5f631606725184663f149cd1959457fa3831dc13dd463c3413e60bf15418b3c28561fc216c1a2399d82008f46dee8ac3617203b11b78c5b29856e86c3b0d7558e8f1ec831c9c1e679f21bf9a1f44049ff311712171756861bf1c0ac1392d6b628a5a9387c616bec162da97e9396f8d8bc0529c55530c8e5d9c65c01dd8f4d768720b90cbed0a5d5e93679e165fb00717f787e48ae7210f1c19abc6f7e2636ad2a9f08655c5ed8c2a20215df8818bd'
try:
    response = requests.get(url)
    pokemon = pd.read_csv(url,index_col = 0)
except requests.exceptions.HTTPError as e:
    print('The api is expired. We may swtich to grab the path from the local folder')
    url='./Pokemon.csv'
'''

# Benchmark 1: Retrieve a local file
location='Pokemon.csv'
## Use pandas package to read a csv file
try:
    pokemon = pd.read_csv(location,index_col = 0)
    print(pokemon)
except FileNotFoundError as e:
    print("Did you download the csv file?")
    exit(1)


# Benchmark 5: Generate a brief summary of the data file
## number of records for each pokemon using iteration
num_records= 0
for col in pokemon:
    num_records+=1
print("For each pokemon, we have", num_records, "data")
## number of rows
print("Number of rows: ", len(pokemon))
## The difference between the number of rows and the number of pokemons 
## is caused by mega evolution of a pokemon.
## e.g. Vanusaur and VanusaurMaga are the same pokemon, but have different data.

# Benchmark 3: Modify the number of columns from the source to the dest
## Now, I am going to create a table that only contains information below:
## Name: pokemon's name
## Type 1: type/category of a pokemon
## Type 2: another type/category of a pokemon
## Total: sum of all stats of a pokemon, which determines strength
## (I will also rename "Total" to "Strength")
modifiedPokemon = pd.read_csv(location,index_col = 0)
list_col_names=[]
for col_name in pokemon:
    list_col_names.append(col_name)
for curr_col in list_col_names:
    if(not (curr_col=='Name' or curr_col=='Type 1' or curr_col=='Type 2' or curr_col=='Total')):
        modifiedPokemon.drop(curr_col, inplace=True, axis=1)
modifiedPokemon.rename(columns={'Name':'Name of Pokemon','Type 1':'Type 1','Type 2':'Type 2', 'Total': 'Strength'},inplace=True)
modifiedPokemon.dropna(axis=0, subset=['Strength'])
print(modifiedPokemon)

# Benchmark 2: Convert the general format and data structure of the data source
## Convert the modified pokemon file from CSV to TSV
modifiedPokemon.to_csv('./TSVpokemon.tsv', index = False, sep='\t')
## Convert the newly-created tsv file to csv file
sourceFile='./TSVpokemon.tsv'
destFile=pd.read_table(sourceFile,sep='\t')
destFile.to_csv('./CSVpokemon.csv',index=False)
## Convert the newly-created csv file to json file
srcFile='./CSVpokemon.csv'
jsonFile='./JSONpokemon.json'
modifedSrcFile='./CSVpokemonGrass.csv'
data={}
with open(srcFile) as csvf:
    csvReader=csv.DictReader(csvf)
    for rows in csvReader:
        key = rows['Name of Pokemon']
        data[key]=rows
with open(jsonFile,'w') as jsonf:
    jsonf.write(json.dumps(data,indent=4))

#Pattern Match
## Find all pokemons whose name end with character z
pattern='.*z$'
endZ=[]
with open('./Pokemon.csv','r') as findf:
    reader=csv.reader(findf)
    for rows in reader:
        key = rows[1]
        key=re.escape(key)
        if re.match(pattern,key):
            endZ.append(key)
print("\nPokemons whose name end with 'z': ", endZ, "\n")

# Extra Function
# Purpose: Pattern Match and Error Message
# Description: This function takes a text file path as an input,
# and it checks if the text file contains only email addresses.
# Each address has to be listed as a single line in the text file

inputDir=''
## Pattern of an email address
emailPattern = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  
try:
    ## Get a filename in the same directory
    inputDir=input("Please input the directory of a txt file that contains a list of email addresses: ")
    ## Check if the file ends with txt
    if not inputDir.endswith('.txt'):
        print('Your input file is not a txt file')
    elif os.path.getsize(inputDir)==0:
        print('Your text file is empty')
    else:
        try:
            with open(inputDir,'r') as txtf:
                line=txtf.readline()
                if not re.match(emailPattern,line):
                    print('Your text file contains something other than email address: ', line)
                    exit(1)
        except os.error as e:
            print(e)
            exit(1)
        finally:
            txtf.close()
        print('Your input text file has been checked')
            
except EOFError as e: ## If the input is not a string
    print("Oops, you did not input a valid directory")
except FileNotFoundError as e2:
    print('The system cannot find the file')