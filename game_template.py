"""
    Game Template for pys60 platform
"""
import e32
import appuifw
import graphics

class GraphicBase:

    def __init__(self, bg_color=(0, 0, 0)):
        """ Constructor
            Args:
                bg_color (tuple): RGB color three byte int
        """
        self.bg_color = bg_color
        #
        self.old_body = appuifw.app.body
        self.canvas = appuifw.Canvas(redraw_callback=self.clear_display)
        self.draw = graphics.Draw(self.canvas)
        appuifw.app.body = self.canvas

    def clear_display(self, rect=()):
        self.draw.clear(self.bg_color)

    def close_canvas(self):
        appuifw.app.body = self.old_body
        self.canvas = None
        self.draw = None


class Graphics(GraphicBase):
    """ All drawing login here """

    def __init__(self):
        pass


class GameCore:
    """ All game logic here """

    def __init__(self):
        pass


class Game():

    INTERVAL = 0.01

    def __init__(self, screen_mode="full"):
        """ Constructor
            Args:
                screen_mode (str): normal, large, full
        """
        appuifw.app.screen = screen_mode
        #
        appuifw.app.menu = [
            (u"Exit", self.set_exit)
        ]
        self.exit_flag = False

    def set_exit(self):
        """ Breaks game loop in self.run function """
        self.exit_flag = True

    def draw_scene(self):
        """ Here all drawing functions """
        self.clear_display()

    def run(self):
        """ Main game loop """
        appuifw.app.exit_key_handler = self.set_exit
        
        while not self.exit_flag:
            self.draw_scene()
            e32.ao_sleep(self.INTERVAL)
        self.close_canvas()


if __name__ == "__main__":
    try:
        app = Game()
    except Exception, e:
        appuifw.note(u"Exception: %s" % (e))
    else:
        app.run()
        del app
