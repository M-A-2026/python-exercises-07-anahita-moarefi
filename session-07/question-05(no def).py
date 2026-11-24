logs=[("Ali","LOGIN",200),("Ali","DOWNLOAD",200),\
      ("Sara","LOGIN",403),("Reza","LOGIN",200),\
      ("Sara","LOGIN",403),("Sara","LOGIN",403)]
count1=0
count2=0
count3=0
count4=0
count5=0
count6=0
count7=0
count8=0
c=3
d={}
d1={}
d2={}
d3={}
for i in logs:
    if i[1]=="LOGIN" and i[2]==200:
        count1+=1
    if i[1]=="LOGIN" and i[2]==403:
        count2+=1
        count=i.count(403)
        if c>=count:
            c=count    
    if i[0]=="Ali":
        if i[1]=="LOGIN":
            count3+=1
        if i[1]=="DOWNLOAD":   
            count4+=1
    if i[0]=="Sara":
        if i[1]=="LOGIN":
            count5+=1
        if i[1]=="DOWNLOAD":
            count6+=1
    if i[0]=="Reza":
        if i[1]=="LOGIN":
            count7+=1
        if i[1]=="DOWNLOAD":
            count8+=1
d.setdefault("Successful LOGIN",count1)
d.setdefault("Unsuccessful LOGIN",count2)
d.setdefault("Suspicious User",i[0])
d1.setdefault("LOGIN",count3)
d1.setdefault("DOWNLOAD",count4)
d.setdefault("Ali",d1)
d2.setdefault("LOGIN",count5)
d2.setdefault("DOWNLOAD",count6)
d.setdefault("Sara",d2)
d3.setdefault("LOGIN",count7)
d3.setdefault("DOWNLOAD",count8)
d.setdefault("Reza",d3)
print("Successful LOGIN:",count1)        
print("Unsuccessful LOGIN:",count2)
print("Suspicious user:",i[0])
print("Ali:","LOGIN:",count3,";","DOWNLOAD:",count4)
print("Sara:","LOGIN:",count5,";","DOWNLOAD:",count6)
print("Reza:","LOGIN:",count7,";","DOWNLOAD:",count8)
print(d)