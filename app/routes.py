from flask import render_template, request, redirect, url_for, flash
from app import app, db
from app.models import Book, Member, Transaction
from app.forms import BookForm, MemberForm, IssueForm, ReturnForm, SearchForm
from datetime import datetime

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/books', methods=['GET', 'POST'])
def books():
    form = BookForm()
    if form.validate_on_submit():
        book = Book(title=form.title.data, author=form.author.data, stock=form.stock.data)
        db.session.add(book)
        db.session.commit()
        flash('Book added successfully!', 'success')
        return redirect(url_for('books'))
    books = Book.query.all()
    return render_template('books.html', form=form, books=books)

@app.route('/members', methods=['GET', 'POST'])
def members():
    form = MemberForm()
    if form.validate_on_submit():
        member = Member(name=form.name.data)
        db.session.add(member)
        db.session.commit()
        flash('Member added successfully!', 'success')
        return redirect(url_for('members'))
    members = Member.query.all()
    return render_template('members.html', form=form, members=members)

@app.route('/issue_book', methods=['GET', 'POST'])
def issue_book():
    form = IssueForm()
    form.member_id.choices = [(m.id, m.name) for m in Member.query.all()]
    form.book_id.choices = [(b.id, b.title) for b in Book.query.all()]
    if form.validate_on_submit():
        transaction = Transaction(member_id=form.member_id.data, book_id=form.book_id.data)
        db.session.add(transaction)
        db.session.commit()
        flash('Book issued successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('issue_book.html', form=form)

@app.route('/return_book/<int:transaction_id>', methods=['GET', 'POST'])
def return_book(transaction_id):
    transaction = Transaction.query.get_or_404(transaction_id)
    form = ReturnForm(obj=transaction)
    if form.validate_on_submit():
        transaction.date_returned = form.return_date.data
        transaction.rent_fee = form.rent_fee.data
        db.session.commit()
        flash('Book returned successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('return_book.html', form=form, transaction=transaction)

@app.route('/search', methods=['GET', 'POST'])
def search():
    form = SearchForm()
    books = []
    if form.validate_on_submit():
        search = "%{}%".format(form.search.data)
        books = Book.query.filter((Book.title.like(search)) | (Book.author.like(search))).all()
    return render_template('search.html', form=form, books=books)
