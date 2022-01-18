'''Author: Aditya Wiwekananda'''


#Import csv module
import csv

#Function will display vehicle inventory
def displayInventory():
    with open('CarInventory.csv') as csvfile:

        #Take all info from csv and store as dictionary
        d_reader = csv.DictReader(csvfile)

        #print all car information
        for car in d_reader:

            #Print each type of information
            for key,value in car.items():
                #If the key is retail price, make sure that the value has a '$' sign
                if key == 'Retail Price':
                    print(key,': $'+value)
                else:
                    print(key,":",value)
            print("---------------------------")

#Function to add new vehicle to Inventory
def addInventory():
    with open('CarInventory.csv', 'r+',) as csvfile:
        fieldnames = ["Dealer Inventory Number","Auto VIN", "Make", "Model", "Exterior Color", "Interior Color", "Transmission Type", "Retail Price"]

        #Take all info from csv and store as dictionary
        writeInventory = csv.DictWriter(csvfile, fieldnames=fieldnames)

        #Ask user to enter information
        inventoryNum = int(input("Enter the dealer inventory number: "))
        #User must enter an inventory number greater than 1000
        while inventoryNum<1000 or inventoryNum>9999:
            print("****Error - Invalid Entry. Dealer inventory numbers must begin at 1000 and be four-digits****")
            inventoryNum = int(input("Enter the dealer inventory number: "))

        vinNum = input("Enter Auto VIN: ")
        #User must enter a five digit VIN number
        while len(vinNum)!=5:
            print("****Error - Invalid Entry. Auto Vehicle Information Number (VIN) must be five-digits****")
            vinNum = input("Enter Auto VIN: ")

        make = input("Enter Make: ")
        model = input("Enter Model: ")
        extColor = input("Enter Exterior Color: ")
        intColor = input("Enter Interior Color: ")
        transmission = input("Enter Transmission Type: ")
        price = input("Enter Retail price: ")

        #Reset Cursor
        csvfile.seek(0,2)

        #Add all the information to the CSV file
        writeInventory.writerow({'Dealer Inventory Number': inventoryNum, 'Auto VIN': vinNum, 'Make': make, 'Model': model, 'Exterior Color': extColor, 'Interior Color':intColor,"Transmission Type":transmission,"Retail Price":price})
        print("")

#This function will be able to find a vehicle based on an entered number
def searchInventory():
    edit = 0
    with open('CarInventory.csv', 'r+') as csvfile:
        csvfile.seek(0,0)
        searchInv = csv.reader(csvfile)


        searchVehicle = input("Please enter the dealer inventory number: ")
        #This variable will store the index of the car that the matches the entered number
        foundRow = 0

        #
        for index,row in enumerate(searchInv):
            while True:
                try:
                    if row[0]==searchVehicle:
                        foundRow=index
                        print("Vehicle found!")
                        print("________________")
                        print("Dealer Inventory Number:",row[0])
                        print("Auto VIN:",row[1])
                        print("Make:",row[2])
                        print("Model:",row[3])
                        print("Exterior Color:",row[4])
                        print("Interior Color:",row[5])
                        print("Transmission Type:",row[6])
                        print("Retail Price: $"+str(row[7]))
                        print(foundRow)

                #Break loop once done
                except IndexError:
                    break
                else:
                    break
        #Tell user that no vehicle was found
        if foundRow==0:
            print("No vehicle found!")

        else:
            #Ask user if they want to edit that cars info
            while True:
                try:
                    edit = int(input("Enter 1 if you would like to edit that car's information. Enter 2 if you want to keep the information: "))
                except ValueError:
                    print("Please enter an integer.\n")
                else:
                    break

            if edit == 1:
                csvfile.seek(0,0)
                #Get car lists
                editList=[]
                for row in searchInv:
                    editList.append(row)


                editList[foundRow][0] = input("Enter Dealership Number: ")
                editList[foundRow][1] = input("Enter the AUTO VIN: ")
                editList[foundRow][2] = input("Enter Make: ")
                editList[foundRow][3] = input("Enter Model: ")
                editList[foundRow][4] = input("Enter Exterior Color: ")
                editList[foundRow][5] = input("Enter Interior Color: ")
                editList[foundRow][6] = input("Enter Transmission Type: ")
                editList[foundRow][7] = input("Enter Retail price: ")
                print(editList)

                #remove empty lists from 2d list
                overwriteList = [x for x in editList if x != []]
                print(overwriteList)

        # ***THIS PART WILL ERASE THE CSV FILE ***
        if edit == 1:

            with open('CarInventory.csv', 'w') as csvfile:
                newInv = csv.writer(csvfile)

                newInv.writerows(overwriteList)






"""MAIN"""
print("Welcome to the Dealership car inventory program.")
run = True
while run == True:
    print("""Please choose from the following options
1) Enter new vehicle into inventory
2) Display vehicle inventory
3) Search for vehicle (by inventory number)
4) Exit the program
""")

    selection = None

    while selection not in ["1", "2", "3", "4"]:
        selection = input("Selection: ")
        print("")

    #If user chooses to enter new vehicle
    if selection == "1":
        print("*Enter new vehicle into inventory*")
        addInventory()
        print("*Car has been added into inventory*")

    #If user chooses to vehicle inventory
    elif selection == "2":
        print("*Display vehicle inventory*")
        displayInventory()

    #If user chooses to search for a vehicle
    elif selection == "3":
        print("*Search for vehicle (by inventory number)*")
        searchInventory()

    #End the program if they choose elsewise
    else:
        print("Thank you for running the car inventory program! Come again soon!")
        run = False
