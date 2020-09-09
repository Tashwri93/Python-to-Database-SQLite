import wget

import csv


def download_dat_files():
    """Files downloaded via website"""
    url = 'https://raw.githubusercontent.com/jpatokal/openflights/master/data/airports.dat'
    wget.download(url, 'C:\sqlite3\Python Database files')

    url2 = 'https://raw.githubusercontent.com/jpatokal/openflights/master/data/airlines.dat'
    wget.download(url2, 'C:\sqlite3\Python Database files')

    url3 = 'https://raw.githubusercontent.com/jpatokal/openflights/master/data/routes.dat'
    wget.download(url3, 'C:\sqlite3\Python Database files')

    
def convert_files_to_csv():
    """Converting dat files to csv files"""

    filename = 'airports.dat'

    with open(filename, encoding ="utf8") as dat_file:
        with open('airports.csv','w', encoding ='utf8')as csv_file:
            for line in dat_file:
                csv_file.write(line)
                
    filename = 'airlines.dat'

    with open(filename, encoding ="utf8") as dat_file:
        with open('airlines.csv','w', encoding ='utf8')as csv_file:
            for line in dat_file:
                csv_file.write(line)

    filename = 'routes.dat'

    with open(filename, encoding ="utf8") as dat_file:
        with open('routes.csv','w', encoding ='utf8')as csv_file:
            for line in dat_file:
                csv_file.write(line)

download_dat_files()
convert_files_to_csv()

