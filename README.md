# Flask Webshop

A simple Flask application demonstrating session cookies and flash messages.

## Features

- ✅ **Session Management**: Track user visits and store data using Flask sessions
- 💬 **Flash Messages**: Display temporary messages with different categories (success, error, warning, info)
- 🎨 **Modern UI**: Clean, responsive design with smooth animations
- 🔒 **Secure**: Uses cryptographically secure secret keys for session management

## Setup

This project uses `uv` as the package manager.

### Install Dependencies

```bash
uv sync
```

### Run the Application

```bash
uv run python main.py
```

Or activate the virtual environment and run directly:

```bash
source .venv/bin/activate  # On Unix/macOS
# or
.venv\Scripts\activate     # On Windows

python main.py
```

The application will be available at `http://localhost:5000`

## Routes

- `/` - Home page showing session information
- `/form` - Form demo to submit data with flash messages
- `/trigger-flash` - Demonstrates different flash message types
- `/clear-session` - Clears all session data

## How It Works

### Session Cookies

Flask's session cookies are signed using a secret key. In this app:
- Visit counts are tracked automatically
- User data (like username) persists across requests
- Sessions are stored client-side in encrypted cookies

### Flash Messages

Flash messages are one-time notifications that appear after redirects:
- They're stored in the session temporarily
- Automatically cleared after being displayed
- Support categories: `success`, `error`, `warning`, `info`

## Development

The app runs in debug mode by default, which enables:
- Auto-reload on code changes
- Detailed error pages
- Debug toolbar

For production, set `debug=False` and use a proper WSGI server like Gunicorn.
