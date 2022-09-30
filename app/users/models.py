from datetime import datetime

from pydantic import BaseModel, constr, EmailStr


class User(BaseModel):
    name: constr(max_length=50, regex=r'^[а-яА-Я\s\-]+$')
    surname: constr(max_length=50, regex=r'^[а-яА-Я\s\-]+$')
    patronymic: constr(max_length=50, regex=r'^[а-яА-Я\s\-]+$') = None
    phone_number: constr(regex=r'^7\d{10}$')
    email: EmailStr = None
    country: constr(max_length=50, regex=r'^[а-яА-Я\s\-]+$')


class UserInDB(User):
    user_id: constr(min_length=12, max_length=12)
    date_created: datetime
    date_modified: datetime


class UserOut(User):
    country_code: int = None
