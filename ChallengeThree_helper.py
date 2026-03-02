print("Helper file running")


#Using this if statement helps us run code in this file only when it is run directly, and NOT when it is imported as a module in another file.
#This is a common practice in Python to allow for code reuse and modularity.

if __name__ == "__main__":
    print("Helper is being run directly")
#else block will run when this file is imported as a module in another file, allowing us to see the value ONLY in the importing file, and not in this helper file.
else:
    print("__name__ of import file is:", __name__)
    #This will show us the file name of the importing file,  which would be ChallengeThree_main, because we are importing this helper file into the main file.
    print("Helper was imported")
    print()