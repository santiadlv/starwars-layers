import httpx
import asyncio


def sort_by_id(movies: list) -> list:
    return movies.sort(key=lambda x: x['id'])

async def get_character_name(client: httpx.AsyncClient, url: str) -> str:
    response = await client.get(url)
    character = response.json()
    return character['name']

async def get_all_movie_character_names(urls: list) -> list:
    async with httpx.AsyncClient() as client:
        tasks = []
        for url in urls:
            tasks.append(asyncio.ensure_future(get_character_name(client, url)))
            
        character_names = await asyncio.gather(*tasks)
        return character_names
