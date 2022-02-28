#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# EMartin, 2022-Feb-27, Added logic to load from file and delete an entry
#------------------------------------------#

# Declare variables

strChoice = '' # User input
lstTbl = []  # list of dictionaries to hold data
dictRow = {}  # dictionary containing row of data
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # Exit the program if the user chooses so
        break
    if strChoice == 'l':
        #Add the functionality of loading existing data
        lstTbl = []
        objFile = open(strFileName, 'r')
        for row in objFile:
            tempRow = row.strip().split(',')
            dictRow = {
                        'id' : int(tempRow[0]), 
                        'title' : tempRow[1], 
                        'artist' : tempRow[2],
                      }
            lstTbl.append(dictRow)
        objFile.close()
    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # Add data to the table each time the user wants to add data
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        dictRow = {
                    'id' : intID, 
                    'title' : strTitle, 
                    'artist' : strArtist, 
                  }
        lstTbl.append(dictRow)
    elif strChoice == 'i':
        # Display the current data to the user each time the user wants to display the data
        print('ID, CD Title, Artist')
        for row in lstTbl:
            print(*row.values(), sep = ', ')
    elif strChoice == 'd':
        # Add functionality of deleting an entry
        indexCounter = 0
        idInput = int(input('Enter a CD ID: '))
        for row in lstTbl:
            if idInput == row['id']:
                del(lstTbl[indexCounter])
                break
            indexCounter += 1
        if idInput != row['id']:
                print("CD ID not found.")
    elif strChoice == 's':
        # Save the data to a text file CDInventory.txt if the user chooses so
        '''
        Changed to write from append to avoid data duplication when a user attempts to load from file then save to file, as well as data discrepancies between memory and
        CDInventory.txt when a user deletes an entry in memory. I envision CDInventory.txt as the source of truth for this invenetory, not memory.
        '''
        objFile = open(strFileName, 'w')
        for row in lstTbl:
            strRow = ''
            for item in row.values():
                strRow += str(item) + ','
            strRow = strRow[:-1] + '\n'
            objFile.write(strRow)
        objFile.close()
    else:
        print('Please choose either l, a, i, d, s or x!')