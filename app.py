#attendance management system
from flask import Flask,render_template,request,Response,url_for,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///attendance.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

class Attendance(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    student_name=db.Column(db.String(100),nullable=False)
    roll_no=db.Column(db.String(100),nullable=False)
    date=db.Column(db.DateTime, default=datetime.utcnow)
    status=db.Column(db.String(10), nullable=False)
    
@app.route('/')
def index():
    records=Attendance.query.all()
    return render_template('index.html',records=records)
    
@app.route('/add',methods=['POST'])
def add_record():
    student_name=request.form['student_name']
    roll_no=request.form['roll_no']
    status=request.form['status']
    new_record=Attendance(student_name=student_name,roll_no=roll_no,status=status)
    db.session.add(new_record)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete_record(id):
    record=Attendance.query.get(id)
    db.session.delete(record)
    db.session.commit()
    return redirect(url_for('index'))

if __name__=="__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
