from copy import deepcopy

a=[[1],2,3]
b=a
c=a[:]
d=deepcopy(a)
e=deepcopy(b)
f=deepcopy(c)
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(id(a))
print(id(b))
print(id(c))
print(id(d))
print(id(e))
print(id(f))
print(id(a[0]))
print(id(b[0]))
print(id(c[0]))
print(id(d[0]))
print(id(e[0]))
print(id(f[0]))
print(id(f[1]))
print(id(f[2]))

a[0]=[9]
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(id(a))
print(id(b))
print(id(c))
print(id(d))
print(id(e))
print(id(f))
print(id(a[0]))
print(id(b[0]))
print(id(c[0]))
print(id(d[0]))
print(id(e[0]))
print(id(f[0]))
print(id(f[1]))
print(id(f[2]))
