from models import Samples

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import os
import json

class Database(object):
    session = None
    db_user = os.getenv("DB_USER") if os.getenv("DB_USER") != None else "example"
    db_pass = os.getenv("DB_PASS") if os.getenv("DB_PASS") != None else "example"
    db_host = os.getenv("DB_HOST") if os.getenv("DB_HOST") != None else "db"
    db_name = os.getenv("DB_NAME") if os.getenv("DB_NAME") != None else "tp2"
    db_port = os.getenv("DB_PORT") if os.getenv("DB_PORT") != None else "3306"
    Base = declarative_base()


    """get_last: get_last process
    funcion que retorna la ultima muestra realizada
    
        
    """
    def get_last(self):
        session = self.get_session()
        ultima = session.query(Samples).order_by(Samples.id.desc()).first()
        session.close()
        return ultima
    ################################





    """get_last_ten: get_last_ten process
        funcion que retorna las ultimas muestras realizada
    
        
    """
    def get_last_ten(self):
        promedio = Samples()# asigno la tabla de muestras

        #inicializo las variables para acumular
        promedio.temperature = 0
        promedio.humidity = 0
        promedio.pressure = 0
        promedio.windspeed = 0
        

        session = self.get_session() #optengo la sesion
        diez = session.query(Samples).order_by(Samples.id.desc()).limit(10) #obtengo las ultimas 10 muestras
        session.close() #cierro sesion
        
        #acumulando las ultimas 10 temperaturas
        for d in diez:
            promedio.temperature = (promedio.temperature + d.temperature)
            promedio.humidity = (promedio.humidity + d.humidity)
            promedio.pressure = (promedio.pressure + d.pressure)
            promedio.windspeed = (promedio.windspeed + d.windspeed)

        #calculando el promedio para cada campo
        promedio.temperature = (promedio.temperature/10)
        promedio.humidity = (promedio.humidity/10)
        promedio.pressure = (promedio.pressure/10)
        promedio.windspeed = (promedio.windspeed/10)
        return promedio
    ################################

    def get_session(self):
        """Singleton of db connection

        Returns:
            [db connection] -- [Singleton of db connection]
        """
        if self.session == None:
            connection = 'mysql+mysqlconnector://%s:%s@%s:%s/%s' % (self.db_user,self.db_pass,self.db_host,self.db_port,self.db_name)
            engine = create_engine(connection,echo=True)
            connection = engine.connect()
            Session = sessionmaker(bind=engine)
            self.session = Session()
            self.Base.metadata.create_all(engine)
        return self.session
    