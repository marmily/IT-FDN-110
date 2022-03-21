#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# EMartin, 2022-Mar-20, added code to complete assignment 08
#------------------------------------------#

import pickle

# -- DATA -- #
strFileName = 'cdInventory.pkl'


class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:
        __init__(self, cd_id, cd_title, cd_artist): constructor for this class
        __repr__(self): returns string representation of a class object
    """
    def __init__(self, cd_id, cd_title, cd_artist):
        """
        Constructor for this class.
    
        Args:
           cd_id: (int) with CD ID
           cd_title: (string) with the title of the CD
           cd_artist: (string) with the artist of the CD
        Returns:
            CD object
        """
        self.cd_id = cd_id
        self.cd_title = cd_title
        self.cd_artist = cd_artist
        
    def __repr__(self):
        """
        Returns string representation of a class object
    
        Args:
            None
        Returns:
            string representation of a class object.
        """
        return f"CD ID: {self.cd_id}\nCD Title: {self.cd_title}\nArtist Name: {self.cd_artist}"


# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file.

    methods:
        read_file(file_name): -> None
        write_file(file_name, cd_inventory): -> an Inventory object
    """
    @staticmethod
    def read_file(file_name):
        """
        Function to manage data ingestion from file to an Inventory object.

        Unpickles and reads the data from file identified by file_name.

        Args:
            file_name (string): name of pickle file used to read the data from
        Returns:
            cd_inventory: an Inventory object
        """
        cd_inventory = Inventory()
        try:
            with open(file_name, 'rb') as readPickleFile:
                cd_inventory = pickle.load(readPickleFile)
        except FileNotFoundError:
            print(f"{file_name} not located. Continuing...\n")
        except Exception:
            print(f"Exception ocurred when attempting to read {file_name}.")
        return cd_inventory

    @staticmethod
    def write_file(file_name, cd_inventory):
        """
        Function to manage data writing to file to a list of dictionaries.
    
        Pickles and writes the binary data to file identified by file_name.
    
        Args:
            file_name (string): name of pickle file used to read the data from
            cd_inventory: an Inventory object
        Returns:
            None
        """
        try:
            with open(file_name, 'wb') as writePickleFile:
                pickle.dump(cd_inventory, writePickleFile)
        except Exception:
            print(f"Exception ocurred when attempting to write {file_name}.")


# -- PRESENTATION (Input/Output) -- #
class IO:
    """Handling Input / Output

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:
        print_menu(): Displays a menu of choices to the user
        menu_choice(): Gets user input for menu selection
        show_inventory(cd_inventory): Displays an Inventory object
        add_cd_input(): Function to manage data ingestion from user to create CD entries.
        load_inventory_prompt(): Function to manage data loading from file to memory.
        delete_cd_prompt(): Function to manage IO for deleting a CD from inventory.
    """
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
            # Because input always returns a string, and the input function guarantees that this is always possible, no error handling needed here
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(cd_inventory):
        """
        Displays current inventory

        Args:
            cd_inventory: an Inventory object
        Returns:
            None
        """
        print(cd_inventory)
        
    @staticmethod
    def add_cd_input():
        """
        Function to manage data ingestion from user to create CD entries.
        
        Prompts user to input the CD ID, CD title, and CD artist name, and assigns that input to variables.
        Args:
            None
        Returns:
            cd_id (integer): integer denoting the CD ID number
            cd_title (string): string denoting CD title
            artist_name (string): string denoting CD artist name
        """
        cd_id = None
        while cd_id is None:
            try:
                cd_id = int(input('Enter ID: ').strip())
            except ValueError:
                print("Please enter a valid integer for CD ID.")
                continue
            except:
                print("Exception ocurred when attempting to enter a CD ID.")
                continue
        cd_title = input('What is the CD\'s title? ').strip()
        artist_name = input('What is the Artist\'s name? ').strip()
        return cd_id, cd_title, artist_name
            
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
        # Because input always returns a string, and the input function guarantees that this is always possible, no error handling needed here.
        strYesNo = input('type \'yes\' to continue and reload from file. Otherwise reload will be canceled: ')
        return strYesNo
    
    @staticmethod
    def delete_cd_prompt():
        """
        Function to manage IO for deleting a CD from inventory.
        
        Reminds user that a valid integer is needed in order to locate a CD in the CD inventory.
        
        Args:
            None
        Returns:
           cd_id (int): int denoting user input from IO prompt
        """
        cd_id = None
        while cd_id is None:
            try:
                cd_id = int(input('Which ID would you like to delete? ').strip())
            except ValueError:
                print("Please choose a valid CD ID to delete.")
                continue
            except Exception:
                print("Exception ocurred when attempting to retrieve CD ID for deletion.")
        return cd_id


