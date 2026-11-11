
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.models.associations import university_coordinators


class University(Base):
    __tablename__ = "universities"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    name: Mapped[str] = mapped_column(
        String(200),
        unique=True,
        nullable=False
    )

    location: Mapped[str] = mapped_column(
        String(200),
        nullable=False
    )

    website: Mapped[str | None] = mapped_column(
        String(300),
        nullable=True
    )

    approval_status: Mapped[str] = mapped_column(
        String(30),
        default="pending",
        nullable=False
    )

    submitted_by: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )

    reviewed_by: Mapped[int | None] = mapped_column(
        ForeignKey("users.id"),
        nullable=True
    )

    rejection_reason: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True
    )

    coordinators = relationship(
        "User",
        secondary=university_coordinators,
        back_populates="universities"
    )

    programs = relationship(
        "Program",
        back_populates="university"
    )

    policies = relationship(
        "UniversityPolicy",
        back_populates="university"
    )

    submitter = relationship(
        "User",
        foreign_keys=[submitted_by]
    )

    reviewer = relationship(
        "User",
        foreign_keys=[reviewed_by]
    )

    def __repr__(self):
        return f"<University(name='{self.name}', status='{self.approval_status}')>"

