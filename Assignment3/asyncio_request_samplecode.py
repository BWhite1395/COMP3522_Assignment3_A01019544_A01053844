"""
This module depicts the use of asyncio and aiohttp to make HTTP GET
requests.
"""
import aiohttp
import asyncio


async def get_starwars_people_data(id_: int, url: str, session: aiohttp.ClientSession) -> dict:
    """
    An async coroutine that executes GET http request. The response is
    converted to a json. The HTTP request and the json conversion are
    asynchronous processes that need to be awaited.
    :param id_: an int
    :param url: a string, the unformatted url (missing parameters)
    :param session: a HTTP session
    :return: a dict, json representation of response.
    """
    target_url = url.format(id_)
    response = await session.request(method="GET", url=target_url)
    print("Response object from aiohttp:\n", response)
    print("Response object type:\n", type(response))
    print("-----")
    json_dict = await response.json()
    return json_dict


async def process_single_request(id_) -> dict:
    """
    This function depicts the use of await to showcase how one async
    coroutine can await another async coroutine
    :param id_: an int
    :return: dict, json response
    """
    url = "https://swapi.co/api/people/{}/"
    async with aiohttp.ClientSession() as session:
        print("***process_single_request")
        response = await get_starwars_people_data(id_, url, session)
        print(response)
        return response


async def process_requests(requests: list) -> list:
    """
    This function depicts the use of asyncio.gather to run multiple
    async coroutines concurrently.
    :param requests: a list of int's
    :return: list of dict, collection of response data from the endpoint.
    """
    url = "https://swapi.co/api/people/{}/"
    async with aiohttp.ClientSession() as session:
        print("***process_requests")
        async_coroutines = [get_starwars_people_data(id_, url, session)
                            for id_ in requests]

        responses = await asyncio.gather(*async_coroutines)

        for response in responses:
            print(response)
        return responses


async def process_single_request_task(id_: int) -> list:
    """
    Thsi function depicts how an async coroutine can be converted into
    a task object and awaited.
    :param id_: an int
    :return:
    """
    url = "https://swapi.co/api/people/{}/"
    async with aiohttp.ClientSession() as session:
        print("***process_single_request_task")
        coroutine = get_starwars_people_data(id_, url, session)
        async_task = asyncio.create_task(coroutine)
        response = await async_task
        print(response)
        return response


async def process_requests_tasks(requests: list) -> list:
    """
    This function depicts the use of asyncio.gather to run multiple
    async tasks concurrently.
    :param requests: a list of int's
    :return: list of dict, collection of response data from the endpoint.
    """
    url = "https://swapi.co/api/people/{}/"
    async with aiohttp.ClientSession() as session:
        print("***process_requests_tasks")
        list_tasks = [asyncio.create_task(get_starwars_people_data(id_, url, session))
                 for id_ in requests]
        responses = await asyncio.gather(*list_tasks)
        for response in responses:
            print(response)
        return responses

def main():

    # prior to Python 3.8 aiohttp worked with this approach
    # requests = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # response = asyncio.run(process_single_request(1))
    # response2 = asyncio.run(process_single_request_task(2))
    # responses = asyncio.run(process_requests(requests))
    # responses2 = asyncio.run(process_requests_tasks(requests))


    loop = asyncio.get_event_loop()

    response = loop.run_until_complete(process_single_request(1))
    response2 = loop.run_until_complete(process_single_request_task(2))
    requests = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    responses = loop.run_until_complete(process_requests(requests))
    responses2 = loop.run_until_complete(process_requests_tasks(requests))


if __name__ == '__main__':
    main()