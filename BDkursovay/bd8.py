import PySimpleGUI as sg
import config, layout, math


window = sg.Window('Автопарк', layout.layout)

layout = 1
while True:
    event, values = window.read()
    if event in (None, 'Exit'):
        break
    if event in ('1', '11', '2', '12', '3', '13', '14'):
        window[f'-COL{layout}-'].update(visible=False)
        layout = int(event)
        window[f'-COL{layout}-'].update(visible=True)
    if event in ('141', '142', '143', '241', '242', '243', '341', '342', '343'):
        window[f'-COL{layout}-'].update(visible=False)
        layout = int(int(event) / 10)
        window[f'-COL{layout}-'].update(visible=True)
    if event == 'print':
        config.print_s(layout)


    if event == 'search_d':
        window['out_driver'].Update(config.driver_search(values))
    if event == 'select_d':
        window['out_driver'].Update(config.driver_select())
    if event == 'search_d_p':
        if values['route']:
            window['out_driver_1'].Update(config.driver_p(values))
        else:
            window['out_driver_2'].Update(config.driver_p(values))

    if event == 'search_r':
        window['out_route'].Update(config.route_search(values))
    if event == 'select_r':
        window['out_route'].Update(config.route_select())
    if event == 'search_r_p':
        window['out_route_1'].Update(config.route_p(values))

    if event == 'search_b':
        window['out_bus'].Update(config.bus_search(values))
    if event == 'select_b':
        window['out_bus'].Update(config.bus_select())
    if event == 'search_b_p':
        if values['route_l3']:
            window['out_bus_2'].Update(config.bus_p(values))
        else:
            window['out_bus_1'].Update(config.bus_p(values))

    if event == 'add_d':
        config.add_d(values)
        window['fullname'].Update('')
        window['expirience'].Update('')
        window['class'].Update('')
        window['salary'].Update('')
        window['number_bus_add'].Update('')
    if event == 'delete_d':
        config.delete_d(values)
        window['fullname_delete'].Update('')

    if event == 'add_r':
        config.add_r(values)
        window['st_time'].Update('')
        window['end_time'].Update('')
        window['number_route_a'].Update('')
        window['interval'].Update('')
        window['length'].Update('')
    if event == 'delete_r':
        config.delete_r(values)
        window['number_route_d'].Update('')
    if event == 'update_r':
        config.update_r(values)
        window['new_distance'].Update('')
        window['number_route'].Update('')
        
window.close()
