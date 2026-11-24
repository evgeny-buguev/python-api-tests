from pydantic import BaseModel, ConfigDict, Field


class Address(BaseModel):
    model_config = ConfigDict(strict=True)

    city: str = Field(min_length=1)


class User(BaseModel):
    model_config = ConfigDict(strict=True)

    id: int = Field(gt=0)
    name: str = Field(min_length=1)
    email: str
    address: Address


class Post(BaseModel):
    model_config = ConfigDict(strict=True)

    id: int = Field(gt=0)
    title: str
    body: str
    userId: int = Field(gt=0)
