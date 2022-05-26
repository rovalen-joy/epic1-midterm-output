#Rovalen Joy Calaguing BSCS 1-A
import turtle  

class Draw:

    mandala = turtle.Turtle()              
    window = turtle.Screen()               
    
    incrementSquareShapes = 0
    incrementRoundSquareShapes = 0
    incrementColorIndex = 0 

    def __init__(self):
        self.window.bgcolor('black')        
        self.mandala.speed(0)               
    
    def setMandala(self): 
        self.mandala.hideturtle()           
        self.mandala.penup()                
        self.mandala.goto(-200, -200)       
        self.mandala.showturtle()          
        self.mandala.pendown()              
        self.mandala.goto(0, 100)          

class DrawMandala(Draw):
    
    color = []

    def loopMandala(self, color):

        Draw.__init__(self)
        Draw.setMandala(self)

        while True:
            self.mandala.pencolor(color[self.incrementColorIndex])     
            for i in range(4):                                          
                self.mandala.forward(80)                                
                self.mandala.right(90)                                  
            self.mandala.right(15)                                  
            self.incrementSquareShapes += 1                            
            
            if self.incrementSquareShapes >= 26:                       
                self.mandala.forward(50)                                
                self.incrementSquareShapes = 0                         
                self.incrementRoundSquareShapes += 1                    
                self.incrementColorIndex += 1                           

                if self.incrementColorIndex == 3:                       
                    self.incrementColorIndex = 0                      

                if self.incrementRoundSquareShapes >= 12:               
                    break                                               

    def hideTurtleGraphics(self):
        self.mandala.hideturtle()                                      
        turtle.done()                                                   


color = ['dark orange','deep pink', 'dark orchid']    
obj = DrawMandala()                 
obj.loopMandala(color)              
obj.hideTurtleGraphics()            