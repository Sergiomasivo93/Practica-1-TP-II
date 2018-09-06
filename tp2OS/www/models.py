from sqlalchemy.schema import Column
from sqlalchemy.types import Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Samples(Base):
    __tablename__ = 'samples'
    id=Column(Integer, primary_key=True)
    temperature=Column('temperature', Integer)
    humidity=Column('humidity', Integer)
    pressure=Column('pressure', Integer)
    windspeed=Column('windspeed', Integer)


"""funcion que retorna valores en un iterable

        Returns:
            {dict} -- [Singleton of db connection]
"""
def serilize(self):
    	return{
    		'id' : self.id,
    		'temperatura' : self.temperature,
    		'humedad' : self.humidity,
    		'pressure' : self.pressure,
    		'velocidaddelviento' : self.windspeed
    	}