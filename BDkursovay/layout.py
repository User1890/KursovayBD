import PySimpleGUI as sg

font = ("Calibri", 11)
sg.set_options(font=font)

layout0 = [
    [sg.Text("Логин", font = ("Calibri", 11,'bold'))],
    [sg.InputText(size=(20,15), key = 'log')],
    [sg.Text("Пароль", font = ("Calibri", 11,'bold'))],
    [sg.InputText(size=(20,15), key = 'pas')],
    [sg.Button('Войти', size=(17,1), key = 'auth', font = ("Calibri", 11,'bold'))],
    [sg.Button('Зарегистрироваться', size=(17,1), key = 'reg', font = ("Calibri", 11,'bold'))]
]

layout1 = [
    [sg.Text('  ФИО  '), sg.InputText( key = ("key")),
     sg.Button('Поиск', key="search_d")
    ],
    [sg.Text('', size=(39,1)), sg.Button('      Просмотр      ', key="select_d")],
    [sg.Text('', size=(39,1)), sg.Button('      Справка          ', key="11")],
    [sg.Output(size=(60,20),key='out_driver')]
]

layout11 = [
    [sg.Text('Ключ'), sg.InputText( key = ("key_d")),
     sg.Button('Поиск', key="search_d_p"),
     sg.R('Маршруты', 1, key = 'route'),
     sg.R('Автобусы', 1, key = 'bus')
    ],
    [sg.Text('При выборе "Маршрут" введите номер маршрута\nПри выборе "Автобусы" введите имя водителя')],
    [sg.Output(size=(40,20),key='out_driver_1'), sg.Output(size=(40,20),key='out_driver_2')]
]

layout2 = [
    [sg.Text('Номер'), sg.InputText( key = ("key")),
    sg.Button('Поиск', key="search_r")
    ],
    [sg.Text('', size=(39,1)), sg.Button('      Просмотр      ', key="select_r")],
    [sg.Text('', size=(39,1)), sg.Button('      Справка          ', key="12")],
    [sg.Output(size=(60,20),key='out_route')]
]

layout12 = [[sg.Text('Ключ'), sg.InputText( key = ("key_p")),
     sg.Button('Поиск', key="search_r_p"),
    ],
    [sg.Text('Введите номер маршрута или номера нескольких маршрутов\nПример: 1, 2, 3')],
    [sg.Output(size=(60,20),key='out_route_1')]
]

layout3 = [
    [sg.Text('Номер'), sg.InputText( key = ("key")),
    sg.Button('Поиск', key="search_b", )
    ],
    [sg.Text('', size=(39,1)), sg.Button('      Просмотр      ', key="select_b")],
    [sg.Text('', size=(39,1)), sg.Button('      Справка          ', key="13")],
    [sg.Output(size=(60,20),key='out_bus')]
]

layout13 = [[sg.Text('Ключ'), sg.InputText( key = ("key_b")),
     sg.Button('Поиск', key="search_b_p"),
     sg.R('Расписание', 2, key = 'time'),
     sg.R('Маршрут', 2, key = 'route_l3')
    ],
    [sg.Text('Введите номер маршрута')],
    [sg.Output(size=(40,20),key='out_bus_1'), sg.Output(size=(40,20),key='out_bus_2')]
]

layout14 = [
    [sg.Button('Водители', key="141"), sg.Button('Маршруты', key="241"), sg.Button('Автобусы', key="341")],
    [sg.Text("Добавить водителя", font = ("Calibri", 11,'bold'))],
    [sg.Text("Имя водителя                           "),sg.Text("Опыт работы        "),sg.Text("Класс водителя   "),sg.Text("Заработная плата")],
    [sg.InputText(size=(25,10), key = ("fullname")), sg.InputText(size=(15,10), key = ("expirience")), 
     sg.InputText( size=(15,10),key = ("class")), sg.InputText(size=(15,10), key = ("salary"))], 
    [sg.Text("Номер автобуса"),sg.InputText(size=(15,10), key = ("number_bus_add")), sg.Button('Добавить', key="add_d")],
    [sg.Text("")],
    [sg.Text("Уволить водителя", font = ("Calibri", 11,'bold'))],
    [sg.Text("Имя водителя")],
    [sg.InputText(size=(25,10), key = ("fullname_delete")), sg.Button('Уволить', key="delete_d")],
    [sg.Text("")],
    [sg.Text("")]
    ]

layout24 = [
    [sg.Button('Водители', key="142"), sg.Button('Маршруты', key="242"), sg.Button('Автобусы', key="342")],
    [sg.Text("Добавить новый маршрут", font = ("Calibri", 11,'bold'))],
    [sg.Text("Начало маршрута"), sg.Text("Окончание маршрута"), sg.Text("Номер маршрута"), sg.Text("Интервал"), sg.Text("Протяженность")],
    [sg.InputText(size=(17,10), key = ("st_time")),sg.InputText(size=(19,10), key = ("end_time")), sg.InputText(size=(16,10), key = ("number_route_a")), sg.InputText(size=(9,10), key = ("interval")), sg.InputText(size=(12,10), key = ("length")), sg.Button('Добавить', key="add_r")],
    [sg.Text("")],
    [sg.Text("Удалить маршрут", font = ("Calibri", 11,'bold'))],
    [sg.Text("Номер маршрута")],
    [sg.InputText(size=(15,10), key = ("number_route_d")), sg.Button('Удалить', key="delete_r")],  
    [sg.Text("")],
    [sg.Text("Изменить протяжённость маршрута", font = ("Calibri", 11,'bold'))],
    [sg.Text("Номер маршрута "), sg.Text("Протяженность")],
    [sg.InputText(size=(15,10), key = ("number_route")),sg.InputText(size=(15,10), key = ("new_distance")), sg.Button('Обновить', key="update_r")]

]

layout34 = [
    [sg.Button('Водители', key="143"), sg.Button('Маршруты', key="243"), sg.Button('Автобусы', key="343")],
    [sg.Text("Добавить автобус", font = ("Calibri", 11,'bold'))],
    [sg.Text("Номер автобуса"), sg.Text("Тип автобуса        "), sg.Text("Рабочий маршрут")],
    [sg.InputText(size=(15,10), key = ("number_bus_a")), sg.InputText(size=(15,10), key = ("type_bus")), sg.InputText(size=(15,10), key = ("num_route")), sg.Button('Добавить', key="add_b")],
    [sg.Text("")],
    [sg.Text("Списать автобус", font = ("Calibri", 11,'bold'))],
    [sg.Text("Номер автобуса")],
    [sg.InputText(size=(15,10), key = ("number_bus")), sg.Button('Списать', key="delete_b")],
    [sg.Text("")],
    [sg.Text("")],
    [sg.Text("")]
]

layout = [[sg.Column(layout1, key='-COL1-'), sg.Column(layout11, visible=False, key='-COL11-'), sg.Column(layout2, visible=False, key='-COL2-'), sg.Column(layout12, visible=False, key='-COL12-'), sg.Column(layout3, visible=False, key='-COL3-'), sg.Column(layout13, visible=False, key='-COL13-'), sg.Column(layout14, visible=False, key='-COL14-'),sg.Column(layout24, visible=False, key='-COL24-'),sg.Column(layout34, visible=False, key='-COL34-')],
          [sg.Button('Водители', key = '1'), sg.Button('Маршруты', key='2'), sg.Button('Автобусы',key='3'), sg.Button('Редактирование',key='14'), sg.Button('Печать', key='print')]]

