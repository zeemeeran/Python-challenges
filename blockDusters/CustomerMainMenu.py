

# Python 3
# coding: utf-8
__author__ = "Per-Scholas Cohort-5"
__copyright__ = "Copyright 2022, Customer main menu"
__credits__ = ["Ricardo,Tim,Ammar,Zee,Bakal,Anju,Rupa"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "all creditors/github"
__email__ = "dev.malik.ammar@gmail.com"
__status__ = "Production"

import os, BlockDusterColors
from re import L, M
import customersDataManMod
import library

def MainMenu() :
    # Clear the terminal before starting the program so everything is clear
    #library.clearTerminal()

    print('''       
          )
        (  (              .^.
         \) )           .'.^.'.
          (/          .'.'---'.'.
         _\)_       .'.'-------'.'.
        (__)()    .'.'-,=======.-'.'.
        (_)__)  .'.'---|   |   |---'.'.
        (__)_),'.'-----|   |   |-----'.'.
        ()__.'.'-------|___|___|-------'.'.
        (_.'.'---------------------------'.'.
        .'.'-------------------------------'.'.
        """""|====..====.=======.====..====|"""""
        ()_)|    ||    |.-----.|    ||    |
        (_)_|    ||    ||     ||    ||    |
        (...|____||____||_____||____||____|
        (_)_(|----------| _____o|----------|
        (_)(_|----------||     ||----------|
        (__)(|----------||_____||----------|
        (_)(_|---------|"""""""""|---------|
        ()()(|--------|"""""""""""|--------|
    Zot-wWUwwuw|wwWWwuu|"""""""""""""|uwuwuuW|wuwwuuwu
    -------------- CUSTOMER INFORMAT4ION --------------
    ''')

    print(''' 
    ######################################################################
    #           CUSTOMER MENU - Choose one of the options from below     #
    ----------------------------------------------------------------------
    #    0-Search | 1-Add New | 2-Edit A Customer | 3-Delete | 4-Exit    #         
    ######################################################################
    ''')
    selection = 0
    while selection != "4" :
        selection=input(BlockDusterColors.colorFormat.CBLUE + "     Customer selection.......: " + BlockDusterColors.colorFormat.ENDC)
        if selection == '0' :
            customersDataManMod.searchCustomers()
            input()
            MainMenu()
        if selection == '1' :
            customersDataManMod.addCustomers()
            input()
            MainMenu()
        elif selection == '2' :
            customersDataManMod.editCustomers()
            input()
            MainMenu()
        elif selection == '3' :
            customersDataManMod.delCustomers()
            input()
            MainMenu()
        elif selection == '4' :
            library.clearTerminal()
            exit
        else :
            print("\nWarning - Invalid option\n")            


MainMenu()