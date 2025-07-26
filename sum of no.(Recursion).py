def add(num):
    if len(num)==1:
        return(num[0])
    else:
        return((num[0])+add(num[1:]))
print(add([12,4,7,9]))    