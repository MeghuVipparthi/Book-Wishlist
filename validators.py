from .forms import TITLE_MAX, AUTHOR_MAX


def validate_book_form(form) -> list[str]:
    errors = []
    if not form.title:
        errors.append("Title is required.")
    if len(form.title) > TITLE_MAX:
        errors.append(f"Title must be ≤ {TITLE_MAX} characters.")
    if not form.author:
        errors.append("Author is required.")
    if len(form.author) > AUTHOR_MAX:
        errors.append(f"Author must be ≤ {AUTHOR_MAX} characters.")
    return errors
