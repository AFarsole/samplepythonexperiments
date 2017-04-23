# The program to demostarte basic String Operations in Python

import sys;

FirstName=raw_input("First Name : \n");
LastName=raw_input("Last Name : \n");

# String Concate

FullName = FirstName + " " + LastName;
print("\nFull Name : " + FullName); 

# String UPPERCASE

UP_FirstName=FirstName.upper();
print("\nCapital First Name : " + UP_FirstName);
UP_LastName=LastName.upper();
print("\nCapital Last Name : " + UP_LastName);

# String LOWERCASE

LOW_FirstName=FirstName.lower();
print("\nLower First Name : " + LOW_FirstName);
LOW_LastName=LastName.lower();
print("\nLower Last Name : " + LOW_LastName);

print("\n");