from dataclasses import dataclass
from databse import Examination, Period, Subject


@dataclass
class PastPaperDto:
    examination: Examination
    subject: Subject
    year: int
    period: Period
    paper_number: int