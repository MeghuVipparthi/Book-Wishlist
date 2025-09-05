from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import Book
from .db import db
from .forms import BookForm
from .validators import validate_book_form

bp = Blueprint("routes", __name__)


@bp.route("/", methods=["GET"])
def index():
    status = request.args.get("status", "all")
    q = Book.query.order_by(Book.created_at.desc())
    if status in ("want", "reading", "finished"):
        q = q.filter_by(status=status)
    books = q.all()
    return render_template("index.html", books=books, status=status)


@bp.route("/book", methods=["POST"])
def create_book():
    form = BookForm.from_dict(request.form)
    errors = validate_book_form(form)
    if errors:
        for e in errors:
            flash(e, "error")
        return redirect(url_for("routes.index"))

    book = Book(title=form.title, author=form.author, notes=form.notes)
    db.session.add(book)
    db.session.commit()
    flash("Book added.", "success")
    return redirect(url_for("routes.index"))


@bp.route("/book/<int:book_id>/status", methods=["POST"])
def change_status(book_id):
    book = Book.query.get_or_404(book_id)
    next_status = request.form.get("status")
    if next_status in ("want", "reading", "finished"):
        book.status = next_status
        db.session.commit()
        flash("Book status updated.", "success")
    return redirect(url_for("routes.index"))


@bp.route("/book/<int:book_id>/edit", methods=["GET", "POST"])
def edit_book(book_id):
    book = Book.query.get_or_404(book_id)
    if request.method == "POST":
        form = BookForm.from_dict(request.form)
        errors = validate_book_form(form)
        if errors:
            for e in errors:
                flash(e, "error")
            return redirect(url_for("routes.edit_book", book_id=book.id))
        book.title = form.title
        book.author = form.author
        book.notes = form.notes
        db.session.commit()
        flash("Book updated.", "success")
        return redirect(url_for("routes.index"))
    return render_template("edit.html", book=book)


@bp.route("/book/<int:book_id>/delete", methods=["POST"])
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    flash("Book deleted.", "success")
    return redirect(url_for("routes.index"))
