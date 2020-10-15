from shop import db

class Brand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)

    def __repr__(self):
        return '<Brand %r>' % self.name

    def __str__(self):
        return '<Brand %r>' % self.name

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)

    def __repr__(self):
        return '<Category %r>' % self.name

    def __str__(self):
        return '<Category %r>' % self.name

db.create_all()
