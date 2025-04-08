S1={1,2,3}
S2={"A","B","C"}
S3=list(zip(S1,S2))
print(S3)

List1=[1,2,3,4,5]
List2=[3,16,14,11,12]
for x,y in zip (List1,List2[::-1]):
    print(x,y)

Dict_1={List1:List2  for List1,List2 in zip (List1,List2)}
print(Dict_1)