class Inventory:
    """Managing CD Inventory:

    properties:
        cd_inventory (list): 
    methods:
       __init__(self): Constructor for this class.
       add_cd(self, cd_id, cd_title, cd_artist): Function to manage addition of CD data to an Inventory object.
       delete_cd(self, cd_id): Function to manage deletion of CD data from an Inventory object.
       __repr__(self): Returns string representation of a class object
    """
    def __init__(self):
        """
        Constructor for this class.
        
        Args:
            None
        Returns:
            Inventory object
        """
        self.cd_inventory = []
    
    def add_cd(self, cd_id, cd_title, cd_artist):
        """
        Function to manage addition of CD data to an Inventory object.
        
        Args:
            cd_id: (int) with CD ID
            cd_title: (string) with the title of the CD
            cd_artist: (string) with the artist of the CD
         Returns:
             None
        """
        new_cd = CD(cd_id, cd_title, cd_artist)
        self.cd_inventory.append(new_cd)
    
    def delete_cd(self, cd_id):
        """
        Function to manage deletion of CD data from an Inventory object.
        
        Args:
            cd_id: (int) with CD ID
         Returns:
            Bool: Indicates if CD was successfully deleted. 
        """
        counter = -1
        for cd in self.cd_inventory:
            counter += 1
            if cd.cd_id == cd_id:
                del self.cd_inventory[counter]
                return True
        return False
    
    def __repr__(self):
        """
        Returns string representation of a class object
    
        Args:
            None
        Returns:
            A string representation of an Inventory obejct
        """
        representation = ""
        for cd in self.cd_inventory:
            representation += f'CD ID: {cd.cd_id}\n'
            representation += f'CD Title: {cd.cd_title}\n'
            representation += f'Artist Name: {cd.cd_artist}\n'
        return representation

    
# -- Main Body of Script -- #
cd_inventory = FileIO.read_file(strFileName)

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
            cd_inventory = FileIO.read_file(strFileName)
            IO.show_inventory(cd_inventory)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(cd_inventory)
        continue  # start loop back at top.
    # 3.3 process add a CD
    elif strChoice == 'a':
        # 3.3.1 Ask user for new ID, CD Title and Artist
        cd_id, cd_title, artist_name = IO.add_cd_input()
        # 3.3.2 Add CD to Inventory
        cd_inventory.add_cd(cd_id, cd_title, artist_name)
        IO.show_inventory(cd_inventory)
        continue  # start loop back at top.
    # 3.4 process display current inventory
    elif strChoice == 'i':
        IO.show_inventory(cd_inventory)
        continue  # start loop back at top.
    # 3.5 process delete a CD
    elif strChoice == 'd':
        # 3.5.1 get Userinput for which CD to delete
        # 3.5.1.1 display Inventory to user
        IO.show_inventory(cd_inventory)
        # 3.5.1.2 ask user which ID to remove
        cd_id = IO.delete_cd_prompt()
        # 3.5.2 search thru Inventory and delete CD
        was_deleted = cd_inventory.delete_cd(cd_id)
        if was_deleted:
            IO.show_inventory(cd_inventory)
        else:
            print("CD not found!")
        continue  # start loop back at top.
    # 3.6 process save inventory to file
    elif strChoice == 's':
        # 3.6.1 Display current inventory and ask user for confirmation to save
        IO.show_inventory(cd_inventory)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # 3.6.2 Process choice
        if strYesNo == 'y':
            # 3.6.2.1 save data
            FileIO.write_file(strFileName, cd_inventory)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    # 3.7 catch-all should not be possible, as user choice gets vetted in IO, but to be safe:
    else:
        print('General Error')