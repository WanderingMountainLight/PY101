# ddaaiillyy ddoouubbllee

# Write a function that takes a string argument and returns a new string that contains the value of the
# original string with all consecutive duplicate characters collapsed into a single character.

# Examples
# # These examples should all print True
# print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
# print(crunch('4444abcabccba') == '4abcabcba')
# print(crunch('ggggggggggggggg') == 'g')
# print(crunch('abc') == 'abc')
# print(crunch('a') == 'a')
# print(crunch('') == '')

def crunch(str):
    result = []
    for char in range(len(str)):
        if char == 0 or str[char-1] != str[char]:
            result.append(str[char])
    return ''.join(result)

print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')