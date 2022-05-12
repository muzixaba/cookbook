from user_table import User, Session, engine

# create session n bind it to specific db
local_session = Session(bind=engine)

new_user = User(id=1, username="MuziX", email="muzi@email.com")

local_session.add(new_user)
local_session.commit()