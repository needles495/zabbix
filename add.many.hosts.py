#!/usr/bin/env python3
import requests
import json

url = "http://localhost:8080/api_jsonrpc.php"
authtoken = "secret_token_abc" # Zabbix 6.4.13
group_id = 23  # Идентификатор группы, в которую нужно добавить хост
db = {
    "hostname.example.org": "172.17.0.1",
    "hostname2.example.org": "172.17.0.2",
    "hostname3.example.org": "172.17.0.3"
} # список хостов, сервер:ip

def create_host(host_name, ip_address, group_id):
    req = requests.post(url,
        json={
            "jsonrpc": "2.0",
            "method": "host.create",
            "params": {
                "host": host_name,
                "interfaces": [
                    {
                        "type": 1,
                        "main": 1,
                        "useip": 1,
                        "ip": ip_address,
                        "dns": "",
                        "port": "10050"
                    }
                ],
                "groups": [
                    {
                        "groupid": str(group_id)
                    }
                ],
                "templates": []  # Укажите шаблоны, если нужно
            },
            "auth": authtoken,
            "id": 2
        }
    )
    result = req.json()
    print(host_name,ip_address)
    print(result)
    return result

for host_name,ip_address in db.items():
    response = create_host(host_name, ip_address, group_id)
