class Fleet:
      def __init__(self, bots):
        self.bots = []
        for bot in bots:
            self.bots.append(bot)

      def remove_dead(self):
        for bot in self.bots:
          if bot.get_health() < 1:
            self.bots.remove(bot)
