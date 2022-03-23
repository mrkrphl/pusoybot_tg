import logging
from gamethings.game import Game
from objects.player import Player
from errors import (AlreadyJoinedError, LobbyClosedError, NoGameInChatError,
                    NotEnoughPlayersError)


class GameManager(object):
    """ Manages all running games by using a confusing amount of dicts """

    def __init__(self):
        self.chatid_games = dict()
        self.userid_players = dict()
        self.userid_current = dict()
        self.logger = logging.getLogger(__name__)

    def new_game(self, chat):
        """
        Create a new game in this chat
        """
        
        self.logger.debug("Creating new game in chat " + str(chat.id))
        game = Game(chat)
        if chat.id not in self.chatid_games:
            self.chatid_games[chat.id] = list()
        
        self.chatid_games[chat.id].append(game)
        return game

    def join_game(self, user, chat):
        """ Create a player from the Telegram user and add it to the game """
        self.logger.info("Joining game with chat id " + str(chat.id))
        try:
            game = self.chatid_games[chat.id][-1]
        except (KeyError, IndexError):
            raise NoGameInChatError()
        if not game.open:
            raise LobbyClosedError()

        if user.id not in self.userid_players:
            self.userid_players[user.id] = list() #empy list user id players

        players = self.userid_players[user.id]

        # Don not re-add a player and remove the player from previous games in
        # this chat, if he is in one of them
        for player in players:
            if player in game.players:
                raise AlreadyJoinedError()
        try: #checks if user can leave a game meaning they joined na sa ibang game
            self.leave_game(user, chat)
        except NoGameInChatError:
            pass #goods join ka dito
        except NotEnoughPlayersError:
            self.end_game(chat, user)

        player = Player(game, user)

        players.append(player) #if userid ay may iba pang games na player siya dito nililist
        self.userid_current[user.id] = player #current game ng userid na player siya

    def leave_game(self, user, chat):
        """ Remove a player from its current game """

        player = self.player_for_user_in_chat(user, chat)
        players = self.userid_players.get(user.id, list())

        #if not a player of current game
        if not player:
            games = self.chatid_games[chat.id]
            for g in games:
                for p in g.players:
                    if p.user.id == user.id:
                        if p is g.current_player:
                            g.turn()

                        p.leave()
                        return

            raise NoGameInChatError

        game = player.game

        if len(game.players) < 3:
            raise NotEnoughPlayersError()

        if player is game.current_player:
            game.turn()

        player.leave()
        players.remove(player)

        # If this is the selected game, switch to another
        if self.userid_current.get(user.id, None) is player:
            if players:
                self.userid_current[user.id] = players[0]
            else:
                del self.userid_current[user.id]
                del self.userid_players[user.id]

    def end_game(self, chat, user):
        """
        End a game
        """

        self.logger.info("Game in chat " + str(chat.id) + " ended")

        # Find the correct game instance to end
        player = self.player_for_user_in_chat(user, chat)

        if not player:
            raise NoGameInChatError

        game = player.game

        # Clear game
        for player_in_game in game.players:
            this_users_players = \
                self.userid_players.get(player_in_game.user.id, list())

            try:
                this_users_players.remove(player_in_game)
            except ValueError:
                pass

            if this_users_players:
                try:
                    self.userid_current[player_in_game.user.id] = this_users_players[0]
                except KeyError:
                    pass
            else:
                try:
                    del self.userid_players[player_in_game.user.id]
                except KeyError:
                    pass

                try:
                    del self.userid_current[player_in_game.user.id]
                except KeyError:
                    pass

        self.chatid_games[chat.id].remove(game)
        if not self.chatid_games[chat.id]:
            del self.chatid_games[chat.id]

    def player_for_user_in_chat(self, user, chat):
        players = self.userid_players.get(user.id, list())
        for player in players:
            if player.game.chat.id == chat.id:
                return player
        return None
