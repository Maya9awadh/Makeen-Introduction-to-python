
#unction that count the number f vowels in string
def countVowels(string):
    count=0
    for i in string:
        if (i in 'aeiou') or (i in 'AEIOU'):
            count=count+1
    return count

str1=input("Enter string: ")
print(countVowels(str1))