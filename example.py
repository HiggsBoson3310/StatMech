import numpy as np
import itertools
import copy
def sum(p, E, n):
    c = 0
    for i in range(len(E)):
        if(p in E[i]):
            c+=n[i]
    return c
def diff(l,e):
    for x in l:
        if(x!=e): 
            a=x
            break
    return a
V = range(np.random.randint(4,8))
E = []
for results in itertools.combinations(V,2):
    E.append(results)
n = []
for i in range(len(E)):
    n.append(np.random.randint(10))
A = []
for p in V:
    if(sum(p,E,n)%2==1): 
        A.append(p)
print(V)
print(E)
print(n)
print(A)
Z = [0]*len(E)
N = [n]
X = [A[0]]
finish = False
c = 0

print("Inicia Algoritmo")
while(finish == False):
    e = [x for x in E if X[c] in x]
    n_c = []
    for a in e:
        n_c.append(N[c][E.index(a)])
    if(N[c]==Z):
        finish = True
    elif(n_c==[0]*len(e)):
        N.append(copy.deepcopy(N[c]))
        if(set(A)<=set(X)):
            for p in V:
                if(sum(p,E,N[c])>0 and p!=X[c]):
                    X.append(p)
                    break
        else:
            l3 = [x for x in A if x not in X]
            X.append(min(l3))
    else:
        l3 = [E.index(x) for x in E if X[c] in x]
        l4 = [diff(E[i],X[c]) for i in l3 if N[c][i]>0]
        X.append(min(l4))
        j=copy.deepcopy(N[c])
        for i in range(len(N[c])):
            if(X[c] in E[i] and X[c+1] in E[i]):
                j[i]=j[i]-1
        N.append(j)
    c+=1
t = []
for i in range(1,len(N)):
    if(N[i]==N[i-1]):
        t.append(i)
print t
    
