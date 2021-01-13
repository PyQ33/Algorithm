a = [1,4,3]
print(f"{a} : normal list")


a.append(2)
print(f"{a} : Append")

a.sort()
print(f"{a} : sorted down upscale")

a.sort(reverse= True)
print(f"{a} : sorted down downscale")

a.reverse()
print(f"{a} : reverse a")

a.insert(2,11)
# insert 3 to index 2
print(f"{a} : insert 3 to index 2")



print(f"{a.count(11)} : count num under 3")

a.remove(11)
print(a)

# not in
a = [1,2,3,4,5,5,5,5]
remove_set= {3,5}
result =[i for i in a if i not in remove_set]
print(result)


a = [1,2,3,4,5,5,5,5]
remove_set= [1,5]
result =[i for i in a if i not in remove_set]
print(result)