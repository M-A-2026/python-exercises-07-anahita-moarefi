text=input("text: ")

def analyze_text(text):
    l=0
    n=0
    u=0
    lo=0
    m=0
    w=0
    v=0
    e=0
    #p=0
    [lw,ml]=[0,0]
    words=text.split()
    Words=len(words)
    d.setdefault("words",Words)
    sw=min(words,key=len)
    for word in words:
        mcw=words.count(word)        
        length=len(word)        
        if mcw>w and word.isalpha():
            w=mcw
            v=word
        if [length,word]>[ml,lw] and word.isalpha():
            ml=length
            lw=word
        if word==word[::-1]:
            p=word
            d.setdefault("palindrome words",p)
    print(v,w)
    d.setdefault("most common word",v)
    d.setdefault("longest word",lw)               
    for i in text:
        c=text.count(i)
        if i.isalpha():
            l+=1
        if i.isnumeric():
            n+=1
        if i.isupper():
            u+=1
        if i.islower():
            lo+=1
        if c>m and i.isalpha():
            m=c
            e=i
    print(m,e)
    d.setdefault("most common letter",e)    
    d.setdefault("letters",l)
    d.setdefault("digits",n)
    d.setdefault("uppercase",u)
    d.setdefault("lowercase",lo)
    d.setdefault("shortest word",sw)
d={}
analyze_text(text)
print(d)