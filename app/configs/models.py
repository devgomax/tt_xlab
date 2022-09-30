from pydantic import BaseModel


class CountryData(BaseModel):
    code: int
    alfa2: str
    alfa3: str
    name_short: str
    name: str


class Country(BaseModel):
    value: str
    unrestricted_value: str
    data: CountryData
