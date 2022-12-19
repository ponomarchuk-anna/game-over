from db import db_session
from models import Location

locations = [
    (0, 0, 'Town'), (10, 0, 'Forest'), (20, 0, 'Castle'),
    (0, 10, 'Lake'), (10, 10, 'Field'), (20, 10, 'Tavern'),
    (0, 20, 'Dungeon'), (10, 20, 'Cave'), (20, 20, 'Mountain'),
]

locations2 = []
for l in locations:
    location = {'x_coord': l[0], 'y_coord': l[1], 'location_type': l[2]}
    locations2.append(location)
db_session.bulk_insert_mappings(Location, locations2)
db_session.commit()
