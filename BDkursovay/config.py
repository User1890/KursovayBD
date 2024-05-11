import mysql.connector
 
connect = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='fleet')

cursor = connect.cursor()

def driver_select():
    data = ""
    cursor.execute(f"select fullname, expirience, class, salary from driver;")
    for i in cursor.fetchall():
        data += f"""* {i[0]}\nОпыт работы: {i[1]}\nКласс водителя: {i[2]}\nЗаработная плата: {i[3]} руб.""" + "\n\n"
    return data

def driver_search(dictionary):
    cursor.execute(f"select fullname, expirience, class, salary from driver where fullname = '{dictionary['key']}';")
    i = cursor.fetchall()[0]
    return f"""* {i[0]}\nОпыт работы: {i[1]}\nКласс водителя: {i[2]}\nЗаработная плата: {i[3]} руб."""

def driver_p(dictionary):
    if dictionary['route'] and dictionary['bus'] == False:
        cursor.execute(f"select fullname from driver where id = (select iddriver from bus_driver where idbus = (select idbus from bus_route where numberroute = {int(dictionary['key_d'])}));")
        out = "Данный маршрут обслуживают следующие водители:\n"
        for i in cursor.fetchall():
            for j in i:
                out += j + '\n'
    elif dictionary['route'] == False and dictionary['bus']:
        cursor.execute(f"select numbers from bus where id = (select idbus from bus_driver where iddriver = (select id from driver where fullname = '{(dictionary['key_d'])}'))")
        out = f"{(dictionary['key_d'])} работает на следующих автобусах:\n"
        for i in cursor.fetchall():
            for j in i:
                out += j + '\n'
    return out

def route_select():
    data = ""
    cursor.execute(f"select st_time, end_time, number, interval_r from route;")
    for i in cursor.fetchall():
        data += f"""* Маршрут - №{i[2]}\nВремя начала движения: {str(i[0])[0:5]}\nВремя окончания движения: {str(i[1])[0:5]}\nИнтервал: {str(i[3])[0:5]}""" + "\n\n"
    return data

def route_search(dictionary):
    cursor.execute(f"select st_time, end_time, number, interval from route where number = '{dictionary['key0']}';")
    i = cursor.fetchall()[0]
    return f"""* Маршрут - №{i[2]}\nВремя начала движения: {str(i[0])[0:5]}\nВремя окончания движения: {str(i[1])[0:5]}\nИнтервал: {str(i[3])[0:5]}""" + "\n\n"

def route_p(dictionary):
    out = f"Протяженность:\n"
    for i in range(len(dictionary['key_p'].split(', '))):
        cursor.execute(f"select length from way where number in ({dictionary['key_p'].split(', ')[i]})")
        out += f"Маршрут №{dictionary['key_p'].split(', ')[i]} - {cursor.fetchall()[0][0]} км\n"
    return out

def bus_select():
    data = ""
    cursor.execute(f"select type, numbers from bus;")
    for i in cursor.fetchall():
        cursor.execute(f"select capacity from typebus where type = {i[0]}")
        data += f"""* Номер автобуса - {i[1]}\nТип: {i[0]}\nВместимость: {cursor.fetchall()[0][0]}""" + "\n\n"
    return data


def bus_search(dictionary):
    cursor.execute(f"select type, numbers from bus where numbers = '{dictionary['key1']}';")
    i = cursor.fetchall()[0]
    cursor.execute(f"select capacity from typebus where type = {i[0]}")
    return f"""* Номер автобуса - {i[1]}\nТип: {i[0]}\nВместимость: {cursor.fetchall()[0][0]}""" + "\n\n"

def bus_p(dictionary):
    if dictionary['route_l3'] and dictionary['time'] == False:
        cursor.execute(f"select numbers from bus where id = (select idbus from bus_route where numberroute = {int(dictionary['key_b'])})")
        out = f"Маршрут №{dictionary['key_b']} обслуживается автобусами:\n"
        for i in cursor.fetchall():
            for j in i:
                out += j + '\n'
    elif dictionary['route_l3'] == False and dictionary['time']:
        out = ""
        for i in range(len(dictionary['key_b'].split(', '))):
            cursor.execute(f"select st_time, end_time from route where number = {dictionary['key_b'].split(', ')[i]}")
            r = cursor.fetchall()
            out += f"Маршрут №{dictionary['key_b'].split(', ')[i]}\nВремя начала движения: {str(r[0][0])[0:5]}\nВремя окончания движения: {str(r[0][1])[0:5]}\n"
    return out

