from request import Request
from pokeretriever.pokemon import *
import http.client
import json
import requests
import asyncio
import aiohttp


class PokeDexSearcher:
    def __init__(self, request):
        self.request = request

    async def execute_request(self, url, session: aiohttp.ClientSession) -> PokedexObject:
        response = await session.request("GET", url)
        data = await response.json()
        print(data.get("name"))
        if self.request.mode == "pokemon":
            if self.request.expanded:
                #p = PokemonStat(data.get("name"))
                pass
            else:
                pass
                #p = Pokemon()
        elif self.request.mode == "ability":
            pass
            #p = PokemonAbility()
        else:
            pass
            #p = PokemonMove()
        return data# p


    async def process_single_request(self, request):
        """
        Processes a single request
        :param pargs:
        :return:
        """
        url = "http://pokeapi.co/api/v2/"
        if request.inputdata:
            url += str(request.mode + "/")
            url += str(request.inputdata + "/")
        async with aiohttp.ClientSession() as session:
            print("process_single_request")
            response = await self.execute_request(url, session)
            print(response)
            return response

    async def process_requests(self, request):
        """

        :param request:
        :return:
        """
        url = "http://pokeapi.co/api/v2/"
        url += str(request.mode + "/")
        url_list = [(url + name) for name in request.inputdata_list]
        async with aiohttp.ClientSession() as session:
            print("***process_requests")
            async_coroutines = [self.execute_request(url, session)
                                for url in url_list]

            responses = await asyncio.gather(*async_coroutines)

            for response in responses:
                print(response)
            return responses
