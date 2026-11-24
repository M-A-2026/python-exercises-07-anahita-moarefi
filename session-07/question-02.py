def process_order(customer,*products,**options):
    d={}
    l=[]
    final_price=0
    customer=input("cn:")
    products=input("ps:")
    product=products.split()
    d.setdefault("customer",customer)
    for i in product:
        l.append(i)
    d.setdefault("products",l)
    options=input("op:")
    option=options.split()
    for j in option: 
        if j=="tax":
           fee_t=float(input("tax fee:")) 
        if j=="discount":
            fee_d=float(input("discount:")) 
        if j=="shipping":
            fee_sh=float(input("shipping fee:")) 
    fee=fee_t+fee_sh+fee_d
    final_price=final_price+fee    
    d.setdefault(j,fee)
    d.setdefault("final_price",final_price)
    return{"customer":customer,"products":l,"tax":fee_t,"discount":fee_d,\
           "shipping":fee_sh,"final_price":final_price}
result=process_order("customer","products","options")
print(result)