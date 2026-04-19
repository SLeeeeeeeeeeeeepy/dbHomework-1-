from database import engine, Base
import models.user
import models.profile
import models.course
import models.lesson
import models.association

Base.metadata.create_all(bind=engine)

print("Tables created successfully")