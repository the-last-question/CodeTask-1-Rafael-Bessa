
def isPalindromeRecursive(word,start=-1,end=-1):
    if start == -1 and end ==-1:
        start = 0
        end = len(word) -1
        return isPalindromeRecursive(word,start,end)
    if start >= end:
        return True
    elif word[end] == word[start]:
        return isPalindromeRecursive(word,start+1,end-1)
    else:
        return False



def __main__():
    x = input("type the word\n")
    if isPalindromeRecursive(x):
        print("the word is a palindrome")
    else:
        print("the word is not a palindrome")

__main__()


