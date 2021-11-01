# DS3002 Project1 By Emily Feng (ejf9kwf)
This repository is created for DS 3002 Project 1 only.

## Set up:
- Please make sure you have installed pandas, requests and re via pip.
- For your convinence, please clone testEmail package as well.
- CSVpokemon.csv, JSONpokemon.json, and TSVpokemon.tsv are not necessary because they will be created if you run project1.py
- Pokemon.csv is downloaded directly from Kaggle. 

## How it works:
Open a new terminal, run python project1.py<br />
- (1) The first output you will see is the non-modified table [800 rows x 12 columns] <br />
- (2) Then a brief summary () of the non-modified table is shown <br />
&nbsp; &nbsp; This summary includes:<br />
&nbsp; &nbsp; number of records for each pokemon<br />
&nbsp; &nbsp; number of rows<br />
&nbsp; &nbsp; (Notes: The difference between the number of rows and the number of pokemons is caused by mega evolution of a pokemon. For example, VanusaurMaga is the mega evolution of Vanusaur. But they have different data.)<br />
- (3) Then, a modified table is printed to the terminal. It consists of only 4 columns: <br />
&nbsp; &nbsp; Name: pokemon's name<br />
&nbsp; &nbsp; Type 1: type/category of a pokemon<br />
&nbsp; &nbsp; Type 2: another type/category of a pokemon<br />
&nbsp; &nbsp; Strength (Total): sum of all stats of a pokemon, which determines strength<br />
- (4) Later, the modified csv table will be converted to tsv file --> csv file --> json file. TSVpokemon.tsv, CSVpokemon.csv, and JSONpokemon.json will be created to this directory accordingly.<br />
- (5) Finally, there is an extra function that takes in a textfile as an input, and check if each file contains only a list of emails. The purpose of this function is to demonstrate my understanding of displaying error messages and applying pattern match for each line in a csv file. You can try 3 examples txt file in testEmail package. <br />
&nbsp; &nbsp; Address.txt contains a list of email addresses. <br />
&nbsp; &nbsp; emptyAddress.txt is an empty file. <br />
&nbsp; &nbsp; wrongAddress.txt has some random texts in it. <br />
