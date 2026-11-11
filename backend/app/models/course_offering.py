
from sqlalchemy import (
    ForeignKey,
    String,
    Integer,
    Boolean,
    UniqueConstraint
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class CourseOffering(Base):
    __tablename__ = "course_offerings"

    __table_args__ = (
        UniqueConstraint(
            "course_id",
            "term",
            "academic_year",
            name="uq_course_term_year"
        ),
    )

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    course_id: Mapped[int] = mapped_column(
        ForeignKey("courses.id"),
        nullable=False
    )

    term: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )

    academic_year: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    is_available: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False
    )

    course = relationship("Course")

    def __repr__(self):
        return (
            f"<CourseOffering(course_id={self.course_id}, "
            f"term='{self.term}', year={self.academic_year})>"
        )
