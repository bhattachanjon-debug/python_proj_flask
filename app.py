from flask import Flask, render_template,abort
from db_connect import get_connection

app = Flask(__name__)

subjects = ['Python','Database','Data Science','Java']

conn = get_connection()

@app.route("/")
def index():
    return render_template('index.html',name='Jack', subjects=subjects)

@app.route("/about")
def about():
    return 'I am zoti. Welcome to my class.'

@app.route("/contact")
def contact():
    return render_template('contact.html',contact=9876352816)

@app.route("/students")
def students():
    with conn.cursor() as cur:
        cur.execute("SELECT * from student")
        students = cur.fetchall()
    return render_template('student.html',students=students)

@app.route("/courses")
def courses():
    with conn.cursor() as cur:
        cur.execute("SELECT * from student")
        courses = cur.fetchall()
    return render_template('student.html',courses=courses)

# @app.route("/students/<int:student_id>")
# def student_detail(student_id):
#     with conn.cursor() as cur:
#         cur.execute("SELECT * from student")
#         student = cur.fetchone()
#     if student  is None:
#         abort(404)
#     return render_template('student_detail.html',student=student)
@app.route("/students/<int:student_id>")
def student_detail(student_id):
    # Using dictionary=True makes the result easier to use in templates (student['name'])
    with conn.cursor(dictionary=True) as cur:
        # Use a parameterized query to prevent SQL Injection
        cur.execute("SELECT * FROM student WHERE id = %s", (student_id,))
        student = cur.fetchone()
        
        # Optional: If your query could still return multiple rows, 
        # call cur.fetchall() or use buffered=True to clear the buffer.
    
    if student is None:
        abort(404)
        
    return render_template('student_detail.html', student=student)

if __name__ == '__main__':
    app.run(debug=True)