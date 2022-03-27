#------------------------------------------#
# Title: CD_Inventory.py
# Desc: The CD Inventory App main Module
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# DBiesinger, 2030-Jan-02, Extended functionality to add tracks
# Emartin, 2022-March-27, added tracks
#------------------------------------------#

import ProcessingClasses as PC
import IOClasses as IO

lstFileNames = ['AlbumInventory.txt', 'TrackInventory.txt']
try:
    lstOfCDObjects = IO.FileIO.load_inventory(lstFileNames)
except Exception:
    lstOfCDObjects = []
    print(f'Failed to load Inventory from {lstFileNames}!')

while True:
    IO.ScreenIO.print_menu()
    strChoice = IO.ScreenIO.menu_choice()

    if strChoice == 'x':
        break
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            lstOfCDObjects = IO.FileIO.load_inventory(lstFileNames)
            IO.ScreenIO.show_inventory(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    elif strChoice == 'a':
        tplCdInfo = IO.ScreenIO.get_CD_info()
        PC.DataProcessor.add_CD(tplCdInfo, lstOfCDObjects)
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    elif strChoice == 'd':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    elif strChoice == 'c':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        cd_idx = input('Please enter the CD / Album ID: ')
        cd = PC.DataProcessor.select_cd(lstOfCDObjects, cd_idx)
        while True: 
            IO.ScreenIO.print_CD_menu() 
            user_choice = IO.ScreenIO.menu_CD_choice() 
            if user_choice == 'x': 
                break 
            if user_choice == 'a': 
                track_info = IO.ScreenIO.get_track_info() 
                PC.DataProcessor.add_track(track_info, cd) 
            elif user_choice == 'd': 
                IO.ScreenIO.show_tracks(cd) 
            elif user_choice == 'r': 
                IO.ScreenIO.show_tracks(cd) 
                track_id = input('Please enter the Track ID: ') 
                cd.rmv_track(track_id)
            else: 
                print(f'{user_choice} is not a valid input.')
    elif strChoice == 's':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        if strYesNo == 'y':
            IO.FileIO.save_inventory(lstFileNames, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    else:
        print('General Error')