from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String(10))
    age = db.Column(db.Integer)
    height = db.Column(db.Float)
    weight = db.Column(db.Float)
    favorite_foods = db.relationship('FavoriteFood', backref='user', lazy=True)

    records = db.relationship('Record', backref='user', lazy=True)

class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    record_date = db.Column(db.Date)
    weight = db.Column(db.Float)
    total_calorie = db.Column(db.Float)
    total_salt = db.Column(db.Float)
    total_protein = db.Column(db.Float)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    food_items = db.relationship('FoodItem', backref='record', lazy=True)

class FoodItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    calorie = db.Column(db.Float)
    protein = db.Column(db.Float)  # ← 追加！
    salt = db.Column(db.Float)
    time = db.Column(db.Time)

    record_id = db.Column(db.Integer, db.ForeignKey('record.id'), nullable=False)


class FavoriteFood(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    calorie = db.Column(db.Float)
    salt = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

