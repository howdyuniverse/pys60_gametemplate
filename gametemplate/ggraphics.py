import appuifw
import graphics

class GraphicsBase(object):
    """ Base functionality for graphics """

    def __init__(self, bg_color=(0, 0, 0)):
        """ Constructor
            Args:
                bg_color (tuple): RGB color
        """
        self.bg_color = bg_color
        #
        self.old_body = appuifw.app.body
        self.canvas = appuifw.Canvas(redraw_callback=self.redraw)
        self.screen_size = self.canvas.size
        self.buf = graphics.Draw(self.canvas)
        appuifw.app.body = self.canvas

    def clear_buf(self):
        self.buf.clear(self.bg_color)

    def redraw(self, rect=()):
        if not self.buf:
            self.canvas.blit(self.buf)

    def close_canvas(self):
        """ Return old body and destroy drawing objects """

        appuifw.app.body = self.old_body
        self.canvas = None
        self.buf = None


class GameGraphics(GraphicsBase):
    """ All drawing logic here """

    def __init__(self):
        GraphicsBase.__init__(self)
