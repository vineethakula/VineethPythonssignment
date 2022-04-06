import csv

from py import code

 

def test_exercise2():

    with open(r"../payloads/IM/test.log", encoding="ISO-8859-1") as f, open ('../payloads/IM/test.csv', 'w' ) as f2: # or 'wb' if on python2

        writer = csv.writer(f2)

        writer.writerow([])

        i = 0

        for line in f:

            writer.writerow(line.rstrip().split('|'))

            fieldnames = ['response code']

            i += 1

            if i == 10000:

                break      

    with open ('../payloads/IM/test.csv', newline='', mode='r') as csv_file:

        line = csv_file.readline()

        for row in csv_file:

            first_item = row.split(',')

            if (len(first_item) > 1):

                if (first_item[3] != '200'):

                    print(first_item[2:5])

 

test_exercise2()
