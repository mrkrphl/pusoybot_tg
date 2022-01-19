def usersetting_entity(db, orm):
    class UserSetting(db.Entity):
        __table__ = "usersetting"
        id = orm.PrimaryKey(int, auto=False, size=64)  # Telegram User ID
        stats = orm.Optional(bool, default=False)  # Opt-in to keep game statistics
        first_places = orm.Optional(int, default=0)  # Nr. of games won in first place
        games_played = orm.Optional(int, default=0)  # Nr. of games completed
        cards_played = orm.Optional(int, default=0)  # Nr. of cards played total
        use_keyboards = orm.Optional(bool, default=False)  # Use keyboards (unused)
    return UserSetting