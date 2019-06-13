s = '/usr/local/bin/python'
for w in s.split("/") : print(w,end=' ')
print("\n",s[:s.rindex("/")],s[s.rindex("/")+1:])
