#回文数
def is_palindrome(m):
    str1 = str(m)
    str2 = ""
    length  = len(str1)
    for x in range(len(str1)):
        str2 += str1[length - 1 - x]
    if str1 == str2:
        return True
    else:
        return False
output = filter(is_palindrome, range(1, 1000))
print(list(output))