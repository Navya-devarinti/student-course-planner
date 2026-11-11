from datetime import datetime, timezone

from sqlalchemy import String, ForeignKey, DateTime, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class StudyPlan(Base):
    __tablename__ = "study_plans"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    student_profile_id: Mapped[int] = mapped_column(
        ForeignKey("student_profiles.id"),
        nullable=False
    )

    strategy_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    status: Mapped[str] = mapped_column(
        String(30),
        default="draft",
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False
    )

    notes: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    student_profile = relationship("StudentProfile")

    semesters = relationship(
        "PlannedSemester",
        back_populates="study_plan",
        cascade="all, delete-orphan",
        order_by="PlannedSemester.semester_order"
    )

    def __repr__(self):
        return (
            f"<StudyPlan("
            f"id={self.id}, "
            f"strategy='{self.strategy_name}', "
            f"status='{self.status}')>"
        )
