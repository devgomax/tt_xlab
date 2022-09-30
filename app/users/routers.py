from fastapi import APIRouter, HTTPException, Body

from app.configs.db import collection
from app.misc import get_country_info
from .models import User, UserOut
from .serializers import UserSerializer, UserOutSerializer

users = APIRouter()


@users.post('/save_user_data', response_model=User)
async def save_user_data(user: User):
    entity = collection.find_one_and_update(
        {'phone_number': user.phone_number},
        UserSerializer.to_mongo_entity(user),
        return_document=True,
        upsert=True
    )
    return UserSerializer.get_obj_from_db(entity)


@users.post('/get_user_data', response_model=UserOut)
async def get_user_data(phone_number: str = Body(regex=r'^7\d{10}$')):
    user = collection.find_one({'phone_number': phone_number})
    if not user:
        raise HTTPException(status_code=404, detail='User not found')
    entity = UserOutSerializer.get_obj_from_db(user)
    country_info = await get_country_info(entity.country)
    entity.country_code = country_info.data.code
    return entity


@users.post('/delete_user_data', status_code=204)
async def delete_user_data(phone_number: str):
    user = collection.find_one_and_delete({'phone_number': phone_number})
    if not user:
        raise HTTPException(status_code=404, detail='User not found')
    return {'detail': 'success'}
