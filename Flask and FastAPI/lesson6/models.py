from pydantic import BaseModel
import datetime


class User(BaseModel):
  id: int
  name: str
  surname: str
  email: str
  password: str


class Order(BaseModel):
  id: int
  user_id: int
  product_id: int
  date_created: datetime
  status: str


class Product(BaseModel):
  id: int
  name: str
  description: str
  price: float