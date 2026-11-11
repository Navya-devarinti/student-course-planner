
from sqlalchemy import ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Prerequisite(Base):
    __tablename__ = "prerequisites"

    __table_args__ = (
        UniqueConstraint(
            "course_id",
            "required_course_id",
            name="uq_course_prerequisite"
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

    required_course_id: Mapped[int] = mapped_column(
        ForeignKey("courses.id"),
        nullable=False
    )

    minimum_grade: Mapped[str | None] = mapped_column(
        String(10),
        nullable=True
    )

    course = relationship(
        "Course",
        foreign_keys=[course_id]
    )

    required_course = relationship(
        "Course",
        foreign_keys=[required_course_id]
    )

    def __repr__(self):
        return (
            f"<Prerequisite(course_id={self.course_id}, "
            f"required_course_id={self.required_course_id})>"
        )
