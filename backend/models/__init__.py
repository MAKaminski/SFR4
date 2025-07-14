from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class ZipCode(Base):
    __tablename__ = 'zipcodes'
    id = Column(Integer, primary_key=True)
    code = Column(String, unique=True, nullable=False)
    neighborhoods = relationship('Neighborhood', back_populates='zipcode')

class Neighborhood(Base):
    __tablename__ = 'neighborhoods'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    zipcode_id = Column(Integer, ForeignKey('zipcodes.id'))
    zipcode = relationship('ZipCode', back_populates='neighborhoods')
    properties = relationship('Property', back_populates='neighborhood')

class Property(Base):
    __tablename__ = 'properties'
    id = Column(Integer, primary_key=True)
    address = Column(String, nullable=False)
    neighborhood_id = Column(Integer, ForeignKey('neighborhoods.id'))
    neighborhood = relationship('Neighborhood', back_populates='properties')
    price = Column(Float)
    status = Column(String)  # e.g., 'for_sale', 'sold'

class CrimeStat(Base):
    __tablename__ = 'crimestats'
    id = Column(Integer, primary_key=True)
    zipcode_id = Column(Integer, ForeignKey('zipcodes.id'))
    date = Column(Date, nullable=False)
    crime_count = Column(Integer)
    zipcode = relationship('ZipCode') 