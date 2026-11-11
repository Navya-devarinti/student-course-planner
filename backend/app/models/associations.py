
from sqlalchemy import Table, Column, ForeignKey

from app.database import Base


university_coordinators = Table(
    "university_coordinators",
    Base.metadata,

    Column(
        "university_id",
        ForeignKey("universities.id", ondelete="CASCADE"),
        primary_key=True
    ),

    Column(
        "user_id",
        ForeignKey("users.id", ondelete="CASCADE"),
        primary_key=True
    )
)
