from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from pydantic import BaseModel



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/shop'
db = SQLAlchemy(app)


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


@app.route('/users', methods=['GET', 'POST'])
def users():
  if request.method == 'GET':
    users = db.session.query(User).all()
    return {'users': [user.dict() for user in users]}

  if request.method == 'POST':
    user = User.parse_obj(request.json)
    db.session.add(user)
    db.session.commit()
    return {'user': user.dict()}


@app.route('/orders', methods=['GET', 'POST'])
def orders():
  if request.method == 'GET':
    orders = db.session.query(Order).all()
    return {'orders': [order.dict() for order in orders]}

  if request.method == 'POST':
    order = Order.parse_obj(request.json)
    db.session.add(order)
    db.session.commit()
    return {'order': order.dict()}


@app.route('/products', methods=['GET', 'POST'])
def products():
  if request.method == 'GET':
    products = db.session.query(Product).all()
    return {'products': [product.dict() for product in products]}

  if request.method == 'POST':
    product = Product.parse_obj(request.json)
    db.session.add(product)
    db.session.commit()
    return {'product': product.dict()}


if __name__ == '__main__':
  app.run()