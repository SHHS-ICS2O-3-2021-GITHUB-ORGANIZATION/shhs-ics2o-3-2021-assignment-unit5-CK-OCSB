# NAME OF AUTHOR:  Carter King (CK-OCSB)
# NAME OF THE PROGRAM:  Q2Reverse
# DATE OF CREATION:  2022-01-25
# PURPOSE OF PROGRAM:  To print a word in reverse one line at a time


# VARIABLE DEFINITION




# INPUT
UserWord = str(input("Please enter The word you would like reversed: "))


# PROCESSING
Reversal= (UserWord[::-1])

for i in range(1,20):
  print(Reversal[i:i +1])


# OUTPUT
