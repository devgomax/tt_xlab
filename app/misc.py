import aredis

from .configs.da_data import ddata
from .configs.models import Country
from .configs.redis import cached

cache = aredis.StrictRedis().cache('country_info')


@cached(cache)
async def get_country_info(country: str):
    data = await ddata.suggest('country', country, count=1)
    return Country(**data[0])
