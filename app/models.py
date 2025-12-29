from app.extentions import db 
from enum import Enum 
from werkzeug.security import generate_password_hash, check_password_hash 
from datetime import datetime 

class OrderStatus(str, Enum):

    CANCELLED = 'cancelled'
    PENDING = 'pending'
    COMPLETED = 'completed'


class User(db.Model):

    __tablename__='users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False, unique=True, index=True)
    password_hash = db.Column(db.String(200), nullable=False) 
    is_admin = db.Column(db.Boolean, nullable=False, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow , nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow , nullable=False, onupdate=datetime.utcnow)

    orders = db.relationship('orders', back_populate='user', lazy='dynamic')


    def set_password(self, password):

        self.password_hash = generate_password_hash(password)

    def check_password(self, password):

        return check_password_hash(self.password_hash, password)


    def __repr__(self):

        return f'<User {self.email}>'
    
class Order(db.Model):
    
    __tablename__= 'orders'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), index=True)
    status = db.Column(db.String(), nullable=False, default = OrderStatus.PENDING.value)
    total = db.Column(db.Numeric(10, 2), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow , nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow , nullable=False, onupdate=datetime.utcnow)

    user = db.relationship('User', back_populate='orders')
    orders = db.relationship('OrderItem', back_populate='order', lazy='dynamic', cascade='all, delete-orphan')

    def calculate_total(self):

        return sum(self.Quantity * item.price for item in self.items.all())

    
    def __repr__(self):

        return f'<Order {self.item} - {self.status}>'

class OrderItem(db.Model):

    __tablename__ = 'order_items' 

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False,  index=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False,  index=True)
    quantity = db.Column(db.Integer, nullable=False, default=1)
    price = db.Column(db.Numeric(10, 2), nullabl=False)

    product = db.relationship('Product', back_populate='order_items')
    order = db.relationship('Order', back_populate='items')

    def subtotal(self):

        return self.quantity * self.price

    def __repr__(self):

        return f'<OrderItem Order:{self.order_id} Product:{self.product_id} Quantity:{self.quantity}>'



class Product(db.Model):

    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name= db.column(db.String(60), nullable=False) 
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Numeric(10, 2), nullable=False, default=0)
    stock = db.Column(db.Integer, nullable=False, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow , nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow , nullable=False, onupdate=datetime.utcnow)

    order_items = db.relationship('OrderItem', back_populat='product', lazy='dynamic')

    def __repr__(self):
        return f'<Product {self.name}>'









    












