

def palindrome(word):
    """Sprawdza czy dany łańcuch znaków jest palindromem za pomocą rekurencji."""
    word = word.lower()
    if len(word) == 1:
        return "Word is palindrome"
    elif word[0] == " ":
        return palindrome(word[1:])

    elif word[-1] == " ":
        return palindrome(word[-1])
    
    elif word[0] == word[-1]:
        return palindrome(word[1:-1])
    else:
        return "Word isn't palindrome"
    

print(palindrome("abcdefedcba"))
print(palindrome("abcdefghijk"))
print(palindrome("Was it a cat I saw"))
print(palindrome.__doc__)