def analyze_transactions(transactions):
    d1={}
    d2={}
    d3={}
    t={}
    l1=[]
    l2=[]
    l3=[]
    sum1=0
    sum2=0
    sum3=0
    sum4=0
    sum5=0
    sum6=0
    count1=0
    count2=0
    count3=0
    for i in transactions:
        if i[0]=="Ali":
            count1=i.count(i[0])+count1           
            if i[1]=="deposit":
                sum1=sum1+i[2]  
            if i[1]=="withdraw":
                sum2=sum2+i[2]       
        if i[0]=="Sara":
            count2=i.count(i[0])+count2            
            if i[1]=="deposit":
                sum3=sum3+i[2]
            if i[1]=="withdraw":
                sum4=sum4+i[2]
        if i[0]=="Reza":
            count3=i.count(i[0])+count3            
            if i[1]=="deposit":
                sum5=sum5+i[2]
            if i[1]=="withdraw":
                sum6=sum6+i[2]
        Balance_change1=sum1-sum2
        Balance_change2=sum3-sum4
        Balance_change3=sum5-sum6        
    d1.setdefault("deposits",sum1)          
    d1.setdefault("withdrawals",sum2)
    d1.setdefault("Balance_change",Balance_change1)
    d1.setdefault("transactions",count1)
    d2.setdefault("deposits",sum3)          
    d2.setdefault("withdrawals",sum4)
    d2.setdefault("Balance_change",Balance_change2)
    d2.setdefault("transactions",count2)
    d3.setdefault("deposits",sum5)          
    d3.setdefault("withdrawals",sum6)
    d3.setdefault("Balance_change",Balance_change3)
    d3.setdefault("transactions",count3)
    t.setdefault("Ali",d1)
    t.setdefault("Sara",d2)
    t.setdefault("Reza",d3)   
    for i in t.values():
        l1.append(i["deposits"])
        l2.append(i["withdrawals"]) 
        l3.append(i["transactions"])        
    print("max deposit:",max(l1))   
    print("max withdraw:",max(l2))
    print("max transactions:",max(l3))
    for i in t.keys():
        for j in t[i].keys():
            if t[i]["transactions"]==t[i][j]:
                if t[i]["transactions"]==max(l3):
                    print("most active user:",i)
    return t                         
transactions=[("Ali","deposit",5000000),\
              ("Ali","withdraw",1000000),\
              ("Sara","deposit",8000000),\
              ("Ali","withdraw",500000),\
              ("Sara","withdraw",2000000),\
              ("Reza","deposit",10000000) ]   
print(analyze_transactions(transactions))    