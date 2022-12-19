from sqlalchemy import Column, ForeignKey, Integer, String
from db import Base, engine


class Mob(Base):
    __tablename__ = 'mob'
    id = Column(Integer, primary_key=True)
    req_level = Column(Integer)
    attack_type = Column(String)
    attack = Column(Integer)
    xp = Column(Integer)
    armour = Column(Integer)
    magic_armour = Column(Integer)


class Location(Base):
    __tablename__ = 'location'
    id = Column(Integer, primary_key=True)
    x_coord = Column(Integer)
    y_coord = Column(Integer)
    location_type = Column(String)


class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    nickname = Column(String, unique=True)
    level = Column(Integer, default=1)
    hp = Column(Integer, default=100)
    curr_hp = Column(Integer, default=100)
    money = Column(Integer, default=50)
    attack = Column(Integer, default=1)
    magic_attack = Column(Integer, default=1)
    xp = Column(Integer, default=0)
    armour = Column(Integer, default=0)
    magic_armour = Column(Integer, default=0)
    location_id = Column(Integer, ForeignKey(Location.id))


class Item(Base):
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True)
    req_level = Column(Integer)
    hp = Column(Integer)
    cost = Column(Integer)
    cost_to_sale = Column(Integer)
    mana = Column(Integer)
    attack = Column(Integer)
    magic_attack = Column(Integer)
    armour = Column(Integer)
    magic_armour = Column(Integer)
    item_type = Column(String)


class PersonsItem(Base):
    __tablename__ = 'personsitem'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(Person.id), nullable=False)
    item_id = Column(Integer, ForeignKey(Item.id), nullable=False)
    quantity = Column(Integer, default=1)
    condition = Column(Integer, default=100)


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
