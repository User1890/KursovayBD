from russian_names import RussianNames
import random
import string
import datetime
def d():
    fullname = RussianNames(gender=1).get_person()
    exp = random.randint(5,20)
    clas = random.randint(1,3)
    salary = 15 * (1 + clas / 10) + 15 * exp / 10
    return [fullname, exp, clas, int(salary * 1000)]

def b():
    type = random.randint(2,5) * 10 + 2
    a = 'ABEKMHOPCTYX'
    num = a[random.randint(0,len(a)-1)] + f"{random.randint(0,9)}" + f"{random.randint(0,9)}" + f"{random.randint(0,9)}" + a[random.randint(0,len(a)-1)] + a[random.randint(0,len(a)-1)]
    return [type, num]

def r():
    stime = f"0{random.randint(4,9)}:{random.randint(10,59)}"
    etime = f"{random.randint(20,23)}:{random.randint(10,59)}"
    num = random.randint(1,200)
    interval = f"00:{random.randint(10,30)}"
    return [stime, etime, num, interval]

def db():
    res =[]
    r = [6,10,12,28,28,41,54,70,101,102,107,113,116,131,149,150,161,167,177,181]
    b = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
    while len(r) != 0:
        d_i = random.randint(0,len(r)-1)
        b_i = random.randint(0,len(b)-1)
        res.append([r[d_i], b[b_i]])
        r.remove(r[d_i])
        b.remove(b[b_i])
    return res

data = db()
for i in data:
    print(f"insert into bus_route(idbus, numberroute) values ({i[1]}, {i[0]});")
