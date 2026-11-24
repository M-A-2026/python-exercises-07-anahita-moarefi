transactions=[("Ali","deposit",50000000,10),\
              ("Ali","withdraw",2000000,11),\
              ("Ali","withdraw",3000000,12),\
              ("Ali","withdraw",4000000,13),\
              ("Ali","withdraw",5000000,14),\
              ("Ali","withdraw",6000000,15),\
              ("Sara","deposit",50000000,20),\
              ("Sara","withdraw",60000000,21),\
              ("Reza","deposit",150000000,30)]
def detect_fraud(transactions):
    d={}
    d1={}
    d2={}
    d3={}    
    rw=3   
    l=[]
    report={}
    final_report={}
    def check_large_transaction():
        for i in transactions:
            if i[2]>100000000:
                return i[0]
    def check_repeated_withdrawals():
        for i in transactions:        
            if i[1]=="withdraw":
                l.append(i[0])
                l.append(i[3])            
        for i in l:
            count=l.count(i)
            if count>rw:
                #print(l)
                return i, count
    def check_balance():
        sum=0
        for i in transactions:
            if i[0]=="Ali":
                if i[1]=="withdraw":
                    sum=sum+i[2]            
                if i[1]=="deposit":
                    d1.setdefault("deposit",i[2])
            if i[0]=="Sara":
                if i[1]=="withdraw":
                    d2.setdefault("withdraw",i[2])
                if i[1]=="deposit":
                    d2.setdefault("deposit",i[2])
            if i[0]=="Reza":
                if i[1]=="withdraw":
                    d3.setdefault("withdraw",i[2])
                if i[1]=="deposit":
                    d3.setdefault("deposit",i[2])
        d.setdefault("Ali",d1)
        d.setdefault("Sara",d2)
        d.setdefault("Reza",d3)
        #print("sum of withdraws:",sum)           
        d1.setdefault("withdraw",sum)
        for i in d.keys():
            if i=="Ali":
                balance1=d[i].get("deposit")-d[i].get("withdraw") 
                if balance1<0:
                    return i 
            if i=="Sara":
                balance2=d[i].get("deposit")-d[i].get("withdraw")
                if balance2<0:
                    return i
            if i=="Reza":
                balance3=d[i].get("deposit")
                if balance3<0:
                    return i
    def generate_fraud_report():    
        report.setdefault("large transaction",check_large_transaction())
        report.setdefault("repeated withdrawals",check_repeated_withdrawals())
        report.setdefault("balance",check_balance())
        final_report.setdefault("Suspicious financial transaction",report)
        return report
    generate_fraud_report()          
    print(final_report)
detect_fraud(transactions)
