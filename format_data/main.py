import json

def read_json(filename):
    with open(filename, 'r') as read_file:
        data = json.load(read_file)
    return data

def parse_data(data):
    interfaces = data['frinx-uniconfig-topology:configuration']['openconfig-interfaces:interfaces']
    for interface in interfaces['interface']:
        print(interface)
        print()
        # for a in data['frinx-uniconfig-topology:configuration']['Cisco-IOS-XE-native:native']['interface']['TenGigabitEthernet']:
        #     if 'Cisco-IOS-XE-ethernet:channel-group' in a.keys():
        #         print(a)

def parse_port_channels():
    pass


if __name__ == '__main__':
    data = read_json('src/configClear_v2.json')
    parsed_data = parse_data(data)





# ошибка импорта json файла в некорректной запятой последнего элемента массива
