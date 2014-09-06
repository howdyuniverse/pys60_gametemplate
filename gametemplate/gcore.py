import ggraphics

class GameCore(object):
    """ All game logic here """

    def __init__(self):
        self.graphics = ggraphics.GameGraphics()

    def draw_scene(self):
        self.graphics.clear_buf()
        self.graphics.redraw()

    def tick(self):
        self.draw_scene()

    def cancel(self):
        """ cancel all game flags/core loops """
        pass

    def quit(self):
        """ Must be called when game ends """

        self.graphics.close_canvas()
