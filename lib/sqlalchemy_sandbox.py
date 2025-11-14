#!/usr/bin/env python3
# lib/sqlalchemy_sandbox.py
from sqlalchemy import Column, Integer, String, create_engine # type: ignore
from sqlalchemy.ext.declarative import declarative_base # type: ignore

# Define the Base class for declarative mapping
Base = declarative_base()

class Student(Base):
    # 1. __tablename__ attribute is required to name the table
    __tablename__ = 'students'

    # 2. Columns are defined using Column objects as class attributes
    # 3. 'id' is specified as the primary key
    id = Column(Integer(), primary_key=True)
    name = Column(String())

# This block ensures that the table is created only when this file is run as a script.
if __name__ == '__main__':
    # Create the Engine connected to the SQLite file
    engine = create_engine('sqlite:///students.db')
    # Create all defined tables in the database (including 'students')
    Base.metadata.create_all(engine)