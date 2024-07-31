'''
#String Concatenation (Adding two Strings)
str1 = "My name"
str2 = "is Oliver"
print(str1+ " " +str2)
'''
'''
#Calculating the length of the String, using len() function of string. 
#It also includes blank-space.
str = "Hi, Welcome to the Journey of Python"
siz = len(str)
print(siz)
'''
'''
#Using in-built python functions such as lower() and upper()
#lower() is used to convert the given string to the lowercase completely.
#upper() is used to convert the given string to the uppercase completely.
givnStr="PYTHON is DYNAMIC language"
print("Upper Case - "+givnStr.upper())
print("Lower Case - "+givnStr.lower())
'''
'''
#Using in-built function named as split(), it will give you a list of elements
#splited with the blankspaces
strtemp="Implementing the function-split() here"
spltStr=str(strtemp.split())
#why i've used this str() here as we can't concat list to the string typed datatype 
#so as to print the splitted elements in the string i've used this typecasting concept here.
print("Splitted String - "+spltStr)
'''
strTemp = "What is the concept of replace()"
strNew = str  