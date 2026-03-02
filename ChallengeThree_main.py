import ChallengeThree_helper
#importing to display the else statement in the helper file, which will show us the value of __name__ in the importing file, and not in the helper file.

print("Main file now running after importing helper")

#This will show us the value of __name__ in the existing file. Everytime you run this in the existing file,it will show you "__main__" as the value of __name__, because you are running this file directly.
print("__name__ is:", __name__)

