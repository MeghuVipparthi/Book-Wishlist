from dataclasses import dataclass

TITLE_MAX = 160
AUTHOR_MAX = 120


@dataclass
class BookForm:
    title: str
    author: str
    notes: str | None = None

    @classmethod
    def from_dict(cls, d: dict):
        title = (d.get("title") or "").strip()
        author = (d.get("author") or "").strip()
        notes = (d.get("notes") or "").strip() or None
        return cls(title=title, author=author, notes=notes)
