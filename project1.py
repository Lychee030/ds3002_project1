import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt
# import seaborn as sns
import requests

"""
The dataset named "Pokemon with stats" is useful for Pokemon lovers and Pokemon games players.
It contains detailed information including name, type, HP, speed of 721 Pokemon.
The data table is expressed in a csv file. All data are acquired from official websites such as pokemon.com

Information of this dataset
Name: Pokemon with stats
Author: Alberto Barradas
Where: Kaggle
URL:https://www.kaggle.com/abcsds/pokemon
"""

# Benchmark 1 (No.1): Retrieve a remote data file by URL
## Get URL from Kaggles
url='https://storage.googleapis.com/kagglesdsdata/datasets/121/280/Pokemon.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20211022%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20211022T134612Z&X-Goog-Expires=259199&X-Goog-SignedHeaders=host&X-Goog-Signature=5055adae3ae6cead8ed25092e1c41ccc6ed60d5abbbbe298ae68d20b0f741594cef860c5b24595c2b1117b0c888474902bb1d9a67bbb28ed9538217fe0837f30eaf39527466251370dce6194b2cee03e0e9d6ed2c326c0180dba555870acf07d948314266d4cd6caf31904da7f1d135a1e132cea9ee740c0788fc6a2253d7c89a095c1e26f09b89b340a467078aaccc9214f20af1502410ae97a7a065b4ea77fccb200bc8c597b098bd52d7cc823c562c1375dc978bec5c76fa7993c29d19cc20dc95f95e1e3c93ab09d435ea6db8053a2bd6d1e653e6b2ec39a8608d60d0a80dfb5dac043f14e737bb148b5ea409ab7fec26d724e64fd373441f7ae4c1f20e3'
response = requests.get(url)
## Use pandas package to read a csv file
pokemon = pd.read_csv(url,index_col = 0)
print(pokemon)

# Benchmark 2 (No.5): Generate a brief summary of the data file
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

# Benchmark 3 (No.3): Modify the number of columns from the source to the dest
## Now, I am going to create a table that only contains information below:
## Name: pokemon's name
## Type 1: type/category of a pokemon
## Type 2: another type/category of a pokemon
## Total: sum of all stats of a pokemon, which determines strength
## (I will also rename "Total" to "Strength")
modifiedPokemon = pd.read_csv(url,index_col = 0)
list_col_names=[]
for col_name in pokemon:
    list_col_names.append(col_name)
for curr_col in list_col_names:
    if(not (curr_col=='Name' or curr_col=='Type 1' or curr_col=='Type 2' or curr_col=='Total')):
        modifiedPokemon.drop(curr_col, inplace=True, axis=1)
modifiedPokemon.rename(columns={'Name':'Name of Pokemon','Type 1':'Type 1','Type 2':'Type 2', 'Total': 'Strength'},inplace=True)
print(modifiedPokemon)
