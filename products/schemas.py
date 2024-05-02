from pydantic import BaseModel, ConfigDict


class PhoneBase(BaseModel):

    name: str
    price: int
    description: str
    counts: int


class ProductCreate(PhoneBase):
    pass


class Phone(PhoneBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
