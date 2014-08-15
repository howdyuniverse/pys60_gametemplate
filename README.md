Experimental game template for pys60 platform.

class GraphicBase(object) -- basic graphics initialization which pys60 require.

class Graphics(GraphicBase) -- now we can avoid initialization steps in our code and just write drawing logic.

class GameCore(object) -- all logic for game here.

class Game(object) -- main game app class with appuifw menu functions and GameCore calls.