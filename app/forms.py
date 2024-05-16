from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, FloatField, SelectField
from wtforms.validators import DataRequired, NumberRange
from wtforms.fields.html5 import DateField

class BookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    stock = IntegerField('Stock', validators=[DataRequired(), NumberRange(min=0, message='Stock cannot be negative')])
    submit = SubmitField('Add/Update Book')

class MemberForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Add/Update Member')

class IssueForm(FlaskForm):
    member_id = SelectField('Member', coerce=int, validators=[DataRequired()])
    book_id = SelectField('Book', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Issue Book')

class ReturnForm(FlaskForm):
    transaction_id = SelectField('Transaction', coerce=int, validators=[DataRequired()])
    return_date = DateField('Return Date', format='%Y-%m-%d', validators=[DataRequired()])
    rent_fee = FloatField('Rent Fee', validators=[DataRequired()])
    submit = SubmitField('Return Book')

class SearchForm(FlaskForm):
    search = StringField('Search by Title or Author', validators=[DataRequired()])
    submit = SubmitField('Search')
