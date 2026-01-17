def ONSquareTime(n):
    interaction=0
    for i in range(0,n):
        for j in range(0,n):
            print("*", end =" ")
            interaction+=1
        print("")



    print("\nWhen n is n",n," Interations =",interaction,"\n")


ONSquareTime(5)