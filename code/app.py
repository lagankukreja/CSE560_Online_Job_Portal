#from crypt import methods
from distutils.log import debug
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_migrate import Migrate
from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declarative_base
# from models import db, InfoModel

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///EMP.db"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


POSTGRES = {
    'user': 'postgres',
    'pw': 1995,
    'db': 'EMP',
    'host': 'localhost',
    'port': '5432',
}
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)

class EMP(db.Model):

    __tablename__ = "EMP"
    sno = db.Column(db.Integer, primary_key = True )
    name = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(500), nullable=False)
    country = db.Column(db.Integer,nullable = False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    def __init__(self,name,password,country) -> None:
        self.name = name
        self.password = password
        self.country = country
    def __repr__(self) -> str:
        return f"{self.sno} - {self.name}"

# class EMP2(db.Model):
    
#     __tablename__ = "EMP2"
#     sno = db.Column(db.Integer,primary_key=True)
#     cno = db.Column(db.Integer, db.ForeignKey('EMP.country' ,ondelete = 'CASCADE'))
#     countryName = db.Column(db.String(50), nullable=False)
#     date_created = db.Column(db.DateTime, default=datetime.utcnow)
#     def __init__(self,cno,countryName) -> None:
#         self.cno = cno
#         self.countryName = countryName
#     def __repr__(self) -> str:
#         return f"{self.sno} - {self.name}"

class Country(db.Model):
    __tablename__ = "Country"
    country_id = db.Column(db.Integer,primary_key=True)
    country_name = db.Column(db.String(100),nullable = False)

class State(db.Model):
    __tablename__ = "State"
    country_id = db.Column(db.Integer, db.ForeignKey('Country.country_id', onupdate = 'CASCADE', ondelete = 'CASCADE'))   
    state_id = db.Column(db.Integer, primary_key = True)
    state_name = db.Column(db.String(50), nullable = False)

class Skill(db.Model):
    __tablename__ = "Skills"
    skill_id = db.Column(db.Integer, primary_key = True)
    skill_name = db.Column(db.String(50),nullable = False)

class Experience(db.Model):
    __tablename__ = "Experience"
    experience_id = db.Column(db.Integer, primary_key = True)
    experience_name = db.Column(db.String(100), nullable = False)

class Company(db.Model):
    __tablename__ = "Company"
    company_id = db.Column(db.Integer, primary_key = True)
    company_name = db.Column(db.String(100), nullable = False)
    company_email  = db.Column(db.String(100), nullable = False)
    state_id = db.Column(db.Integer, db.ForeignKey(State.state_id,onupdate = 'CASCADE', ondelete = 'CASCADE' ))
    country_id = db.Column(db.Integer, db.ForeignKey(Country.country_id,onupdate = 'CASCADE', ondelete = 'CASCADE' ))

class Salary(db.Model):
    __tablename__ = "Salary"
    salary_id = db.Column(db.Integer, primary_key = True)
    salary_group  =  db.Column(db.String(100), nullable = False)
    # salary_upper = db.Column(db.Integer,nullable = False)
    # salary_lower = db.Column(db.Integer,nullable = False)

# Base = declarative_base()
# USER_ID_SEQ = db.Sequence('user_id_seq')
class Jobs(db.Model):
    __tablename__ = "Jobs"
    # job_id = db.Column(db.Integer,USER_ID_SEQ, primary_key = True,server_default=USER_ID_SEQ.next_value() )
    job_id = db.Column(db.Integer, primary_key = True)
    job_title = db.Column(db.String(50), nullable = False)
    job_desc = db.Column(db.String(50),nullable = False)
    company_id = db.Column(db.Integer, db.ForeignKey(Company.company_id, onupdate = 'CASCADE', ondelete = 'CASCADE' ))
    salary_id = db.Column(db.Integer, db.ForeignKey(Salary.salary_id, onupdate = 'CASCADE', ondelete = 'CASCADE' ))
    job_state = db.Column(db.Integer, db.ForeignKey(State.state_id,onupdate = 'CASCADE', ondelete = 'CASCADE' ))
    job_country = db.Column(db.Integer, db.ForeignKey(Country.country_id,onupdate = 'CASCADE', ondelete = 'CASCADE' ))
    experience_id = db.Column(db.Integer, db.ForeignKey(Experience.experience_id,onupdate = 'CASCADE', ondelete = 'CASCADE' ))


    def __init__(self,job_title,job_desc,company_id,salary_id,job_state,job_country,experience_id) -> None:
        self.job_title = job_title
        self.job_desc = job_desc
        self.company_id = company_id
        self.salary_id = salary_id
        self.job_state = job_state
        self.job_country = job_country
        self.experience_id = experience_id

    
# Applicant Tables
class Gender(db.Model):
    __tablename__ = "Gender"
    gender_id = db.Column(db.Integer, primary_key = True)
    gender_name = db.Column(db.String(100), nullable = False)
class Race(db.Model):
    __tablename__ = "Race"
    race_id = db.Column(db.Integer, primary_key = True)
    race_name = db.Column(db.String(100), nullable = False)
class Education(db.Model):
    __tablename__ = "Education"
    education_id = db.Column(db.Integer, primary_key = True)
    education_name = db.Column(db.String(100), nullable = False)
class Applicant(db.Model):
    __tablename__ = "Applicant"
    # job_id = db.Column(db.Integer,USER_ID_SEQ, primary_key = True,server_default=USER_ID_SEQ.next_value() )
    applicant_id = db.Column(db.Integer, primary_key = True)
    applicant_name = db.Column(db.String(100), nullable = False)
    applicant_email = db.Column(db.String(100), nullable = False)
    education_id = db.Column(db.Integer, db.ForeignKey(Education.education_id, onupdate = 'CASCADE', ondelete = 'CASCADE' ))
    age = db.Column(db.Integer, nullable = False)
    gender_id = db.Column(db.Integer, db.ForeignKey(Gender.gender_id, onupdate = 'CASCADE', ondelete = 'CASCADE' ))
    race_id = db.Column(db.Integer, db.ForeignKey(Race.race_id, onupdate = 'CASCADE', ondelete = 'CASCADE' ))
    skill_id = db.Column(db.Integer, db.ForeignKey(Skill.skill_id, onupdate = 'CASCADE', ondelete = 'CASCADE' ))
    work_authorization = db.Column(db.String(10), nullable = False)        
    state_id = db.Column(db.Integer, db.ForeignKey(State.state_id,onupdate = 'CASCADE', ondelete = 'CASCADE' ))
    country_id = db.Column(db.Integer, db.ForeignKey(Country.country_id,onupdate = 'CASCADE', ondelete = 'CASCADE' ))
    job_state_id = db.Column(db.Integer, db.ForeignKey(State.state_id,onupdate = 'CASCADE', ondelete = 'CASCADE' ))
    job_country_id = db.Column(db.Integer, db.ForeignKey(Country.country_id,onupdate = 'CASCADE', ondelete = 'CASCADE' ))
    expected_salary_id = db.Column(db.Integer, db.ForeignKey(Salary.salary_id,onupdate = 'CASCADE', ondelete = 'CASCADE' ))

    def __init__(self,applicant_name,applicant_email,education_id,age,gender_id,race_id,skill_id,work_authorization,state_id,country_id,job_state_id,job_country_id,expected_salary_id) -> None:
            self.applicant_name=applicant_name
            self.applicant_email = applicant_email
            self.education_id = education_id
            self.age=age
            self.gender_id=gender_id
            self.race_id = race_id
            self.skill_id = skill_id
            self.work_authorization = work_authorization
            self.state_id = state_id
            self.country_id = country_id
            self.job_state_id = job_state_id
            self.job_country_id=job_country_id
            self.expected_salary_id=expected_salary_id



@app.before_first_request
def create_tables():
    db.create_all()

@app.route("/", methods = ['GET','POST'])
def hello_world():
    # return "<p>Hello, World!</p>"
    if request.method=='POST':
        name = request.form['name']
        print(request.form['name'])
        password = request.form['password']
        print(request.form['password'])
        country = request.form['country']
        emp = EMP(name=name, password=password, country = country)
        db.session.add(emp)
        db.session.commit()
    # if request.method=='POST':
    #     cno = request.form['country']
    #     print(request.form['country'])
    #     if request.form['country'] == '1':
    #         countryName = 'India'
    #     else:
    #         countryName = 'USA'
    #     emp2 = EMP2(cno=cno, countryName=countryName)
    #     db.session.add(emp2)
    #     db.session.commit()

    allEMP = EMP.query.all()

    
    return render_template("index.html", allEMP = allEMP)


@app.route("/Job", methods = ['GET','POST'])
def Job():
    if request.method=='POST':
        job_title = request.form['job_title']
        job_desc = request.form['job_desc']
        company_id  = request.form['company_id']
        salary_id = request.form['salary_id']
        job_state = request.form['state_id']
        job_country = request.form['country_id']
        experience_id = request.form['experience_id']
        job = Jobs(job_title=job_title, job_desc=job_desc, company_id = company_id,salary_id=salary_id, job_state=job_state, job_country = job_country, experience_id = experience_id )
        db.session.add(job)
        db.session.commit()
    allJobs = Jobs.query.all()   
    return render_template("Job.html", allJobs = allJobs)










@app.route("/ViewData", methods = ['GET','POST'])
def view():
    allJobs = Jobs.query.all()
    print(allJobs.reverse())
    return render_template("ViewData.html", allJobs = allJobs)


@app.route('/delete/<int:job_id>')
def delete_job(job_id):
    job = Jobs.query.filter_by(job_id=job_id).first()
    db.session.delete(job)
    db.session.commit()
    return redirect("/ViewData")
@app.route('/update/<int:sno>', methods=['GET', 'POST'])
def update(sno):
    if request.method=='POST':
        name = request.form['name']
        password = request.form['password']
        country = request.form['country']
        emp = EMP.query.filter_by(sno=sno).first()
        emp.name = name
        emp.password = password
        emp.country = country
        db.session.add(emp)
        print("update successful")
        db.session.commit()
        return redirect("/ViewData")
        
    emp = EMP.query.filter_by(sno=sno).first()
    return render_template('update.html', emp=emp)

# @app.route("/Applicant", methods = ['GET','POST'])
# def Applicant():
#     if request.method=='POST':
#         name = request.form['name']
#         email = request.form['email']
#         education_id  = request.form['education_id']
#         age = request.form['age']
#         gender_id = request.form['gender_id']
#         race_id = request.form['race_id']
#         work_authorization = request.form['work_authorization']
#         skill_id = request.form['skill_id']
#         state_id = request.form['state_id']
#         country_id = request.form['country_id']
#         salary_id = request.form['salary_id']
#         job = Jobs(name=name, email=email, education_id = education_id,age=age, gender_id=gender_id, race_id = race_id
#         , work_authorization = work_authorization, skill_id=skill_id,state_id=state_id,country_id=country_id,salary_id=salary_id)
#         db.session.add(job)
#         db.session.commit()
#     allJobs = Jobs.query.all()   
#     return render_template("Applicant.html", allJobs = allJobs)

@app.route("/Applicant", methods = ['GET','POST'])
def Applicants():
    if request.method=='POST':
        applicant_name = request.form['applicant_name']
        # email = request.form['email']
        applicant_email = request.form['applicant_email'] 
        education_id = request.form['education_id']
        age  = request.form['age']
        gender_id = request.form['gender_id']
        race_id = request.form['race_id']
        skill_id = request.form['skill_id']
        work_authorization = request.form['work_authorization']
        state_id = request.form['state_id']
        country_id = request.form['country_id']
        job_state_id = request.form['job_state_id']
        job_country_id = request.form['job_country_id']
        expected_salary_id = request.form['expected_salary_id']
        job = Applicant(applicant_name=applicant_name,applicant_email=applicant_email,education_id=education_id,  age = age,gender_id=gender_id, race_id=race_id,skill_id=skill_id,work_authorization = work_authorization, state_id = state_id, country_id=country_id, job_state_id=job_state_id, job_country_id=job_country_id, expected_salary_id=expected_salary_id)
        db.session.add(job)
        db.session.commit()
    allJobs = Applicant.query.all()   
    return render_template("Applicant.html", allJobs = allJobs)

if __name__ == "__main__)":
    app.run(debug= True, port = 8000)


    
