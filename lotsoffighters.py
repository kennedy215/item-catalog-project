from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Gym, Fighter



engine = create_engine('sqlite:///tournament.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


gym1 = Gym(name="UFC")
session.add(gym1)
session.commit()


fighter1 = Fighter(name="Greg", description="Has almost inhuman strength", style="mixed martial arts", country="USA", gym=gym1)

session.add(fighter1)
session.commit()

fighter2 = Fighter(name="Jin", description="Strict form and power", style="karate", country="Japan", gym=gym1)

session.add(fighter2)
session.commit()

fighter3 = Fighter(name="Ru", description="Speed, fluidity and agility", style="Coepeira", country="Brazil", gym=gym1)

session.add(fighter3)
session.commit()

gym2 = Gym(name="Muay Thai Gym")
session.add(gym2)
session.commit()

fighter1 = Fighter(name="Yuri Borka", description="the most complete fighter ", style="MMA, Muay Thai, Brazilian Jitsu", country="Russia", gym=gym2)

session.add(fighter1)
session.commit()

gym3 = Gym(name="Rocky's Boxing Gym")
session.add(gym3)
session.commit()

fighter1 = Fighter(name="Muhammed Ali", description="combination of speed, agility and power", style="western boxing", country="USA", gym=gym3)

session.add(fighter1)
session.commit()

fighter2 = Fighter(name="Sugar Ray", description="speed and deadily combinations", style="Western Boxing", country="USA", gym=gym3)

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
