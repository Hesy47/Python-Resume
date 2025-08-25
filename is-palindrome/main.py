def is_palindrome(text: str) -> bool:
    palindrome_word="".join(word.lower() for word in text if word.isalnum())
    return palindrome_word == palindrome_word[::-1]


print(is_palindrome("hello"))
print(is_palindrome("was it a car or a cat I saw?"))
