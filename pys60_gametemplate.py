"""
    Game Template for pys60 platform
"""
import e32
import appuifw
import graphics

class GraphicBase(object):
    """ Base functionality for graphics """

    def __init__(self, bg_color=(0, 0, 0)):
        """ Constructor
            Args:
                bg_color (tuple): RGB color
        """
        self.bg_color = bg_color
        #
        self.old_body = appuifw.app.body
        self.canvas = appuifw.Canvas(redraw_callback=self.clear_display)
        self.screen_size = self.canvas.size
        self.draw = graphics.Draw(self.canvas)
        appuifw.app.body = self.canvas

    def clear_display(self, rect=()):
        self.draw.clear(self.bg_color)

    def close_canvas(self):
        """ Return old body and destroy drawing objects """

        appuifw.app.body = self.old_body
        self.canvas = None
        self.draw = None


class Graphics(GraphicBase):
    """ All drawing logic here """

    def __init__(self):
        GraphicBase.__init__(self)


class GameCore(object):
    """ All game logic here """

    def __init__(self):
        self.graphics = Graphics()

    def draw_scene(self):
        self.graphics.clear_display()

    def quit(self):
        """ Must be called when game ends """

        self.graphics.close_canvas()


class Game(object):
    """ Base game functionality for program """

    INTERVAL = 0.01

    def __init__(self, screen_mode="full"):
        """ Constructor
            Args:
                screen_mode (str): normal, large, full
        """

        appuifw.app.screen = screen_mode
        self.game_core = GameCore()
        # left menu key functions
        appuifw.app.menu = [
            (u"Exit", self.set_exit)
        ]
        self.exit_flag = False

    def set_exit(self):
        """ Breaks game loop in self.run function """

        self.exit_flag = True

    def run(self):
        """ Main game loop """

        appuifw.app.exit_key_handler = self.set_exit
        
        while not self.exit_flag:
            self.game_core.draw_scene()
            e32.ao_sleep(self.INTERVAL)

        self.game_core.quit()


if __name__ == "__main__":
    try:
        app = Game()
    except Exception, e:
        appuifw.note(u"Exception: %s" % (e))
    else:
        app.run()
        del app
