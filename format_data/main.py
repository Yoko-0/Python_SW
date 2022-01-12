import json
from utils.db import Database
from init_db import init_table

valid_types = ['ethernet', 'port-channel']
table_name = 'format_data'

def read_json(filename):
    with open(filename, 'r') as read_file:
        data = json.load(read_file)
    return data

def check_table(db):
    command = """SELECT EXISTS (SELECT 1
    FROM information_schema.columns
    WHERE table_name = 'format_data');"""

    return db.custom_command(command)[0][0]

def upload_to_table(db, data):
    counter = 0
    for key, value in data.items():
        name = value['name']
        if 'description' in value.keys():
            description = value['description']
        else:
            description = 'None'
        config = value['config']
        type = value['type']
        if 'port_channel_id' in value.keys():
            port_channel_id = value['port_channel_id']
        else:
            port_channel_id = -1
        if 'mtu' in value.keys():
            mtu = value['mtu']
        else:
            mtu = -1
        db.insert(table_name, counter, 1, name,
            description, config, type, 'None', port_channel_id, mtu)
        counter += 1

def get_port_channels(data):
    formated_data = {}
    for a in data['frinx-uniconfig-topology:configuration']['Cisco-IOS-XE-native:native']['interface']['TenGigabitEthernet']:
        if 'Cisco-IOS-XE-ethernet:channel-group' in a.keys():
            name = f'TenGigabitEthernet{a["name"]}'
            port_channel_id = a['Cisco-IOS-XE-ethernet:channel-group']['number']
            if name in formated_data.keys():
                formated_data[name]['port_channel_id'] = port_channel_id
            else:
                formated_data[name] = {'port_channel_id': port_channel_id}
    return formated_data

def parse(interface):
    data = {
        'name': interface['name'],
    }
    if 'ethernet' in interface['name'].lower():
        data['type'] = 'ethernet'
    if 'port-channel' in interface['name'].lower():
        data['type'] = 'port-channel'

    if 'config' in interface.keys():
        config = interface['config']
        if 'mtu' in config.keys():
            data['mtu'] = config['mtu']

        if 'description' in config.keys():
            data['description'] = config['description']

    data['config'] = json.dumps(data)
    return data


def parse_loopback(interface):
    pass

def parse_bdi(interface):
    pass

def parse_data(data, formated_data):
    interfaces = data['frinx-uniconfig-topology:configuration']['openconfig-interfaces:interfaces']
    for interface in interfaces['interface']:
        name = interface['name']
        if 'port-channel' in name.lower():
            parsed_interface = parse(interface)
        elif 'ethernet' in name.lower():
            parsed_interface = parse(interface)
        # elif 'loopback' in name.lower():
        #     parsed_interface = parse_loopback(interface)
        # elif 'bdi' in name.lower():
        #     parsed_interface = parse_bdi(interface)
        else:
            continue

        if name in formated_data.keys():
            formated_data[name] = {**formated_data[name], **parsed_interface}
        else:
            formated_data[name] = parsed_interface

    return formated_data



if __name__ == '__main__':
    # parse data
    # get parsed data
    #
    # connect to database
    # check table exists
    # init table in need
    # push parsed data to database

    data = read_json('src/configClear_v2.json')
    formated_data = get_port_channels(data)
    formated_data = parse_data(data, formated_data)

    db = Database()
    exists_table = check_table(db)

    if not exists_table:
        res = init_table()
        if not res:
            print('Init table failed, please try again.')
        else:
            print('Init table successfully.')

    upload_to_table(db, formated_data)







# ошибка импорта json файла в некорректной запятой последнего элемента массива 1890 строка
