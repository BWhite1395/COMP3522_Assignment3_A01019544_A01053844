from request import Request
from pokeretriever.pokemon import PokedexObject
import http.client
import json
import requests
import asyncio


class PokeDexSearcher:
    def __init__(self):
        pass

    def execute_request(self, request: Request) -> PokedexObject:
        payload = ""
        url = "http://pokeapi.co/api/v2/"
        if request.inputdata:
            url += str(request.mode+"/")
            url += str(request.inputdata+"/")
        else:
            for item in request.inputdata_list:
                print(item)
                #asyncio.gather()
        response = requests.request("GET", url, data=payload)

        data = response.json()
        # print(data)
        p = None #PokedexObject()
        return p