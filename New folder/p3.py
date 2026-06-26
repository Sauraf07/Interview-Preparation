'''Problem 3: Count Character Frequency'''
s = 'Saurav kumar Sharma'
feq ={}
for ch in s:
    feq[ch] = feq.get(ch,0)+1

print(feq)