passengers= int(input("How many passengers?"))
 
if passengers <=4:
    print("send coach")
elif passengers >4 and passengers <17:
    print("send 16-seater")
else:
    print("send 4-seater car")
