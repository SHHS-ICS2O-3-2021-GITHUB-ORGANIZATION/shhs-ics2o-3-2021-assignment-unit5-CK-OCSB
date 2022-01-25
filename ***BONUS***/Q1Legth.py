# NAME OF AUTHOR:  Carter King (CK-OCSB)
# NAME OF THE PROGRAM: Q1Legth.py  
# DATE OF CREATION: 2022-01-25 
# PURPOSE OF PROGRAM:  To rpint the legth of a word in a loop then have the user exit when they wish


# VARIABLE DEFINITION





# INPUT
print("Remember, when you would like to exit please type a EXIT")
UserWord = input("Please enter any word:")



# PROCESSING
if UserWord == ("EXIT"):
  print("GoodBye")
while UserWord != ("EXIT"):
  print(len(UserWord))
  UserWord = input("Please enter any word:")
 

# OUTPUT