# My Second Python Program

# Understanding Output & Input in Python

import sys
import io

print("\n------ Sample Application Form -----\n");

FirstName=raw_input ("\nPlease provide your first name ");

# Probable Error : Because of Using "input" instead of "raw_input"

# Traceback (most recent call last) : 
# File "D:\GitHub-Projects\Python\PythonExperiments\samplepythonexperiments\SamplePythonCodes\SamplePythonCodes\SecondPythonProgram.py", 
# line 10, in <module> NameError: name 'AJINKYA' is not defined

# Solution : http://stackoverflow.com/questions/29124380/file-string-line-1-in-module-nameerror-name-san-is-not-defined

LastName=raw_input("\nPlease provide your last name ");

Age=raw_input("\nPlease provide your age ");

print("\nThank You " + FirstName + " " + LastName + ", for informing us your age - which is " + Age + ".")

print("\n---------------- End ------------------\n")
 