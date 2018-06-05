def numOf(s, f, p, counter = 0):
    if p == 0:
        if s[p] == f:
            counter += 1
        return counter

    if s[p] == f:
        counter += 1
        #print("p:",p)

    return numOf(s, f, (p-1),counter)

def reverse(s, l, r):
    s = list(s)

    if r == l or r-1 == l:
        s[r], s[l] = s[l], s[r]
        s = "".join(s)
        return s

    s[r], s[l] = s[l], s[r]

    return reverse(s, l+1, r-1)


def palindrome(s, count = 0):
    start = count
    ende = len(s)-1-count
    count += 1
    if s[start] != s[ende]:
        return False
    if start == ende or start+1 == ende:
        return True
    return palindrome(s, count)




test = "Das Haus ist blau"
pal = "annan"

testcount = numOf(test, "b", 16)
testrev = reverse(test, 4, 12)
print(testrev)
testpal = palindrome(pal)
print(testpal)
