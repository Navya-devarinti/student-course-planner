from sqlalchemy import String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class InProgressCourse(Base):
    __tablename__ = "in_progress_courses"

    __table_args__ = (
        UniqueConstraint(
            "student_profile_id",
            "course_id",
            name="uq_student_in_progress_course"
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

    semester: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )

    academic_year: Mapped[int] = mapped_column(
        nullable=False
    )

    student_profile = relationship("StudentProfile")

    course = relationship("Course")

    def __repr__(self):
        return (
            f"<InProgressCourse("
            f"student_profile_id={self.student_profile_id}, "
            f"course_id={self.course_id})>"
        )
