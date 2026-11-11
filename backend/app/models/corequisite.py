
from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Corequisite(Base):
    __tablename__ = "corequisites"

    __table_args__ = (
        UniqueConstraint(
            "course_id",
            "required_course_id",
            name="uq_course_corequisite"
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

    course = relationship(
        "Course",
        foreign_keys=[course_id]
    )

    required_course = relationship(
        "Course",
        foreign_keys=[required_course_id]
    )
