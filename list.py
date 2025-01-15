nested =[[0]*3]*3
print(nested)
# the above creates one reference only and after creating copy it just copies the reference of one list instead of creating three separate list.
nested[0][1] = 1
print(nested)
# the above changes and upon changing it can be observed that every value changes instead of one value change
nested = [[0]*3 for _ in range(3)]
nested[0][1]=1
print(nested)
# the proper method to initialize 2 dimension list