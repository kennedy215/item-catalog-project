from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Country, Fighter



engine = create_engine('sqlite:///tournament.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


country1 = Country(name="China")
session.add(country1)
session.commit()


fighter1 = Fighter(name="Bruce Lee", description="Trained with the legendary IP man speed and incredible power", style="jeet kundo & wing chun", country=country1)

session.add(fighter1)
session.commit()

fighter2 = Fighter(name="Jack Chan", description="Trained with Bruce Lee, all around versatile fighter with multiple styles", style="drunken style, snake, crane, tiger", country=country1)

session.add(fighter2)
session.commit()

fighter3 = Fighter(name="Bolo Yeung", description="Trained with Bruce Lee, known for his strength and brutal style", style="Kung Fu", country=country1)

session.add(fighter3)
session.commit()

country2 = Country(name="Russia")
session.add(country2)
session.commit()

fighter1 = Fighter(name="Yuri Borka", description="MMA combination of many different styles known as a complete fighter", style="MMA, Muay Thai, Brazilian Jitsu", country=country2)

session.add(fighter1)
session.commit()

country3 = Country(name="United States")
session.add(country3)
session.commit()

fighter1 = Fighter(name="Muhammed Ali", description="Boxing, known for speed, grace and power", style="western boxing", country=country2)

session.add(fighter1)
session.commit()

fighter2 = Fighter(name="Andre the Giant", description="Wrestler known for his incredible strength and size", style="Wrestler", country=country2)

session.add(fighter2)
session.commit()

country4 = Country(name="Thailand")

session.add(country4)
session.commit()

fighter1 = Fighter(name="Saenchi", description="Speed, Witts along with tricky power blows with shins", style="Muay Thai", country=country4)

session.add(fighter1)
session.commit()

fighter2 = Fighter(name="Bukaow", description="Strength, direct power and relentless attacks", style="Muay Thai", country=country4)

session.add(fighter2)
session.commit()

print "loaded fighters DB! "


# fighter1 = Fighter(name="Bruce Lee")
# session.add(fighter1)
# session.commit()
#
# background1 = Background(name="The Dragon", description="Trained with the legendary IP man, speed and incredible power", style="jeet kundo & wing chun", "Hong Kong", fighter=fighter1)
#
# session.add(background1)
# session.commit()
#
# print "loaded fighters DB! "
