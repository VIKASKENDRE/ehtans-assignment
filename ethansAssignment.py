from time import sleep
def one():
    print("1. WAP to reverse a string\n")

    word = input("Enter a word: ")
    word2 = word[::-1]
    print("Revers of {} is {}".format(word, word2))
def two():
    print("2. WAP to split the string and store in a list\n")
    word = input("Enter a word: ")
    l = []
    for i in range(len(word)):
        l.append(word[i])
    print(l)
def three():
    print("3. WAP to split the string and store only even placed items in list\n")
    word = input("Enter a word: ")
    word = word[::2]
    l = []
    for i in range(len(word)):
        l.append(word[i])
    print(l)
def four():
    print("4. WAP to lower the string\n")
    word = input("Enter a word: ")
    print("word in lowecase: "+word.lower())

question=input("Enter the question number: ")

def five():
    print('5. If S="EtHaNs", swap the cases in the word:"eThAnS" ')
    S = "EtHaNs"
    print("S = "+S)
    S2 = ''
    count1 = 0
    count2 = 0
    for i in range (len(S)):
        if S[i].isupper() == True:
            count1+=1
            S2 += S[i].lower()
        elif S[i].islower() == True:
            count2+=1
            S2 += S[i].upper()
    S = S2
    print("S = "+S)

def six():
    print('6. WAP to check if a sub string is available in a string. String = "This is python"')
    stat = "This is python"
    substat = input("Enter a string: ")
    if substat in stat:
        print("True")
    else:
        print("False")
def seven():
    print("7. WAP to capitalize a string")
    word = input("Enter the word : ")
    print("Output: "+word.upper())

def eight():
    print('8. WAP to put 3 "*" on either side of s="ETHANS"')
    s = "ETHANS"
    print(3*"*"+s+3*"*")
def nine():
    print("9. WAP to hide 12 starting digit of a 16 digit account number")
    accountNumber = input("Enter 16 digit account number: ")
    accountNumber1 = ''
    for i in range (len(accountNumber)):
        if i == 12:
            break
        else:
            accountNumber1 += "*"
    print("Account number: "+accountNumber1 + accountNumber[12:])

def ten():
    print('10. WAP to remove leading whitespaces from string s= "       Hello      ". After that remove both leading and trailing whitespaces.')
    s= '       Hello      '
    print(s)
    print("without trailing whitespace: s = " +s.rstrip()+"\n")
    print("without leading whitespace: s = " +s.lstrip()+"\n")
    print("without any whitespace: s = "+s.strip())

def eleven():
    print("11.WAP to remove all [vowel] characters, string s = 'Colorless green ideas sleep furiously'")
    statement = "Colorless green ideas sleep furiously"
    vowels = ['a','e','i','o','u']
    for i in statement:
        if i in vowels:
            statement = statement.replace(i,"")
    print(statement)

def twelve():
    print("12.WAP to del a range of items in list")
    #listofitems = [1,2,3,4,5,6]
    listofitems = []
    n = int(input("Enter number of elements: "))
    print("Enter the elements: ")
    for i in range(0,n):
        element = input()
        listofitems.append(element)
    print(listofitems)
    n1 = int(input("Enter lower limit: "))
    n2 = int(input("Enter uper limit: "))
    del listofitems[n1:n2]
    print(listofitems)

def thirteen():
    print("13.WAP to check if the second last element is divisible by 4.")
    listofitems = []
    n = int(input("Enter number of elements: "))
    print("Enter the elements: ")
    for i in range(0,n):
        element = input()
        listofitems.append(element)
    print(listofitems)
    if int(listofitems[-2])%4 == 0 :
        print("Awesome ! second last element is divisible by 4.")
    else:
        print("Awww, second last element is not divisible by 4")

def fourteen():
    word = input("Enter a number or a word: ")
    if word == word[::-1]:
        print("Entry is a palindrome")
    else:
        print("Not a palindrome")

def fifteen():
    print("15.Convert a list into string")
    listofitems = []
    n = int(input("Enter number of elements: "))
    print("Enter the elements: ")
    for i in range(0,n):
        element = input()
        listofitems.append(element)
    print(listofitems)
    newword = ""
    print(newword.join(listofitems))

def sixteen():
    print("16.convert a string into list")
    word = input("Enter a word: ")
    listfromword = []
    for letter in word:
        listfromword += letter
    print(listfromword)

def seventeen():
    print("17.WAP to print 1st and last element of a list")
    n = int(input("enter the number of elements: "))
    listofitems = []
    for i in range(0,n):
        element = input()
        listofitems += element
    print(listofitems)
    print("The first and the last  elements in the list are: \n",listofitems[0], " and ", listofitems[-1])

def eighteen():
    print("18.write a program to get the 2 highest numbers in a list")
    n = int(input("Enter the number of elements: "))
    l = []
    for i in range(0,n):
        element = input()
        l += element
    print(l)
    print("The highest value in the list is: "+ max(l))
    l.remove(max(l))
    print("The 2nd highest value in the list is: "+ max(l))

def nineteen():
    print("19.WAP to convert list in dictionary")
    n = int(input("Enter the number of elements: "))
    l = []
    for i in range(0,n):
        element = input()
        l += element
    print(l)

    print("\nConvert list into dictionary")

    d = {i : l[i] for i in range(0,len(l))}

    print(d)

