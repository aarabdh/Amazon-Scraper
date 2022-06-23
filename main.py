import AmazonScraper
import csv
searchterm = "insert search term here"
numofpages = 2  # Number of pages you wish to scrape 
searchterm = searchterm.replace(" ", "+")
a = AmazonScraper.main(searchterm, numofpages)  # executing the script

# writing the data into the file
file = open('output.csv', 'w', newline='')
with file:
    write = csv.writer(file)
    write.writerows(a)
