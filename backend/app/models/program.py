
from sqlalchemy import ForeignKey, String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.models.program_courses import program_courses


class Program(Base):
    __tablename__ = "programs"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    name: Mapped[str] = mapped_column(
        String(200),
        nullable=False
    )

    degree_type: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    total_credits: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    university_id: Mapped[int] = mapped_column(
        ForeignKey("universities.id"),
        nullable=False
    )

    university = relationship(
        "University",
        back_populates="programs"
    )

    courses = relationship(
        "Course",
        secondary=program_courses,
        back_populates="programs"
    )

    def __repr__(self):
        return f"<Program(name='{self.name}')>"