def twenty():
    print("20.WAP to flatten a list\n")
    l = [[1,2,3],[4,5,6],[7,8,9]]
    flatlist = []
    for innerlist in l:
        for i in innerlist:
            flatlist.append(i)
    print("Original List: ", l)
    print("Flat List: ", flatlist)

def twentyone():
    print("21.WAP to merge 2 dictionaries:dict = {'Name': 'BB', 'Age': 25}, dict2 = {'YouTubeVideo': 'BB ki vines'}\n")
    def mergeDict(dict1,dict2):
        return(dict2.update(dict1))
    dict1 = {'Name': 'BB', 'Age': 25}
    dict2 = {'YouTubeVideo': 'BB ki vines'}
    print(dict1,",",dict2)
    mergeDict(dict1,dict2)
    print("Merging two dictionaries:")
    sleep(0.5)
    print(".")
    sleep(0.5)
    print(".")
    sleep(0.5)
    print(".")
    sleep(0.5)
    print(".")
    sleep(0.5)
    print(".")
    print("Final dictionary :",dict2)

def twentytwo():
    print("22.What is the output of <list_name>[-1::] and <list_name>[-1] and why?")
    l = [22, 4, 34, 56, 89]
    print("First condition l[-1::] = ", l[-1::])
    print("Second condition l[-1] = ", l[-1])
    print("In First condition we are using splicing, hence,\nit returns a list from range -1 to -1 since no other value is provided.")
    print("In Second condition we are retriving the value present at index of -1.")

def twentythree():
    print("23.WAP to iterate over items in dictionary and print all the key for which value is a vowel")
    d = { 1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'i', 7:'h', 8:'o', 9:'j', 10:'u'}
    l = ['a', 'e', 'i', 'o', 'u']
    print(d)
    print(l)
    for vowels in l:
        for key,v in d.items():
            if vowels == v:
                print(key)
def twentyfour():
    print("24.WAP to empty a dictionary")
    d = { 1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'i', 7:'h', 8:'o', 9:'j', 10:'u'}
    print('d =',d)
    sleep(0.5)
    print("Deleting items from the dictionary!")
    sleep(0.5)
    print('.')
    sleep(0.5)
    print('.')
    sleep(0.5)
    print("Almost there!")
    sleep(0.5)
    print('.')
    sleep(0.5)
    print('.')
    sleep(0.5)
    print('Thank you for your patience.')
    sleep(0.5)
    print('.')
    sleep(0.5)
    d.clear()
    print("d = ",d)

def twentyfive():
    print("25.WAP to remove all duplicate items in a list/tuple")
    l = [1,1,2,2,3,3,4,4]
    print('l = ', l)
    t = (1,1,2,2,3,3,4,4)
    print('t = ', t)

    print("\nRemove duplicates from list l : \n")
    l = list(set(l))
    print("new l = ", l)

    print("\nRemove duplicates from tuple t: \n")
    t = tuple(set(t))
    print("new t = ", t)

def twentysix():
    print("26.WAP to get the common elements in 2 sets")
    s1 = {'lucy', 'sandy','mady','joe'}
    print("S1 = ", s1)
    s2 = {'don','lucy','joe','daisy'}
    print("S2 = ", s2)
    if(s1 & s2):
        print("Common items are: ", (s1 & s2))

def twentyseven():
    print("27.WAP to get the different elements in 2 sets")
    s1 = {'lucy', 'sandy','mady','joe'}
    print("S1 = ", s1)
    s2 = {'don','lucy','joe','daisy'}
    print("S2 = ", s2)
    print("Different items are: ", ((s1 - s2)|(s2 - s1)))

def twentyeight():
    print("28.WAP to shift all the zeros in a list to RHS.")
    l = [1,2,0,3,0,4,5,0]
    print("List = ", l)
    l1 = sorted(l)
    print("Sorted list = ", l1)

    print("Reverse_list = ", l1[::-1])
def twentynine():
    print("29.WAP to print all the elements of a list in one line.")
    l = [1,2,0,3,0,4,5,0]
    print("list = ", l)
    print("unpacked list = ", *l)

def thirty():
    print("30.WAP to print 3 elements of list in one line and then 3 more lines in next line and so on. take a list with 12 elements.")
    l = [1,2,3,4,5,6,7,8,9,10,11,12]
    print("list = ", l)
    print("list items in line 1 : ", *l[0:3])
    print("list items in line 2 : ", *l[3:6])
    print("list items in line 3 : ", *l[6:9])
    print("list items in line 4 : ", *l[9:13])


if question == '1':
    one()
if question == '2':
    two()
if question == '3':
    three()
if question == '4':
    four()
if question == '5':
    five()
if question == '6':
    six()
if question == '7':
    seven()
if question == '8':
    eight()
if question == '9':
    nine()
if question == '10':
    ten()
if question == '11':
    eleven()
if question == '12':
    twelve()
if question == '13':
    thirteen()
if question == '14':
    fourteen()
if question == '15':
    fifteen()
if question == '16':
    sixteen()
if question == '17':
    seventeen()
if question == '18':
    eighteen()
if question == '19':
    nineteen()
if question == '20':
    twenty()
if question == '21':
    twentyone()
if question == '22':
    twentytwo()
if question == '23':
    twentythree()
if question == '24':
    twentyfour()
if question == '25':
    twentyfive()
if question == '26':
    twentysix()
if question == '27':
    twentyseven()
if question == '28':
    twentyeight()
if question == '29':
    twentynine()
if question == '30':
    thirty()
