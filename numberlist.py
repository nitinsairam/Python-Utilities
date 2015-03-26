'''
Created on Feb 20, 2015

'''
from nt import lstat
def bucket():
    data = []
    flag = 0
    try :
        length = int(raw_input("Please enter the length of the series :: "))
        while flag<length :
            num = int(raw_input("Enter number :: "))
            data.append(num)
            flag +=1
     
        return data
    except :
        print "Oops !! Bad Input :("
        exit()

def totalOfSeries(lst):
    print "2.length of list : ",len(lst)
    print "3.List Content :: "
    i =0
    total = 0
    while i < len(lst):
        print "number[",i,"]-> ",lst[i]
        print"\n"
        i+=1
    for j in lst:
        total = total + j
    return total

def reverse(lst):
    num = len(lst)
    num = num-1
    reverseList = []
    for i in lst:
        reverseList.append(lst[num])
        num-=1
    return reverseList

def largest(lst):
    lnum=lst[0]
    j=1
    for i in lst:
        if j==len(lst):
                break
        elif lnum<lst[j]:
            lnum=lst[j]
        j+=1
    return lnum

def smallest(lst):
    lnum = lst[0]
    j=1
    for i in lst:
        if j==len(lst):
            break
        elif lnum>lst[j]:
            lnum=lst[j]
        j+=1
    return lnum

def sortedLst(lst):
    slist =[]
    slist=lst
    lgst = largest(lst)
    smlst = smallest(lst)
    slist.sort()
    return slist    
            
        
lst = []
lst = bucket()
print ""
print "1.Original List :: " , lst

total = totalOfSeries(lst)
print ""
print "4.Sum of Elements of List : " ,total

revList = reverse(lst)
print ""
print "5.Reversed List::  ",revList

largestNum = largest(lst)
print ""
print "6.Largest Number from the list is :: " , largestNum

smallestNum = smallest(lst)
print ""
print "7.Smallest Number from the list is :: ",smallestNum

sortedList = sortedLst(lst)
print ""
print "8.Sorted List ::  ",sortedList
