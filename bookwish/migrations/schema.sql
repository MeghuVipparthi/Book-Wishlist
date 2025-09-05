CREATE TABLE IF NOT EXISTS public.books (
  id SERIAL PRIMARY KEY,
  title VARCHAR(160) NOT NULL,
  author VARCHAR(120) NOT NULL,
  notes TEXT NULL,
  status VARCHAR(20) NOT NULL DEFAULT 'want',
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE OR REPLACE FUNCTION set_updated_at_books()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = NOW();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS trg_set_updated_at_books ON public.books;
CREATE TRIGGER trg_set_updated_at_books
BEFORE UPDATE ON public.books
FOR EACH ROW EXECUTE FUNCTION set_updated_at_books();
