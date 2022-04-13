from enum import Enum
from dataclasses import dataclass
from main import db


class Examination(Enum):
    AS_A_LEVEL = 1
    IGCSE = 2


class Period(Enum):
    FM = 1
    MJ = 1


@dataclass
class Subject(db.Model):
    code: str = db.Column(db.String(4), primary_key=True)
    name: str = db.Column(db.String(60), nullable=False)


@dataclass
class PastPaper(db.Model):
    subject_code: str = db.Column(db.Integer, db.ForeignKey('subject.code'), nullable=False)
    subject: Subject = db.relationship("Subject")
    examination: Examination = db.Column(db.Enum(Examination, primary_key=True))
    year: int = db.Column(db.Integer, primary_key=True)
    period: Period = db.Column(db.Enum(Period), primary_key=True)
    paper_number: int = db.Column(db.Integer, primary_key=True)
    paper_type: str = db.Column(db.String(3), primary_key=True)
