# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# JPlemons,6.4.2020,Modified code to complete assignment 8
# JPlemons,6.5.2020,Filling out classes
# JPlemons,6.6.2020,Filling out Main Body
# JPlemons,6.7.2020,Figuring out bugs and completing assignment
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []
list_of_product_price = []
strStatus = ""
strChoice = ""


class Product(object):
    """Stores data about a product:

    properties:
        product_name: (string) with the products's name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        JPlemons,6.5.2020,Modified code to complete assignment 8

    """

    def __init__(self, product_name, product_price):
        self.__product_name = product_name
        self.__product_price = product_price

    @property
    def product_name(self):  # getter or accessor
        return str(self.__product_name)

    @product_name.setter  # setter or mutator
    def product_name(self, value):
        if not str(value).isnumeric():
            self.__product_name = value
        else:
            raise Exception("Please save your numbers for the value line and use letters for the name.")

    @property
    def product_price(self):  # getter or accessor
        return float(self.__product_price)

    @product_price.setter  # setter or mutator
    def product_price(self, value):
        if float(value).isnumeric() == True:
            self.__product_price = value
        else:
            raise Exception("Letters aren't numbers.  Please only use numbers for prices.")


# End Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):
        read_data_from_file(file_name): -> (a list of product objects)
        add_data_to_list(product_name, product_price, list_of_product_price)
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        JPlemons,6.5.2020,Modified code to complete assignment 8
    """

    @staticmethod
    def read_data_from_file(strFileName, list_of_product_price):
        """ Reads data from a file into a list of dictionary rows
        :param strFileName: (string) with name of file:
        :param list_of_products: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        list_of_product_price.clear()  # clear current data
        file = open(strFileName, "r")
        for line in file:
            product_name, product_price = line.split(",")
            row = {"Product": product_name.strip(), "Price": product_price.strip()}
            list_of_product_price.append(row)
        file.close()
        return list_of_product_price,  # confirmation to user

    @staticmethod
    def save_data_to_file(strFileName, list_of_product_price):
        """ Saves the list of products to text file
        :param strFileName: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        file = open(strFileName, "w")  # w to write vs. a for append
        for row in list_of_product_price:
            file.write(f"{row['Product']},{str(row['Price'])}\n")
        file.close()
        return list_of_product_price

    @staticmethod
    def add_data_to_list(product_name, product_price, list_of_product_price):
        """ Adds a task to the list of dictionary rows
        :param product_name: (string) name of task to be completed
        :param product_price: (string)
        :param list_of_products: (list) you want filled with file data
        :return: (list) of dictionary rows
        """
        row = {"Product": product_name, "Price": product_price}
        list_of_product_price.append(row)
        return list_of_product_price,


# End Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """
    Input Data from the user

    Methods:
        print_menu_Tasks()
        input_menu_choice()
        print_current_products_in_list(list_of_product_price)
        input_new_product_and_price()
        input_yes_no_choice(message)
        input_press_to_continue(optional_message='')
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        JPlemons,6.5.2020,Modified code to complete assignment 8
    """

    @staticmethod
    def print_menu_Tasks():
        """  Display a menu of choices to the user
        :return: nothing
        """
        print('''
    ****** Menu of Options *******
          1) Show Products
           2) Add Product
            3) Save File       
             4)  Exit
    ******************************
            ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user
        :return: string
        """
        choice = input("Which option would you like to perform? [1 - 4] - ").strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_products_in_list(list_of_product_price):
        """ Shows the current Tasks in the list of dictionaries rows
        :param list_of_products: (list) of rows you want to display
        :return: nothing
        """
        print("\n********* List *********")
        print("Product --- Price")
        print("-------------------")
        for row in list_of_product_price:
            print(f"{row['Product']} --- ${row['Price']}")
        print("************************")

    @staticmethod
    def input_new_product_and_price():
        """ Gets the product and price from user
        :return: product and price
        """
        Product.product_name = input("What is the name of product? ")
        Product.product_price = input("What is the price? ")

        return Product.product_name, Product.product_price


    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user
        :return: string
        """
        return str(input(message)).strip().lower()

    @staticmethod
    #  to create a pause in the program for the user to control
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing
        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')


# End Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of product objects when script starts
# Show user a menu of options
# Get user's menu option choice
# Show user current data in the list of product objects
# Let user add data to the list of product objects
# let user save current data to file and exit program

# Main Body of Script  ---------------------------------------------------- #
FileProcessor.read_data_from_file(strFileName, list_of_product_price)

while True:
    IO.print_menu_Tasks()
    strChoice = IO.input_menu_choice()

    if strChoice.strip() == "1":
        IO.print_current_products_in_list(list_of_product_price)
        IO.input_press_to_continue(strStatus)
    elif strChoice.strip() == "2":
        IO.input_new_product_and_price()
        FileProcessor.add_data_to_list(Product.product_name, Product.product_price, list_of_product_price)
    elif strChoice.strip() == "3":
        FileProcessor.save_data_to_file(strFileName, list_of_product_price)
        print("Products and Prices have been saved.")
    elif strChoice.strip() == "4":
        strChoice = IO.input_yes_no_choice("Any unsaved information will be lost.  Do you want to Exit? (y/n)? ")
        if strChoice.lower() == "y":
            print("\nExiting Program...")
            break
        else:
            print("\nReturning to Program...")
            continue
    else:
        print("Please choose 1-4.")  # if anything other than 4 was entered.
