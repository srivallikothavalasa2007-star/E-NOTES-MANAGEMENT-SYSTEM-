from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(_name_)

# Temporary storage for notes (in-memory)
notes = []

# Home page - show all notes
@app.route('/')
def home():
    page = """
    <h1>E-NOTES MANAGEMENT SYSTEM</h1>
    <a href='/add'>Add New Note</a>
    <hr>
    <h2>All Notes</h2>
    {% for note in notes %}
        <div style="border:1px solid #aaa; padding:10px; margin:10px;">
            <h3>{{ note.title }}</h3>
            <p>{{ note.content }}</p>
        </div>
    {% else %}
        <p>No notes yet. Add one!</p>
    {% endfor %}
    """
    return render_template_string(page, notes=notes)

# Add a new note
@app.route('/add', methods=['GET', 'POST'])
def add_note():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        notes.append({'title': title, 'content': content})
        return redirect(url_for('home'))
    page = """
    <h1>Add Note</h1>
    <form method='post'>
        <label>Title:</label><br>
        <input type='text' name='title'><br><br>
        <label>Content:</label><br>
        <textarea name='content' rows='5' cols='40'></textarea><br><br>
        <input type='submit' value='Save'>
    </form>
    <br>
    <a href='/'>Back to Home</a>
    """
    return render_template_string(page)

if _name_ == '_main_':
    app.run(debug=True)