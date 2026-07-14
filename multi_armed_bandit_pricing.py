import random, math

r = [5, 8, 12]  
n = 100

e = [0]*3; c = [0]*3; rev1 = 0
for i in range(n):
    a = random.randint(0,2) if random.random()<0.1 else e.index(max(e))
    x = r[a] + random.randint(-2,2)
    rev1 += x
    c[a] += 1
    e[a] += (x-e[a])/c[a]

v = r[:]; c = [1,1,1]; rev2 = sum(r)
for t in range(3,n):
    u = [v[i]+math.sqrt(2*math.log(t+1)/c[i]) for i in range(3)]
    a = u.index(max(u))
    x = r[a] + random.randint(-2,2)
    rev2 += x
    c[a] += 1
    v[a] += (x-v[a])/c[a]

s = [1]*3; f = [1]*3; rev3 = 0
for i in range(n):
    a = max(range(3), key=lambda k: random.betavariate(s[k],f[k]))
    x = r[a] + random.randint(-2,2)
    rev3 += x
    if x >= r[a]: s[a]+=1
    else: f[a]+=1

print("Epsilon-Greedy :", rev1)
print("UCB            :", rev2)
print("Thompson       :", rev3)
