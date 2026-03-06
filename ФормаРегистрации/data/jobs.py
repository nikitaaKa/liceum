import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField, DateTimeField
from wtforms.validators import DataRequired


class Job(SqlAlchemyBase):
    __tablename__ = 'jobs'

    id = sqlalchemy.Column(sqlalchemy.Integer, 
                           primary_key=True, autoincrement=True)
    team_leader = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    job = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    work_size = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    collaborators = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    start_date = sqlalchemy.Column(sqlalchemy.DateTime, 
                                   default=datetime.datetime.now)
    end_date = sqlalchemy.Column(sqlalchemy.DateTime, 
                                 default=datetime.datetime.now)
    is_finished = sqlalchemy.Column(sqlalchemy.Boolean, nullable=True)

class CreateForm(FlaskForm):
    job = StringField('Описание работы', validators=[DataRequired()])
    team_leader = IntegerField('ID руководителя', validators=[DataRequired()])
    work_size = IntegerField('Объем работы (в часах)', validators=[DataRequired()])
    collaborators = StringField('Список соавторов (через запятую)', validators=[DataRequired()])
    is_finished = BooleanField('Работа завершена?')
    submit = SubmitField('Создать работу')
