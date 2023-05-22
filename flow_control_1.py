for x in range(1, 51): 
    if x % 3 == 0:  # if i when divided by 3 has zero remainder print "Boy"
        print("Boy")
    elif x % 5 == 0:  # else if i when divided by 5 has zero remainder print "Girl"
        print("girl")
    elif x % 3 == 0 & x % 5 == 0:  # else if i when divided by both 3 and 5 has a remainder zero print "couple"
        print("couple")
    else:
        print(x)  # print the incremented i
