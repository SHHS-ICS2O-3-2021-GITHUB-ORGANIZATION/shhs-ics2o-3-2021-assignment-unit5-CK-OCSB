# NAME OF AUTHOR:  Carter King (CK-OCSB)
# NAME OF THE PROGRAM: Q3WordTriangles  
# DATE OF CREATION:  2022-01-26
# PURPOSE OF PROGRAM:  to print they user word as a triangle
# INPUT
UserWord = input("Please enter the word  wou would like to be pyrimidifyed: ")
# VARIABLE DEFINITION
WordNumb = (len(UserWord))
# PROCESSING
for i in range (0,WordNumb +1):
  print(UserWord[:i:])
# OUTPUT