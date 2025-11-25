from flask import Flask, render_template, request, redirect, url_for, flash, session
import secrets

app = Flask(__name__)
# Generate a secure secret key for session management
app.secret_key = secrets.token_hex(16)
app.debug = True

@app.context_processor
def inject_user_check():
    """Make user check available to all templates."""
    user = session.get('user')
    is_bart = user == 'bart' if user else False
    return {
        'current_user': user,
        'is_user_bart': is_bart,
        'user_check_status': 'User is Bart! ✓' if is_bart else 'User is not Bart' if user else 'No user set',
        'secret_key': app.secret_key
    }

@app.route('/')
def index():
    """Home page displaying flash messages."""
    # You can access session data here if needed
    visit_count = session.get('visit_count', 0)
    visit_count += 1
    session['visit_count'] = visit_count
    
    return render_template('index.html', visit_count=visit_count)

@app.route('/trigger-flash')
def trigger_flash():
    """Route to demonstrate flash messages."""
    flash('This is a success message!', 'success')
    flash('This is an info message.', 'info')
    flash('This is a warning message!', 'warning')
    return redirect(url_for('index'))

@app.route('/form', methods=['GET', 'POST'])
def form():
    """Example form with flash message on submission."""
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        user = request.form.get('user', '').strip()
        
        if name:
            session['username'] = name
            flash(f'Welcome, {name}! Your information has been saved.', 'success')
        
        if user:
            session['user'] = user
            if user == 'bart':
                flash(f'User set to "{user}" - You are Bart! 🎉', 'success')
            else:
                flash(f'User set to "{user}" - You are not Bart.', 'info')
        
        if name or user:
            return redirect(url_for('index'))
        else:
            flash('Please enter at least one field.', 'error')
    
    return render_template('form.html')

@app.route('/buy', methods=['GET', 'POST'])
def buy():
    """Buy endpoint - tries to parse product_id as int, will crash if not valid."""
    if request.method == 'POST':
        product_id_str = request.form.get('product_id', '')
        # This will raise ValueError if product_id is not a valid integer
        # triggering the Werkzeug debugger when debug=True
        product_id = int(product_id_str)
        flash(f'Successfully bought product {product_id}!', 'success')
        return redirect(url_for('index'))
    
    return render_template('buy.html')

@app.route('/set-user/<username>')
def set_user(username):
    """Quick route to set the user session variable."""
    session['user'] = username
    if username == 'bart':
        flash(f'User set to "{username}" - You are Bart! 🎉', 'success')
    else:
        flash(f'User set to "{username}" - You are not Bart.', 'info')
    return redirect(url_for('index'))

@app.route('/clear-session')
def clear_session():
    """Clear the session data."""
    session.clear()
    flash('Session cleared successfully!', 'info')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
