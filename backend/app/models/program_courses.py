
from sqlalchemy import Table, Column, ForeignKey

from app.database import Base


program_courses = Table(
    "program_courses",
    Base.metadata,

    Column(
        "program_id",
        ForeignKey("programs.id", ondelete="CASCADE"),
        primary_key=True
    ),

    Column(
        "course_id",
        ForeignKey("courses.id", ondelete="CASCADE"),
        primary_key=True
    )
)
