try:
    def fs(n):
        if(n==0 or n==1):
            return n
        else:
            return fs(n-1)+fs(n-2)
    n=int(input("enter the numbers of terms : "))
    if(n<1):
        print("enter a positive number")
    else:
        for i in range(n):
            print(fs(i), end=(","))
except Exception as e:
    print(f"error occured : {e}")