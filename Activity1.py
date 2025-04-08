#Addition of two lists using map and lambda

Number1=[1,2,3,]
Number2=[4,5,6]
Result=map(lambda x,y :x+y, Number1 , Number2)
print(list(Result))

#Square of numbers using map

Numbers=[1,2,3,5]
def Square(n):
    return n*n
result2=list(map(Square,Numbers))
print(result2)