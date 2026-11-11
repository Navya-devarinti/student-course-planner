
from sqlalchemy import (
    String,
    Integer,
    ForeignKey,
    Text
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class RequirementNode(Base):
    __tablename__ = "requirement_nodes"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    program_id: Mapped[int] = mapped_column(
        ForeignKey("programs.id"),
        nullable=False
    )

    parent_id: Mapped[int | None] = mapped_column(
        ForeignKey("requirement_nodes.id"),
        nullable=True
    )

    course_id: Mapped[int | None] = mapped_column(
        ForeignKey("courses.id"),
        nullable=True
    )

    name: Mapped[str] = mapped_column(
        String(200),
        nullable=False
    )

    node_type: Mapped[str] = mapped_column(
        String(30),
        nullable=False
    )

    group_rule: Mapped[str | None] = mapped_column(
        String(20),
        nullable=True
    )

    required_count: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True
    )

    credits_required: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True
    )

    sort_order: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    parent = relationship(
        "RequirementNode",
        remote_side=[id],
        back_populates="children"
    )

    children = relationship(
        "RequirementNode",
        back_populates="parent",
        cascade="all, delete-orphan",
        order_by="RequirementNode.sort_order"
    )

    course = relationship("Course")

    program = relationship("Program")

    def __repr__(self):
        return (
            f"<RequirementNode("
            f"name='{self.name}', "
            f"type='{self.node_type}')>"
        )
