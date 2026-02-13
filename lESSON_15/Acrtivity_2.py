def totalSetBits(n):

    # Count variable set as 0 

    count = 0

    # Right shift the number till we find first set bit

    while (n):

        if(n&1==1):

            count+=1

        n >>= 1       

    return count

