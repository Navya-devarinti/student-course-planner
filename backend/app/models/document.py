
from datetime import datetime, timezone

from sqlalchemy import String, ForeignKey, DateTime, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class AcademicDocument(Base):
    __tablename__ = "academic_documents"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    filename: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    file_path: Mapped[str] = mapped_column(
        String(500),
        nullable=False
    )

    file_type: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )

    document_type: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    processing_status: Mapped[str] = mapped_column(
        String(30),
        default="uploaded",
        nullable=False
    )

    approval_status: Mapped[str] = mapped_column(
        String(30),
        default="pending",
        nullable=False
    )

    extracted_text: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    uploaded_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False
    )

    university_id: Mapped[int] = mapped_column(
        ForeignKey("universities.id"),
        nullable=False
    )

    program_id: Mapped[int | None] = mapped_column(
        ForeignKey("programs.id"),
        nullable=True
    )

    uploaded_by: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )

    university = relationship("University")

    program = relationship("Program")

    uploader = relationship("User")

    def __repr__(self):
        return f"<AcademicDocument(filename='{self.filename}')>"
