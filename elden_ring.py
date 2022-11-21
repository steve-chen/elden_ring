#!/usr/bin/env python3

import requests
import json

CONFIG_FILE_ARROW    = 'arrows.json'
CONFIG_FILE_WEAPONS  = 'weapons.json'
CONFIG_FILE_MONSTERS = 'monsters.json'

class EldenData:
    def fetch(self):
        "@brief Reaches out to the network to get the data"
        response = requests.get(self.data_url)
        print(f"Fetching data from {self.data_url}")
        return response.json()

    def dump(self):
        json_response = self.fetch()
        json.dump(json_response, open(self.filename, "w"))

    def load(self):
        return json.load(open(self.filename, "r"))

    def get(self, item_id):
        json_response = self.load()
        data = json_response['data']
        for item in data:
            if item_id == item['id']:
                return item
        return None

    def print_all(self):
        json_response = self.load()

        items = json_response['data']

        print(f"{json_response['count']} items")
        for index, item in enumerate(items):
            print("---")
            print(f"{index + 1}. {item['name']} ({item['id']})")
            print(f"{item['description']}")

class ArrowsData(EldenData):
    def __init__(self):
        self.data_url = "https://eldenring.fanapis.com/api/ammos"
        self.filename = CONFIG_FILE_ARROW

class WeaponsData(EldenData):
    def __init__(self):
        self.data_url = "https://eldenring.fanapis.com/api/weapons"
        self.filename = CONFIG_FILE_WEAPONS

class MonstersData(EldenData):
    def __init__(self):
        self.data_url = "https://eldenring.fanapis.com/api/creatures"
        self.filename = CONFIG_FILE_MONSTERS

def fetch_all():
    arrows = ArrowsData()
    arrows.dump()

    weapons = WeaponsData()
    weapons.dump()

    monsters = MonstersData()
    monsters.dump()

if __name__ == '__main__':
    fetch_all()
    #arrows = ArrowsData()
    #arrows.print_all()

    #weapons = WeaponsData()
    #weapons.print_all()
