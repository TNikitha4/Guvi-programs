ch=input()
if(ch=='a' or ch=='A' or ch=='e' or ch=='E' or ch=='i' or ch=='I' or ch=='o' or ch=='O' or ch=='u' or ch=='U'):
    print("vowel")
elif((ch>='a' and ch<='z')or(ch>='A' and ch<='Z')):
    print("consonant")
else:
    print("invalid")
   
