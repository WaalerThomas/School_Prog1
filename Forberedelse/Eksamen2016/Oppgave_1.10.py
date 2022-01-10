def test(a, b):
    if a == b:
        return a
    else:
        return b

print( test(4, test(2, 5)) )

# Output
# 5