# Check if two Strings have the same Characters in Python

def have_same_characters(str1, str2):
    return sorted(str1) == sorted(str2)


print(have_same_characters('bob', 'obb'))  # 👉️ True
print(have_same_characters('bob', 'obbb'))  # 👉️ False
print(have_same_characters('bob', 'abc'))  # 👉️ False