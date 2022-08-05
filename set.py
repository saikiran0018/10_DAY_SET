a={1,2}
a.clear()
print(a)                              #set()


e={}
print(e,type(e))                     #dict


v={1,2.6,"hello",("hi",2)}
print(v,type(v))                     #set



n={10,20,30}
print(n[1])                            #typeError


d={1,3,5}
print(d,type(d))                       #set
k=frozenset(d)
print(k[d])                              #type error


a={1,2,3}
b='hello',1,2,3
a.add(b)
print(a)                              #{1,2,3('hello',1,2,3)}                #{('hello',1,2,3),1,2,3}



a={1,2,3}; b={4,3,3,6}; c={10,15,20}; d={1,4,7}
print(a.intersection(b))            #{3}
print(a.intersection(c))            #set()    
print(a.intersection(d))            #set()
print(b.intersection(d))            #{4}



a={1,2,3,'hello'}
b={4,3,5,'hey'}
print(a.union(b))                    #1,2,3,4,5,'hello','hey'
print(b.union(a))       


a={1,2,3}
b={4,3,5}
c={4,3,7}
a.update(b)
a.update(c)
print(a)                             #{1,2,3,4,5,7}



a={5,4,10,15,20}
b={10,3,6}
print(a.difference(b))               #{5,4,15,20}
print(b.difference(a))               #{3,6}
print(a-b)
print(b-a)




v={2,4,6,7,8}
v.pop()
print(v)                               #{4,6,7,8}


a={1,3,2,4}
b={5,6,7}
c={4,5,6}
print(a.isdisjoint(b))                     #True
print(a.isdisjoint(c))                     #False          
print(b.isdisjoint(c))                     #False