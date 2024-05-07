from pydantic import BaseModel, ConfigDict


class ProductBase(BaseModel):

    name: str
    price: int
    description: str
    counts: int
    category_id: int


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    pass


class ProductUpdatePartial(ProductBase):
    name: str | None = None
    price: int | None = None
    description: str | None = None
    counts: int | None = None
    category_id: int | None = None


class Product(ProductBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
