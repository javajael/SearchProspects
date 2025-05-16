import csv
import os
# get directory to search
# get street to search on
streetNameToSearch = input("Enter The street you would like to search for: ")

# for now - open test file- #
#with open('testProspectList.csv', newline='') as csvfile:
#    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#    for row in spamreader:
#Imp        print(', '.join(row))
# form up list of files that we will search through (Prospect Lists)



is_in_file = False
filename_to_search = 'testProspectList.csv'
dir_to_search = '/Users/Jael/Documents/PY4E/Prospects'
files_to_search = os.listdir(dir_to_search)

def writeToResultFile(search_term, location_found):
    search_results_filename = 'results.csv'
    with open(search_results_filename, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow([search_term] + [location_found])

print(files_to_search)
for file_to_open in files_to_search:
    print(file_to_open)
    with open(file_to_open, 'rt') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            print(row[3])
            if streetNameToSearch.lower() in row[3].lower(): # if the street name occurs in the 4th column the row - street address - print out msg
                writeToResultFile(streetNameToSearch, file_to_open)

# do a compare - loop through existing spreadsheet, search for address match - 
# if there is an email or a ph # in the prospect list - save off the prospect list - OR form up the api call to the funnel


