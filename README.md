# Tripmakur Free Starter Website

A free starter version of the Tripmakur travel planning website built with Flask.

## Local setup

```bash
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000

## Render setup

Create a new Web Service on Render and use:

**Build Command**
```bash
pip install -r requirements.txt
```

**Start Command**
```bash
gunicorn app:app
```

## Files

- `app.py` - Flask app and destination matching logic
- `templates/` - HTML pages
- `static/style.css` - website styling
