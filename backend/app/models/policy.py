
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class UniversityPolicy(Base):
    __tablename__ = "university_policies"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    university_id: Mapped[int] = mapped_column(
        ForeignKey("universities.id"),
        nullable=False
    )

    program_id: Mapped[int | None] = mapped_column(
        ForeignKey("programs.id"),
        nullable=True
    )

    policy_name: Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )

    policy_value: Mapped[str] = mapped_column(
        String(200),
        nullable=False
    )

    description: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True
    )

    university = relationship(
        "University",
        back_populates="policies"
    )

    program = relationship("Program")
