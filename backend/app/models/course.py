
from sqlalchemy import String, Integer, Text, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.models.program_courses import program_courses


class Course(Base):
    __tablename__ = "courses"

    __table_args__ = (
        UniqueConstraint(
            "university_id",
            "code",
            name="uq_university_course_code"
        ),
    )

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    code: Mapped[str] = mapped_column(
        String(30),
        nullable=False
    )

    name: Mapped[str] = mapped_column(
        String(200),
        nullable=False
    )

    credits: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    university_id: Mapped[int] = mapped_column(
        ForeignKey("universities.id"),
        nullable=False
    )

    programs = relationship(
        "Program",
        secondary=program_courses,
        back_populates="courses"
    )

    def __repr__(self):
        return f"<Course(code='{self.code}', name='{self.name}')>"
