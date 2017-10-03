string_in=raw_input()
s=list(string_in)
# print s

if s[0]=="-":
    if s[2]=="-":
        print -int(s[1])-int(s[3])

    if s[2]=="+":
        print -int(s[1])+int(s[3])

else :
        if s[1]=="-":
            print +int(s[0])-int(s[2])
        if s[1]=="+":
            print +int(s[0])+int(s[2])
