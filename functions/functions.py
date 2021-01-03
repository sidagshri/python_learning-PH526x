some = 120
def sum(a, b):
    mysum = a + b
    return mysum

print(sum(10, 13))

def sum_modify(a, b):
    global some
    some = a + b
    return some

print(sum_modify(10, 13))
print(some)

def add_and_sub(a, b):
    mysum = a + b
    mydiff = a - b
    return (mysum, mydiff)

print(add_and_sub(2,3))

def modify(mylist):
    mylist[0] *= 10

l = [1,2,3,4,5,6,7,8,9]
modify(l)
print(l)

def modify_and_return(mylist):
    mylist[0] *= 10
    return(mylist)

l = [1,2,3,4,5]
m = modify_and_return(l)
print(m is l)

def intersect(s1, s2):
    res = []
    for x in s1:
        if x in s2:
            res.append(x)
    return res
print(intersect([1,2,3,4,5,6], [3,4,5,6,7,8]))

# a possible shorthand for this function could be
def intersect_two(s1, s2):
    return [x for x in s1 if x in s2]
print(intersect_two([1,2,3,4,5,6], [3,4,5,6,7,8]))