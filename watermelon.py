w=int(input("enter the weight input"))
if(w%2!=0 and w==2):
      print("no is odd")
else:
    x=w/2
    if(x%2==0):
         print("yes,brother 1 gets",x,"brother2 gets",x+1)
    else:
        print("yes,brother 1 gets",x-1," brother 2 gets ",x+1)
