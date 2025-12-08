#Method 1
sent = "The sky is blue"
rev_sent = ' '.join(sent.split()[::-1])
print(rev_sent)


#Method 2
s = "The sky is blue"
print(' '.join(s.split()[::-1]))


#Method 3
s = "The sky is blue"
for i in s.split()[::-1]:
    print(i,end = " ")