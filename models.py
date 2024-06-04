from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, CheckConstraint
from uuid import UUID, uuid4
from datetime import date
from typing import List


class UUIDMixin:
    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4())


class Base(DeclarativeBase):
    ...

# К категории принадлежит n кол-во оборудования (n > 1).
class Category(UUIDMixin, Base):
    __tablename__ = "category"

    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str]

    equipments: Mapped[List["Equipment"]] = relationship(back_populates="category")

    __table_args__= (
        CheckConstraint("length(name) < 50", name="category_name_less_then_50"),
        CheckConstraint("length(description) < 500", name="description_less_then_500"),
    )


    def __init__(self, **kwargs):
        if 'id' not in kwargs:
            kwargs['id'] = uuid4()
        super().__init__(**kwargs)


# Оборудование принадлежит к ОДНОЙ категории.
class Equipment(UUIDMixin, Base):
    __tablename__ = "equipment"

    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str]
    price: Mapped[float] = mapped_column(nullable=False)
    year: Mapped[date] = mapped_column(nullable=False)

    category_id: Mapped[UUID] = mapped_column(ForeignKey("category.id"))
    category: Mapped["Category"] = relationship(back_populates="equipments")

    __table_args__ = (
        CheckConstraint("length(name) < 50", name="equipment_name_less_then_50"),
        CheckConstraint("length(description) < 500", name="equipment_description_less_then_500"),
        CheckConstraint("price > 0", name="equipment_price_more_then_zero"),
        CheckConstraint("year < 2024", name="year_less_then_2024"),
    )


    def __init__(self, **kwargs):
        if 'id' not in kwargs:
            kwargs['id'] = uuid4()
        super().__init__(**kwargs)

