def check_prime(num):
    if num==1:
        print("Not prime")
    if num==2:
        print("Prime")
    if num>2:
        for i in range(2,num):
            if num%i==0:
                print("Not prime")
                break
            else:
                print("Prime")
                break
check_prime(11)                   