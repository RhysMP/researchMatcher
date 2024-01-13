from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import ARRAY


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:Admin123@35.235.95.124:5432/postgres'


db = SQLAlchemy(app)


class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(40))
    lname = db.Column(db.String(40))
    major = db.Column(db.String(40))
    skills = db.Column(ARRAY(db.String(40)))


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
            'skills': student.skills
        }
        student_list.append(student_data)
    return jsonify({'students': student_list}), 200

# Get a specific student by ID

# @app.route('/students/<int:student_id>', methods=['PUT'])
# def update_student(student_id):
#     student = Student.query.get(student_id)
#     if student:
#         data = request.get_json()
#         student.fname = data.get('fname', student.fname)
#         student.lname = data.get('lname', student.lname)
#         student.major = data.get('major', student.major)
#         student.skills = data.get('skills', student.skills)
#         db.session.commit()
#         return jsonify({'message': 'Student updated successfully'}), 200
#     else:
#         return jsonify({'message': 'Student not found'}), 404


@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = Student.query.get(student_id)
    if student:
        student_data = {
            'id': student.id,
            'fname': student.fname,
            'lname': student.lname,
            'major': student.major,
            'skills': student.skills
        }
        return jsonify({'student': student_data}), 200
    else:
        return jsonify({'message': 'Student not found'}), 404


@app.route('/students', methods=['POST'])
def create_student():
    student = Student(
        fname='John',
        lname='Doe',
        major='Computer Science',
        skills=['Python', 'SQL', 'Data Analysis']
    )

    db.session.add(student)
    try:
        # Commit the changes to the database
        db.session.commit()
        return jsonify({'message': 'Student submitted successfully'}), 200
    except Exception as e:
        # Handle any exceptions that may occur during the database operation
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

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


if __name__ == '__main__':
    app.run(debug=True)
