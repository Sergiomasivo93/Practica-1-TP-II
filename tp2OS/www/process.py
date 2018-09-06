from database import Database
from models import Samples

import random
import time


#def main es el metodo donde se generan los datos aleatorios de la estacion meteorologica de la ciudad de buenos aires
#la estacion climatica sobre la cual simulamos es la de invierno
def main (samples, session):
    s = samples
    temp = random.randint(0, 20)        #genero una sola vez valores aleatorios de la temperatura del dia
    humi = random.randint(60, 80)       #genero una sola vez valores de la humedad del dia
    press = random.randint(1017, 1030)  #genero una sola vez valores de la presion del dia
    wspeed = random.randint(15, 30)     #genero una sola vez valores de la velocidad de viento del dia
    while(True):
        s.temperature = random.randint((temp-2), (temp+2))
        s.humidity = random.randint((humi-2), (humi+2))
        s.pressure = random.randint((press-2), (press+2))
        s.windspeed = random.randint((wspeed-5), (wspeed+5))
        session.add(s)
        session.commit()
        time.sleep(1)
    session.close()

################################################################################
if __name__ == '__main__':
    db = Database()
    session = db.get_session()
    samples = Samples()
    main(samples, session)