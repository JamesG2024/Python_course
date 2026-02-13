def firstSetBit(n):

    # Count variable set as 0 

    count = 1


    # Right shift the number till we find first set bit

    while (n):

        if(n&1==1):

            break

        count += 1

        n >>= 1

    return count
