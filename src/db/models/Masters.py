from src.db.SqlilteDb import Base
from sqlalchemy import Column, String, DateTime, ForeignKey, CHAR
from sqlalchemy.orm import relationship
import uuid

class Site(Base):
    __tablename__ = "site"
    
    id = Column(String(10), primary_key=True, index=False)
    name = Column(String(25), nullable=False)
    
    employee = relationship("Employee", back_populates="site")

class Compositions(Base):
    __tablename__ = "compositions"
    
    id = Column(String(10), primary_key=True, index=False)
    code = Column(String(10))
    name = Column(String(25), nullable=False)
    
    employee = relationship("Employee", back_populates="compositions")
    
class Positions(Base):
    __tablename__ = "positions"
    
    id = Column(String(10), primary_key=True, index=False)
    name = Column(String(25), nullable=False)
    
    employee = relationship("Employee", back_populates="positions")

class Employee(Base):
    __tablename__ = "employee"
    
    id = Column(
        String(36), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    nik = Column(String(10), nullable=False)
    name = Column(String(50), nullable=False)
    birthloc = Column(String)
    birthday = Column(DateTime)
    address = Column(String)
    gender = Column(String(6))
    agama = Column(String(15))
    joining = Column(DateTime)
    status = Column(String(5))
    k_bk = Column(CHAR(3))
    education = Column(String)
    study = Column(String)
    
    site_id = Column(String(10), ForeignKey("site.id"))
    site = relationship("Site", back_populates="employee")
    position_id = Column(String(10), ForeignKey("positions.id"))
    positions = relationship("Positions", back_populates="employee")
    composition_id = Column(String(10), ForeignKey("composition.id"))
    compositions = relationship("Compositions", back_populates="employee")