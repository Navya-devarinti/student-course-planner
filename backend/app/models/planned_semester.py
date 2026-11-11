from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class PlannedSemester(Base):
    __tablename__ = "planned_semesters"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    study_plan_id: Mapped[int] = mapped_column(
        ForeignKey("study_plans.id"),
        nullable=False
    )

    semester_name: Mapped[str] = mapped_column(
        String(30),
        nullable=False
    )

    academic_year: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    semester_order: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    total_credits: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False
    )

    study_plan = relationship(
        "StudyPlan",
        back_populates="semesters"
    )

    planned_courses = relationship(
        "PlannedCourse",
        back_populates="planned_semester",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return (
            f"<PlannedSemester("
            f"name='{self.semester_name}', "
            f"year={self.academic_year})>"
        )
