import csv
def AND(str1, str2):
    if(str1 == str2 or str1 == 'None'):
        return True
    return False

def pos_neg(str1):
    yes = ['yes','Yes','YES','1','y','Y']
    if str1 in yes:
        return True
    return False

filename = 'data.csv'


with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        n = len(row)

most_specific = ['None' for i in range(n)]

with open(filename, 'r') as csvfile2:
    parser = csv.reader(csvfile2)
    for row in parser:
        if(pos_neg(row[-1]) == True):
            for i in range(len(row) - 1):
                if(AND(most_specific[i], row[i]) == False):
                    most_specific[i] = "?"
                else:
                    most_specific[i] = row[i]

print(most_specific[:-1])
