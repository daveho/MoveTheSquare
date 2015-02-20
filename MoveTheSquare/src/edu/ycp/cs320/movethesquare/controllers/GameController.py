import edu.ycp.cs320.movethesquare.model.Game;
import edu.ycp.cs320.movethesquare.model.Square;


class GameController:
	def __init__(self, game, square, mouseX, mouseY):
		game = game
		square = square
		mouseX = mouseX
		mouseY = mouseY
		self.control_game()

	def control_game():
		if mouseX >= 0 and mouseX < game.getWidth() and mouseY >= 0 and mouseY < game.getHeight():
			dx = mouseX - (square.getX() + square.getWidth()/2);
			dy = mouseY - (square.getY() + square.getHeight()/2);
			
			moveX = 0 
			moveY = 0
			if dx > 0:
				moveX = Game.MOVE_DIST;
			else:
				moveX = -Game.MOVE_DIST;
			if dy > 0:
				moveY = Game.MOVE_DIST;
			else:
				moveY = -Game.MOVE_DIST;
			
			game.setSquareDx(moveX);
			game.setSquareDy(moveY);
	
	
	def moveSquare(Game model, Square square): 
		square.setX(square.getX() + model.getSquareDx())
		square.setY(square.getY() + model.getSquareDy())
	


