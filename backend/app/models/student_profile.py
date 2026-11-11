from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class StudentProfile(Base):
    __tablename__ = "student_profiles"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        unique=True,
        nullable=False
    )

    university_id: Mapped[int] = mapped_column(
        ForeignKey("universities.id"),
        nullable=False
    )

    program_id: Mapped[int] = mapped_column(
        ForeignKey("programs.id"),
        nullable=False
    )

    enrollment_status: Mapped[str] = mapped_column(
        String(30),
        default="active",
        nullable=False
    )

    user = relationship("User")

    university = relationship("University")

    program = relationship("Program")

    def __repr__(self):
        return (
            f"<StudentProfile("
            f"user_id={self.user_id}, "
            f"program_id={self.program_id})>"
        )
