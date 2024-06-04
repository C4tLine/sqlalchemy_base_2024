from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from datetime import date

from toolkit import get_db_url
from models import Base, Category, Equipment


engine = create_engine(get_db_url(), echo=True)

Base.metadata.create_all(engine)

with Session(engine) as session:
    equipment1 = Equipment(
        name ='Вафельница HP',
        description='Удобная, переносная, не очень надёжная, но бюджетная грелка',
        price=1900.0,
        year=date(2015, 12, 24)
    )
    equipment2 = Equipment(
        name='Acer',
        description='type_something_here',
        price=2400.0,
        year=date(2021, 12, 24)
    )
    equipment3 = Equipment(
        name='LG',
        description='Monitor from company LG',
        price=3599.99,
        year=date(2023, 12, 24)
    )
    equipment4 = Equipment(
        name='Xiaomi',
        description='9C NFC',
        price=7999.99,
        year=date(2023, 12, 24)
    )
    equipment5 = Equipment(
        name='Toshiba',
        description='The White Mirror from company Toshiba',
        price=3000.0,
        year=date(2019, 12, 24)
    )

    category1 = Category(
        name='Телефон',
        description='Мобильные устройства',
        equipments=[equipment4]
    )
    category2 = Category(
        name='ПК',
        description='Стационарное ЭВМ',
        equipments=[equipment1]
    )
    category3 = Category(
        name='Монитор',
        description='Мобильное ЭВМ',
        equipments=[equipment2, equipment3, equipment5]
    )

   
    session.add(equipment1)
    session.add(equipment2)
    session.add(equipment3)
    session.add(equipment4)
    session.add(equipment5)
    session.add(category1)
    session.add(category2)
    session.add(category3)

    session.commit()

    # error_equipment = Equipment(
    #     name='A',
    #     description='...',
    #     price=-10000.000,
    #     year=date(2024, 12, 24)
    # )

    # category11 = Category(
    #     name='B',
    #     description='...',
    #     equipments =[error_equipment]
    # # )

    # session.add(error_equipment)
    # session.add(category11)

    # session.commit()