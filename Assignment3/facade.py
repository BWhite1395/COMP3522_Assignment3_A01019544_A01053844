from request import Request
from pokeretriever.pokemon import PokedexObject
import http.client
import json
import requests
import asyncio
import aiohttp


class PokeDexSearcher:
    def __init__(self):
        pass

    async def execute_request(self, url, session: aiohttp.ClientSession) -> PokedexObject:
        response = await session.request("GET", url)
        print("Response object from aiohttp:\n", response)
        data = await response.json()
        # print(data)
        p = None #PokedexObject()
        return p


    async def process_single_request(self, pargs):
        """
        This function depicts the use of await to showcase how one async
        coroutine can await another async coroutine
        :param id_: an int
        :return: dict, json response
        """
        request = Request(pargs)
        url = "http://pokeapi.co/api/v2/"
        if request.inputdata:
            url += str(request.mode + "/")
            url += str(request.inputdata + "/")
        async with aiohttp.ClientSession() as session:
            print("process_single_request")
            response = await self.execute_request(url, session)
            print(response)
            return response

    async def process_requests(self, pargs):
        """
        This function depicts the use of asyncio.gather to run multiple
        async coroutines concurrently.
        :param requests: a list of int's
        :return: list of dict, collection of response data from the endpoint.
        """
        r = Request(pargs)
        url = "http://pokeapi.co/api/v2/"
        url += str(r.mode + "/")
        url_list = [(url + x) for x in r.inputdata_list]
        async with aiohttp.ClientSession() as session:
            print("***process_requests")
            async_coroutines = [self.execute_request(url, session)
                                for url in url_list]

            responses = await asyncio.gather(*async_coroutines)

            for response in responses:
                print(response)
            return responses
