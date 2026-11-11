from sqlalchemy import String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class CompletedCourse(Base):
    __tablename__ = "completed_courses"

    __table_args__ = (
        UniqueConstraint(
            "student_profile_id",
            "course_id",
            name="uq_student_completed_course"
        ),
    )

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    student_profile_id: Mapped[int] = mapped_column(
        ForeignKey("student_profiles.id"),
        nullable=False
    )

    course_id: Mapped[int] = mapped_column(
        ForeignKey("courses.id"),
        nullable=False
    )

    grade: Mapped[str | None] = mapped_column(
        String(10),
        nullable=True
    )

    semester: Mapped[str | None] = mapped_column(
        String(20),
        nullable=True
    )

    academic_year: Mapped[int | None] = mapped_column(
        nullable=True
    )

    student_profile = relationship("StudentProfile")

    course = relationship("Course")

    def __repr__(self):
        return (
            f"<CompletedCourse("
            f"student_profile_id={self.student_profile_id}, "
            f"course_id={self.course_id}, "
            f"grade='{self.grade}')>"
        )
