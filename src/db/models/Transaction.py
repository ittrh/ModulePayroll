import uuid
from datetime import datetime
from sqlalchemy import Column, String, Float, Integer, DECIMAL, DATETIME, ForeignKey, DATE, JSON
from sqlalchemy.orm import relationship
from src.db.SqlilteDb import Base
from src.fun.GenerateBulanTahun import generate_bulan_tahun


class DefaultEmployeeSalaryComponent(Base):
    __tablename__ = "default_employee_salary_component"

    id = Column(
        String(36), primary_key=True, default=lambda: str(uuid.uuid4())
    )

    employee_id = Column(String(36), ForeignKey("employee.id"))
    employee = relationship(
        "Employee", back_populates="default_employee_salary_component"
    )

    component_id = Column(String(20), ForeignKey("salary_components.id"))
    salary_component = relationship(
        "SalaryComponents", back_populates="default_employee_salary_component"
    )

    amount = Column(Float, nullable=False)


class PayrollPeriod(Base):
    __tablename__ = "payroll_period"

    id = Column(
        String(36), primary_key=True, default=lambda: str(uuid.uuid4())
    )

    period_name = Column(
        String(50), default=lambda: str(generate_bulan_tahun())
    )
    start_date = Column(DATE, nullable=False)
    end_date = Column(DATE, nullable=False)
    is_closed = Column(Integer, default=0)

    payroll_header = relationship(
        "PayrollHeader", back_populates="payroll_period"
    )


class PayrollHeader(Base):
    __tablename__ = "payroll_header"

    id = Column(
        String(36), primary_key=True, default=lambda: str(uuid.uuid4())
    )

    period_id = Column(String(36), ForeignKey("payroll_period.id"))
    payroll_period = relationship(
        "PayrollPeriod", back_populates="payroll_header"
    )

    # PERBAIKAN: Rujukan ForeignKey diubah dari "payroll_period.id" ke "employee.id"
    employee_id = Column(String(36), ForeignKey("employee.id"))
    employee = relationship("Employee", back_populates="payroll_header")

    total_income = Column(DECIMAL(15, 2), default=0.00)
    total_deduction = Column(DECIMAL(15, 2), default=0.00)
    thp = Column(DECIMAL(15, 2), default=0.00)
    created_at = Column(DATETIME, default=datetime.now)
    context = Column(JSON)

    payroll_detail = relationship(
        "PayrollDetails", back_populates="payroll_header"
    )


class PayrollDetails(Base):
    __tablename__ = "payroll_details"

    id = Column(
        String(36), primary_key=True, default=lambda: str(uuid.uuid4())
    )

    payroll_header_id = Column(String(36), ForeignKey("payroll_header.id"))
    payroll_header = relationship(
        "PayrollHeader", back_populates="payroll_detail"
    )

    component_id = Column(String(20), ForeignKey("salary_components.id"))
    salary_component = relationship(
        "SalaryComponents", back_populates="payroll_detail"
    )

    amount = Column(DECIMAL(15, 2), nullable=False)
    remarks = Column(String, nullable=True)  # Sebaiknya nullable=True jika opsional