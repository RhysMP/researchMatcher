from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import ARRAY
import os
from werkzeug.utils import secure_filename
from sqlalchemy.exc import IntegrityError
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:Admin123@35.235.95.124:5432/postgres'
db = SQLAlchemy(app)

UPLOAD_FOLDER = "/Users/kaankoc/Desktop/test/sbhacksX/flask_server/images"
ALLOWED_EXTENSIONS = set(['txt', 'png', 'jpg', 'jpeg'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# Checks the image is in allowed format.
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(40))
    lname = db.Column(db.String(40))
    major = db.Column(db.String(40))
    skills = db.Column(ARRAY(db.String(40)))
    resume_text_ = db.Column(db.String()) ## resume will be converted to text. 


@app.route('/')
def index():
    return "<p>Hello, World!</p>"


@app.route('/students', methods=['GET'])
def get_all_students():
    students = Student.query.all()
    student_list = []
    for student in students:
        student_data = {
            'id': student.id,
            'fname': student.fname,
            'lname': student.lname,
            'major': student.major,
            'skills': student.skills,
            'resume_text_': student.resume_text_
        }
        student_list.append(student_data)
    return jsonify({'students': student_list}), 200

# Get a specific student by ID

@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    student = Student.query.get_or_404(student_id)
    data = request.get_json()

    student.fname = data['fname']
    student.lname = data['lname']
    student.major = data['major']
    student.skills = data['skills']
    student.resume_text_ = data['resume_text_']

    db.session.commit()

    return jsonify({'message': 'Student updated successfully'})



@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = Student.query.get(student_id)
    if student:
        student_data = {
           'id': student.id,
            'fname': student.fname,
            'lname': student.lname,
            'major': student.major,
            'skills': student.skills,
            'resume_text_': student.resume_text_
        }
        return jsonify({'student': student_data}), 200
    else:
        return jsonify({'message': 'Student not found'}), 404


@app.route('/students', methods=['POST'])
def create_student():
    data = request.get_json()

    new_student = Student(
        fname=data['fname'],
        lname=data['lname'],
        major=data['major'],
        skills=data['skills'],
        resume_text_=data['resume_text_']
    )

    db.session.add(new_student)

    try:
        db.session.commit()
        return jsonify({'message': 'Student created successfully'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Student with the same details already exists'}), 400

# Delete a student by ID


@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    student = Student.query.get(student_id)
    if student:
        db.session.delete(student)
        db.session.commit()
        return jsonify({'message': 'Student deleted successfully'}), 200
    else:
        return jsonify({'message': 'Student not found'}), 404


# Professor Model and CRUD operations

class Professor(db.Model):
    __tablename__ = 'professors'
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(40))
    lname = db.Column(db.String(40))
    image_path = db.Column(db.String(255))  # Store the image filename

    def __init__(self, fname, lname, image_path=None):
        self.fname = fname
        self.lname = lname
        self.image_path = image_path

@app.route('/professors', methods=['POST'])
def create_professor():
    data = request.form.to_dict()

    filename = upload_file()

    new_professor = Professor(
        fname=data['fname'],
        lname=data['lname'],
        image_path=f"{UPLOAD_FOLDER}/{filename}"  # Adjust this line based on your folder structure
    )
    db.session.add(new_professor)

    try:
        db.session.commit()
        return jsonify({'message': 'Professor created successfully'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Professor with the same details already exists'}), 400

def upload_file():
    if "file" not in request.files:
        return jsonify({'error': 'media not provided'}), 400
    file = request.files["file"]
    if file.filename == '':
        return jsonify({"error": "no file selected"}), 400
    if allowed_file(file.filename) == False:
        return jsonify({"error": "not the right format"}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return filename


@app.route('/professors', methods=['GET'])
def get_all_professors():
    professors = Professor.query.all()
    professor_list = []
    for professor in professors:
        professor_data = {
            'id': professor.id,
            'fname': professor.fname,
            'lname': professor.lname
        }
        professor_list.append(professor_data)
    return jsonify({'professors': professor_list}), 200


@app.route('/professors/<int:professor_id>', methods=['GET'])
def get_professor(professor_id):
    professor = Professor.query.get(professor_id)
    
    if professor:
        professor_data = {
            'id': professor.id,
            'fname': professor.fname,
            'lname': professor.lname,
            'image_path': professor.image_path
        }
        return jsonify({'professor': professor_data}), 200
    else:
        return jsonify({'message': 'Professor not found'}), 404

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
