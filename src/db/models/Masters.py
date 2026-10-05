import uuid
from sqlalchemy import Column, String, DateTime, ForeignKey, VARCHAR, Integer, DECIMAL, JSON
from sqlalchemy.orm import relationship
from src.db.SqlilteDb import Base  

class Site(Base):
    __tablename__ = "site"

    id = Column(String(10), primary_key=True)
    name = Column(String(25), nullable=False)

    employee = relationship("Employee", back_populates="site")

class Positions(Base):
    __tablename__ = "positions"

    id = Column(String(10), primary_key=True)
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
    education = Column(String)
    study = Column(String)

    site_id = Column(String(10), ForeignKey("site.id"))
    site = relationship("Site", back_populates="employee")

    position_id = Column(String(10), ForeignKey("positions.id"))
    positions = relationship("Positions", back_populates="employee")
    
    composition = Column(String(5), nullable=False)
    bpjs_tk_active = Column(Integer, default=1)
    bpjs_kes_active = Column(Integer, default=1)
    tax_active = Column(Integer, default=1)

    default_employee_salary_component = relationship(
        "DefaultEmployeeSalaryComponent", back_populates="employee"
    )
    payroll_header = relationship("PayrollHeader", back_populates="employee")


class SalaryComponents(Base):
    __tablename__ = "salary_components"

    id = Column(VARCHAR(20), primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    type = Column(String(20), nullable=False)
    formula = Column(String)
    description = Column(String)

    default_employee_salary_component = relationship(
        "DefaultEmployeeSalaryComponent", back_populates="salary_component"
    )
    payroll_detail = relationship(
        "PayrollDetails", back_populates="salary_component"
    )
    
class BPJSKesehatanRules(Base):
    __tablename__ = "bpjs_kesehatan_rules"
    
    id = Column(VARCHAR(20), primary_key=True, nullable=False)
    
    batas_max_upah = Column(DECIMAL(15, 2), nullable=False)
    batas_min_upah = Column(DECIMAL(15, 2), nullable=False)
    ditanggung_pemberi_kerja = Column(DECIMAL(5, 4), nullable=False)
    ditanggung_tenaga_kerja = Column(DECIMAL(5, 4), nullable=False)
    
class BPJSTenagaKerjaRules(Base):
    __tablename__ = "bpjs_tenaga_kerja_rules"
    
    id = Column(VARCHAR(20), primary_key=True, nullable=False)
    
    batas_max_upah = Column(DECIMAL(15, 2), nullable=False)
    jaminan_kecelakaan_kerja = Column(DECIMAL(5, 4), nullable=False)
    jaminan_kematian = Column(DECIMAL(5, 4), nullable=False)
    jht_ditanggung_pemberi_kerja = Column(DECIMAL(5, 4), nullable=False)
    jht_ditanggung_tenaga_kerja = Column(DECIMAL(5, 4), nullable=False)
    jp_ditanggung_pemberi_kerja = Column(DECIMAL(5, 4), nullable=False)
    jp_ditanggung_tenaga_kerja = Column(DECIMAL(5, 4), nullable=False)
    
class TaxTarRules(Base):
    __tablename__ = "tax_tar_rules"
    
    id = Column(VARCHAR(20), primary_key=True, nullable=False)
    
    kategori = Column(String(10), nullable=False)
    bruto_min = Column(DECIMAL(15, 2), nullable=False)
    bruto_max = Column(DECIMAL(15, 2), nullable=False)
    tarif = Column(DECIMAL(5, 4), nullable=False)
    composition_accept = Column(JSON, nullable=False)