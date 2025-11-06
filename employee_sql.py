from sqlalchemy.orm  import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String, Float, create_engine
''' Define the Employee model '''
Base = declarative_base()

class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    job_title = Column(String(150), nullable=False)
    salary = Column(Float, nullable=False)

    def __repr__(self):
        return f'[id = {self.id}, name = {self.name}, job_title = {self.job_title}, salary = {self.salary}]'                    

''' Create an SQLite database and the employees table '''
engine = create_engine('sqlite:///employees.db', echo=True)
Base.metadata.create_all(engine)    
Session = sessionmaker(bind=engine)
session = Session()

dravid = Employee(id=1, name='David', job_title='Old Coach', salary=75000)
session.add(dravid)
session.commit()