def add_d(dictionary):
    cursor.execute(f"insert into driver (id, fullname, expirience, class, salary) values ((select max(id) from driver) + 1,'{dictionary['fullname']}',{int(dictionary['expirience'])},{int(dictionary['class'])},{int(dictionary['salary'])})")
    cursor.execute(f"insert into bus_driver (idbus, iddriver) values ((select id from bus where numbers = '{dictionary['number_bus_add']}'),(select max(id) from driver) + 1);")
    connect.commit()

def delete_d(dictionary):
    cursor.execute(f"delete from driver where fullname = '{dictionary['fullname_delete']}'")
    connect.commit()

def add_b(dictionary):
    cursor.execute(f"insert into bus (type, numbers) values ({dictionary['type_bus']}, '{dictionary['number_bus_a']}');")
    cursor.execute(f"insert into bus_route(idbus, numberroute) values ((select max(id) from bus) + 1, {dictionary['num_route']});")
    connect.commit()

def delete_b(dictionary):
    cursor.execute(f"delete from bus where numbers = '{dictionary['number_bus']}'")
    connect.commit()
dictionary = {'key_d' : 3, 'route' : True, 'bus' : False, 'key_p' : "3, 149", 'st_time' : "00:00", 'end_time' : "00:00", 'interval' : "00:00", 'number_route_a' : 0, 'length' : 0}
def add_r(dictionary):
    cursor.execute(f"insert into way (number, length) values ({dictionary['number_route_a']}, {dictionary['length']});")
    cursor.execute(f"insert into route (st_time, end_time, number, interval_r) values ('{dictionary['st_time']}', '{dictionary['end_time']}', {dictionary['number_route_a']}, '{dictionary['interval']}');")
    connect.commit()

def delete_r(dictionary):
    cursor.execute(f"delete from route where number = {dictionary['number_route_d']}")
    cursor.execute(f"delete from way where number = {dictionary['number_route_d']}")
    connect.commit()

def update_r(dictionary):
    cursor.execute(f"update way set length = {dictionary['new_distance']} where number = {dictionary['number_route']}")
    connect.commit()

def register(dictionary):
    pass

def print_s(num):
    if num in (1, 11):
        d = open("водители_справка.txt", "w")
        data = "                                        Справка о водителях\n\n\n"
        cursor.execute(f"select fullname, class from driver;")
        for i in cursor.fetchall():
            data += f"""* {i[0]}, класс - {i[1]}""" + "\n\n"
        data += "\n\nДиспетчер: _______________             Дата: _______________           Роспись: _______________"
        d.write(data)
        d.close()
    elif num in (2, 12):
        d = open("маршруты_справка.txt", "w")
        data = "                                        Справка о маршрутах\n\n\n"
        data.center(len(data)+60, '*')
        cursor.execute(f"select st_time, end_time, number, interval from route;")
        for i in cursor.fetchall():
            data += f"""* Маршрут - №{i[2]}, время  движения: ({str(i[0])[0:5]} / {str(i[1])[0:5]}), интервал: {str(i[3])[0:5]}""" + "\n\n"
        data += "\n\nДиспетчер: _______________             Дата: _______________           Роспись: _______________"
        d.write(data)
        d.close()
    else:
        d = open("автобусы_справка.txt", "w")
        cursor.execute(f"select count(*) from bus;")
        data = "                                        Справка об автобусах\n\n\n"
        data.center(len(data)+60, '*')
        data += f"Всего автобусов - {cursor.fetchall()[0][0]}\n\n"
        cursor.execute(f"select type, numbers from bus;")
        for i in cursor.fetchall():
            cursor.execute(f"select capacity from typebus where type = {i[0]}")
            data += f"""* Номер автобуса - {i[1]}, тип: {i[0]}, вместимость: {cursor.fetchall()[0][0]}""" + "\n\n"
        data += "\n\nДиспетчер: _______________             Дата: _______________           Роспись: _______________"
        d.write(data)
        d.close()

