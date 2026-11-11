from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class PlannedCourse(Base):
    __tablename__ = "planned_courses"

    __table_args__ = (
        UniqueConstraint(
            "planned_semester_id",
            "course_id",
            name="uq_semester_planned_course"
        ),
    )

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    planned_semester_id: Mapped[int] = mapped_column(
        ForeignKey("planned_semesters.id"),
        nullable=False
    )

    course_id: Mapped[int] = mapped_column(
        ForeignKey("courses.id"),
        nullable=False
    )

    planned_semester = relationship(
        "PlannedSemester",
        back_populates="planned_courses"
    )

    course = relationship("Course")

    def __repr__(self):
        return (
            f"<PlannedCourse("
            f"semester_id={self.planned_semester_id}, "
            f"course_id={self.course_id})>"
        )
