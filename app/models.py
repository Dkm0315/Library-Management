from datetime import datetime
from app import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    stock = db.Column(db.Integer, default=0)
    transactions = db.relationship('Transaction', backref='book', lazy='dynamic')

    def __repr__(self):
        return f'<Book {self.title}, Author {self.author}>'

class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    debt = db.Column(db.Float, default=0.0)
    transactions = db.relationship('Transaction', backref='member', lazy='dynamic')

    def __repr__(self):
        return f'<Member {self.name}>'

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer, db.ForeignKey('member.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    date_issued = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    date_returned = db.Column(db.DateTime)
    rent_fee = db.Column(db.Float, default=0.0)

    def __repr__(self):
        return (f'<Transaction {self.id} - Book ID {self.book_id} '
                f'Issued to Member ID {self.member_id} on {self.date_issued.strftime("%Y-%m-%d")} '
                f'Returned: {"Yes" if self.date_returned else "No"}>')
