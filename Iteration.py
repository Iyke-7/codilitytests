def solution(n):
    b=bin(n)[2:]
    s1=False
    tz=0 # temp zeros
    mz=0 # max zeros 
    for e in b:
        if e=='1':
            mz=max(tz,mz)
            tz=0
            s1=True
        else:
            if(s1==True):
                tz+=1
            
            
    return mz

def main():
    try:
        n = int (input("Enter a number: "))
        result = solution(n)
        print(f"The maximum number of consecutive zeros surrounded by ones in the binary representation of{n} is {result}.")
    except ValueError:
        print("Please enter a valid integer.")
        
if __name__ == "__main__":
    main()