def print_lineified(s):
    for ch in s:
        print ch

def intersperse(s, sep = ' '):
    ret = s[0]
    for i in range(1, len(s)):
        ret = ret + sep + s[i]
    return ret

def swap(s, n):
    return s[n:len(s)] +s[0:n]

print_lineified('vertical')
print intersperse('hello')
print swap('hello',3)
