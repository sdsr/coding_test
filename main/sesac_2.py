def is_palindrome(s):
    lower_s = ""
    for char in s:
        if char.isalnum():
            lower_s += char.lower()
    if lower_s == lower_s[::-1]:
        return "palindrome"
    else:
        return "not palindrome"

print(is_palindrome("hello"))
print(is_palindrome("racecar"))
print(is_palindrome("Racecar"))
