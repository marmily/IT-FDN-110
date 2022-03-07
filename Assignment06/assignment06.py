#------------------------------------------#
# Title: Assignment06_Starter.py
# Desc: Working with classes and functions.
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# EMartin, 2022-Mar-06, Streamlined code by moving logic into functions
#------------------------------------------#

# -- DATA -- #
strChoice = '' # User input
lstTbl = []  # list of lists to hold data
dicRow = {}  # list of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object


# -- PROCESSING -- #
class DataProcessor:
    """Processing the data for CD addition and deletion"""
    @staticmethod
    def add_cd(cd_id, cd_title, artist_name, table):
        """
        Function to manage addition of CD data to a list of dictionaries.

        Takes in CD ID, CD Title, and CD artist data, constructs a dictionary, and appends that dictionary
        to the provided table.

        Args:
            cd_id (integer): integer denoting the CD ID number
            cd_title (string): string denoting CD title
            artist_name (string): string denoting CD artist name
            table (list): 2D data structure (list of dicts) that holds the data during runtime
        Returns:
            table (list): 2D data structure (list of dicts) that holds the data during runtime
        """
        dicRow = {'ID': cd_id, 'Title': cd_title, 'Artist': artist_name}
        table.append(dicRow)
        return table
        
    @staticmethod
    def delete_cd(cd_id, table):
        """
        Function to manage deletion of CD data from a list of dictionaries.

        Takes in CD ID and table, locates the corresponding dictionary, and deletes that dictionary from 
        the provided table.

        Args:
            cd_id (integer): integer denoting the CD ID number
            table (list): 2D data structure (list of dicts) that holds the data during runtime
        Returns:
            table (list): 2D data structure (list of dicts) that holds the data during runtime
            blnCDRemoved (boolean): flag that indicated whether the CD was located in the table and subsequently
            deleted
        """
        intRowNr = -1
        blnCDRemoved = False
        for row in table:
            intRowNr += 1
            if row['ID'] == cd_id:
                del table[intRowNr]
                blnCDRemoved = True
                break
        return table, blnCDRemoved
    
class FileProcessor:
    """Processing the data to and from text file"""
    @staticmethod
    def read_file(file_name, table):
        """
        Function to manage data ingestion from file to a list of dictionaries.

        Reads the data from file identified by file_name into a 2D table
        (list of dicts) table one line in the file represents one dictionary row in table.

        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime
        Returns:
            None
        """
        table.clear()  # this clears existing data and allows to load data from file
        objFile = open(file_name, 'r')
        for line in objFile:
            data = line.strip().split(',')
            dicRow = {'ID': int(data[0]), 'Title': data[1], 'Artist': data[2]}
            table.append(dicRow)
        objFile.close()

    @staticmethod
    def write_file(file_name, table):
        """
        Function to manage data writing to file to a list of dictionaries.

        Writes the data from file identified by file_name from a 2D table.

        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime
        Returns:
            None
        """
        objFile = open(file_name, 'w')
        for row in table:
            lstValues = list(row.values())
            lstValues[0] = str(lstValues[0])
            objFile.write(','.join(lstValues) + '\n')
        objFile.close()

# -- PRESENTATION (Input/Output) -- #

class IO:
    """Handling Input / Output"""
    @staticmethod
    def print_menu():
        """
        Displays a menu of choices to the user

        Args:
            None
        Returns:
            None
        """
        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit\n')

    @staticmethod
    def menu_choice():
        """
        Gets user input for menu selection

        Args:
            None
        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x
        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(table):
        """
        Displays current inventory table

        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime
        Returns:
            None
        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print('{}\t{} (by: {})'.format(*row.values()))
        print('======================================')
        
    @staticmethod
    def add_cd_input():
        """
        Function to manage data ingestion from user to create CD dictionary entries.
        
        Prompts user to input the CD ID, CD title, and CD artist name, and assigns that input to variables.
        Args:
            None
        Returns:
            cd_id (integer): integer denoting the CD ID number
            cd_title (string): string denoting CD title
            artist_name (string): string denoting CD artist name
        """
        cd_id = input('Enter ID: ').strip()
        cd_title = input('What is the CD\'s title? ').strip()
        artist_name = input('What is the Artist\'s name? ').strip()
        cd_id = int(cd_id)
        return cd_id, cd_title, artist_name
    
    @staticmethod
    def check_if_cd_removed(blnCDRemoved):
        """
        Function to manage data deletion from the list of dictionaries.
        
        Checks if the CD entry was successfully located and removed from the list of CDs.
        
        Args:
            blnCDRemoved (boolean): flag that indicated whether the CD was located in the table and subsequently
            deleted
        Returns:
            None.
        """
        if blnCDRemoved:
            print('The CD was removed')
        else:
            print('Could not find this CD!')
            
    @staticmethod
    def load_inventory_prompt():
        """
        Function to manage data loading from file to memory.
        
        Reminds user that loading CD data will overwrite data in memory, and accepts input confirming or
        exiting the load process.
        
        Args:
            None
        Returns:
            strYesNo (string): string denoting user's preference to confirm or exit load process
        """
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled: ')
        return strYesNo
        
# 1. When program starts, read in the currently saved Inventory
FileProcessor.read_file(strFileName, lstTbl)

# 2. start main loop
while True:
    # 2.1 Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()

    # 3. Process menu selection
    # 3.1 process exit first
    if strChoice == 'x':
        break
    # 3.2 process load inventory
    if strChoice == 'l':
        strYesNo = IO.load_inventory_prompt()
        if strYesNo.lower() == 'yes':
            print('reloading...')
            FileProcessor.read_file(strFileName, lstTbl)
            IO.show_inventory(lstTbl)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.3 process add a CD
    elif strChoice == 'a':
        # 3.3.1 Ask user for new ID, CD Title and Artist
        intID, strTitle, strArtist = IO.add_cd_input()
        # 3.3.2 Add item to the table
        lstTbl = DataProcessor.add_cd(intID, strTitle, strArtist, lstTbl)
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.4 process display current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.5 process delete a CD
    elif strChoice == 'd':
        # 3.5.1 get Userinput for which CD to delete
        # 3.5.1.1 display Inventory to user
        IO.show_inventory(lstTbl)
        # 3.5.1.2 ask user which ID to remove
        intIDDel = int(input('Which ID would you like to delete? ').strip())
        # 3.5.2 search thru table and delete CD
        lstTbl, blnCDRemoved = DataProcessor.delete_cd(intIDDel, lstTbl)
        IO.check_if_cd_removed(blnCDRemoved)
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.6 process save inventory to file
    elif strChoice == 's':
        # 3.6.1 Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstTbl)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # 3.6.2 Process choice
        if strYesNo == 'y':
            # 3.6.2.1 save data
            FileProcessor.write_file(strFileName, lstTbl)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    # 3.7 catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else:
        print('General Error')




