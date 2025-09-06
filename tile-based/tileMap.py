import pygame, simpleGE, random

""" tileMap.py
    demonstrate basic tbw 
    tile images from lpc Atlas - openGameArt
    http://opengameart.org/content/lpc-tile-atlas
    """

class Player(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.walkAnim = simpleGE.SpriteSheet("xeniaWalk.png", (64, 64), 4, 9, .1)

        # in this animation, cell 0 is idle, so start at 1
        self.walkAnim.startCol = 1
        self.animRow = 2
        self.moveSpeed = 5
        self.stepCounter = 0
        
        self.health = 100
        self.attackDMG = 10
        

    

    def process(self):
        self.dx = 0
        self.dy = 0
        walking = False
        
        if self.isKeyPressed(pygame.K_UP):
            self.animRow = 0
            self.dy = -self.moveSpeed
            walking = True
        if self.isKeyPressed(pygame.K_LEFT):
            self.animRow = 1
            self.dx = -self.moveSpeed
            walking = True
        if self.isKeyPressed(pygame.K_DOWN):
            self.animRow = 2 
            self.dy = self.moveSpeed
            walking = True
        if self.isKeyPressed(pygame.K_RIGHT):
            self.animRow = 3 
            self.dx = self.moveSpeed
            walking = True

        if walking:        
            self.copyImage(self.walkAnim.getNext(self.animRow))
            self.stepCounter += 1
            print(self.stepCounter)
        else:
            self.copyImage(self.walkAnim.getCellImage(4, self.animRow))

        # --- clamp to screen edges ---
        scr_w = self.scene.screen.get_width()
        scr_h = self.scene.screen.get_height()

        if self.rect.left < 0:
            self.rect.left = 0
            self.x = self.rect.centerx
        if self.rect.right > scr_w:
            self.rect.right = scr_w
            self.x = self.rect.centerx
        if self.rect.top < 0:
            self.rect.top = 0
            self.y = self.rect.centery
        if self.rect.bottom > scr_h:
            self.rect.bottom = scr_h
            self.y = self.rect.centery
            
class BattlePlayer(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.player = Player(self)
        self.idleAnim = simpleGE.SpriteSheet("xeniaWalk.png", (64, 64), 4, 9, .1)
        self.animRow = 1
        self.copyImage(self.idleAnim.getCellImage(0, self.animRow))
        self.position = (410,210)
        
        self.health = self.player.health
        self.attackDMG = self.player.attackDMG
        
class BattleEnemy(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.idleAnim = simpleGE.SpriteSheet("characterWalk.png", (64, 64), 4, 9, .1)
        self.animRow = 3
        self.copyImage(self.idleAnim.getCellImage(0, self.animRow))
        self.position = (210, 210)
        
        self.health = 30
        self.attackDMG = 50
        
    def battleKnowledge() 
            
            
class StepCounterLbl(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Step Counter: "
        self.center = (500, 20)
        self.size = (200, 30)
        self.clearBack = True
        self.fgColor = "white"
        self.bgColor = "black"
    

class Tile(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.images = [
            pygame.image.load("grass.png"),
            pygame.image.load("dirt.png"),
            pygame.image.load("water.png")]
        
        self.setSize(32, 32)
        self.GRASS = 0
        self.DIRT = 1
        self.WATER = 2
        self.state = self.GRASS

    def setState(self, state):
        self.state = state
        self.copyImage(self.images[state])
      
            
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setCaption("Click on a tile to edit")
        self.tileset = []
        self.player = Player(self)
        saveState = False
        
        self.stepCounter = StepCounterLbl()
        
        
        self.ROWS = 15
        self.COLS = 20
        
        self.loadMap()
        
        self.sprites = [self.tileset,
                        self.player,
                        self.stepCounter]
        
    def loadMap(self):
        
      map = [
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  
          [1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0],  
          [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],  
          [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],  
          [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],  
          [0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0],  
          [2,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,2],  
          [2,2,2,2,2,2,0,0,0,0,1,0,0,0,0,0,2,2,2,2],  
          [0,2,2,2,2,2,2,0,0,0,1,0,0,0,2,2,2,2,2,0],  
          [0,0,0,0,0,0,2,2,2,2,1,2,2,2,2,2,0,0,0,0],  
          [0,0,0,0,0,0,0,2,2,2,1,2,2,2,0,0,0,0,0,0],  
          [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],  
          [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1],  
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]  
      ]
    
      for row in range(self.ROWS):
          self.tileset.append([])
          for col in range(self.COLS):
            currentVal = map[row][col]
            newTile = Tile(self)
            newTile.setState(currentVal)
            xPos = 16 + (32 * col)
            yPos = 16 + (32 * row)
            newTile.x = xPos
            newTile.y = yPos
            self.tileset[row].append(newTile)
            
    
    def process(self):
        self.stepCounter.text = f"Step Counter: {self.player.stepCounter}"
        if self.player.stepCounter >= 50:
            self.player.stepCounter = 0
            if random.randint(1, 2) == 1:
                print("Random Encounter!")
                position = self.player.position
                saveState = True
                self.stop()
                battle = Battle()
                battle.start()
                
        if self.isKeyPressed(pygame.K_b):
            position = self.player.position
            print(position)
            self.stop()
            battle = Battle()
            battle.start()
            
    
    

                
                
class Battle(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("Tavern800x600.png")
        self.btnAttack = AttackBtn()
        self.btnBlock = BlockBtn()
        self.player = BattlePlayer(self)
        self.player.setSize(100,100)
        
        self.enemy = BattleEnemy(self)
        self.enemy.setSize(100,100)
        
        
        
        self.sprites = [self.btnAttack, self.btnBlock, self.player, self.enemy]
        
    def process(self):
        if self.btnAttack.clicked:
            self.enemy.health = self.enemy.health - self.player.attackDMG
            print(f"Enemy is at {self.enemy.health}")
            
        if self.enemy.health <= self.enem:
            print("Enemy Defeat!")
            self.stop
            game = Game()
            game.start()
            
        
        
class AttackBtn(simpleGE.Button):
    def __init__(self):
        super().__init__()
        self.center = ((210,410))
        self.text = "Attack"
        
class BlockBtn(simpleGE.Button):
    def __init__(self):
        super().__init__()
        self.center = ((410, 410))
        self.text = "Block"
    
            
                
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()