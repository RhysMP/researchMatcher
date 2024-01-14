from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import ARRAY
import os
from werkzeug.utils import secure_filename
from sqlalchemy.exc import IntegrityError
from flask_cors import CORS
from pdf_reader import convert_pdf_to_text


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
    email = db.Column(db.String(60))
    field = db.Column(db.String(60))
    key_words = db.Column(ARRAY(db.String())) ## resume will be converted to text. 


@app.route('/')
def index():
    text = convert_pdf_to_text("/Users/kaankoc/Desktop/test/sbhacksX/flask_server/kaankoc_resume.pdf")
    return text



@app.route('/students', methods=['GET'])
def get_all_students():
    students = Student.query.all()
    student_list = []
    for student in students:
        student_data = {
            'id': student.id,
            'fname': student.fname,
            'lname': student.lname,
            'email': student.email,
            'field': student.field, 
            'key_words': student.key_words
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
    student.email = data['email']
    student.field = data['field']
    student.key_words = data['key_words']

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
            'email': student.email,
            'field': student.field, 
            'key_words': student.key_words
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
        email = data['email'],
        field = data['field'],
        key_words=data['key_words']
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


# @app.route('/create/student', methods=['POST'])
# def create_student_with_resume():
#     data = request.form.to_dict()

#     if 'file' not in request.files:
#         return 'No file part'

#     file = request.files['file']

#     if file.filename == '':
#         return 'No selected file'

#     text = convert_pdf_to_text(file)


#     new_student = Student(
#         fname=data['fname'],
#         lname=data['lname'],
#         email = data['email'],
#         phone_number = data['phone_number'],
#         resume_text_=text
#     )

#     db.session.add(new_student)

#     try:
#         db.session.commit()
#         return jsonify({'message': 'Student created successfully'}), 201
#     except IntegrityError:
#         db.session.rollback()
#         return jsonify({'error': 'Student with the same details already exists'}), 400



# Professor Model and CRUD operations

class Professor(db.Model):
    __tablename__ = 'professors'
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(40))
    lname = db.Column(db.String(40))
    field = db.Column(db.String(40))
    abstract = db.Column(db.String())
    image_path = db.Column(db.String(255))  # Store the image filename
    key_words = db.Column(ARRAY(db.String()))

    def __init__(self, fname, lname, field, image_path, key_words, abstract):
        self.fname = fname
        self.lname = lname
        self.field = field
        self.abstract = abstract
        self.image_path = image_path
        self.key_words = key_words
    

@app.route('/professors', methods=['POST'])
def create_professor():
    data = request.form.to_dict()

    filename = upload_file()
    key_words = request.form.getlist('key_words')
    print(key_words)

    new_professor = Professor(
        fname=data['fname'],
        lname=data['lname'],
        abstract=data['abstract'],
        image_path=f"{UPLOAD_FOLDER}/{filename}", # Adjust this line based on your folder structure
        field = data['field'],
        key_words=key_words
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
   # Check if 'field' parameter is provided in the request
    field_query = request.args.get('field')

    # ?field=desired_field

    if field_query:
        # If 'field' parameter is provided, filter professors by the specified field
        professors = Professor.query.filter_by(field=field_query).all()
    else:
        # If 'field' parameter is not provided, get all professors
        professors = Professor.query.all()

    professor_list = []
    for professor in professors:
        professor_data = {
            'id': professor.id,
            'fname': professor.fname,
            'lname': professor.lname,
            'abstract': professor.abstract,
            'image_path': professor.image_path,
            'field': professor.field,
            'key_words': professor.key_words
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
             'abstract': professor.abstract,
            'image_path': professor.image_path,
            'field': professor.field,
            'key_words': professor.key_words
        }
        return jsonify({'professor': professor_data}), 200
    else:
        return jsonify({'message': 'Professor not found'}), 404


@app.route('/professors/<int:professor_id>', methods=['DELETE'])
def delete_professor(professor_id):
    professor = Professor.query.get(professor_id)
    if professor:
        db.session.delete(professor)
        db.session.commit()
        return jsonify({'message': 'professor deleted successfully'}), 200
    else:
        return jsonify({'message': 'professor not found'}), 404

@app.route('/professors/<int:professor_id>', methods=['PUT'])
def update_professor(professor_id):
    professor = Professor.query.get_or_404(professor_id)

    # Get the updated data from the form
    updated_data = request.form.to_dict()

    # Update the professor object with the new data
    professor.fname = updated_data.get('fname', professor.fname)
    professor.lname = updated_data.get('lname', professor.lname)
    professor.abstract = updated_data.get('abstract', professor.abstract)
    professor.field = updated_data.get('field', professor.field)

    # Update keywords
    key_words = request.form.getlist('key_words')
    professor.key_words = key_words

    # Check if a new file is provided for the image update
    if 'file' in request.files:
        filename = upload_file()
        professor.image_path = f"{UPLOAD_FOLDER}/{filename}"  # Adjust based on your folder structure

    # Commit the changes to the database
    try:
        db.session.commit()
        return jsonify({'message': 'Professor updated successfully'}), 200
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Update failed. IntegrityError occurred'}), 400

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)



