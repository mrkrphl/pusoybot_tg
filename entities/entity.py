from pony import orm
from entities import usersetting

db = orm.Database()
db.bind(provider = 'sqlite', filename="pony_tg.db", create_db=True)
usersettings = usersetting.usersetting_entity(db, orm)
db.generate_mapping(create_tables=True)