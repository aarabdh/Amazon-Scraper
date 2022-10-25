import AmazonScraper
import csv
import os
import easygui

cur_dir = os.getcwd()

text = "Enter the following details"
title = "Amazon Scraper"
input_list = ["Search Term", "Pages to search through"]
output = easygui.multenterbox(text, title, input_list, ['', '2'])

searchterm = output[0]
numofpages = int(output[1])  # Number of pages you wish to scrape 
searchterm = searchterm.replace(" ", "+")
a = AmazonScraper.main(searchterm, numofpages)  # executing the script

# writing the data into the file
try:
    file = open(cur_dir + '\output\output.csv', 'w', newline='')
except:
    os.mkdir(cur_dir + '\output')
    file = open(cur_dir + '\output\output.csv', 'w', newline='')
with file:
    write = csv.writer(file)
    write.writerows(a)
