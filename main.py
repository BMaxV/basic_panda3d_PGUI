from panda3d.core import PGButton
from panda3d.core import PGVirtualFrame
from panda3d.core import NodePath
from panda3d.core import PGEntry
from panda3d.core import PGScrollFrame

from panda3d.core import TextNode

# this cointains all the awkwardly setup hardcoded signals.
from direct.gui.DirectGui import DGG
print(DGG.B1CLICK)

from direct.showbase import DirectObject

from direct.showbase.ShowBase import ShowBase

#draw_mask
# what's that? found in pgItem.cxx

class Wrapper:
    def __init__(self):
        self.b = ShowBase()
        self.event_handler = DirectObject.DirectObject()
            
        b = PGButton("hello") # this is not the text, this is the NAME
        b2 = PGButton("there")
        
        textnode1 = TextNode("name")
        textnode2 = TextNode("name2")
        textnode1.set_text("text test 1")
        textnode2.set_text("text test 2")
        
        textNodePath1 = aspect2d.attachNewNode(textnode1)
        textNodePath2 = aspect2d.attachNewNode(textnode2)
        
        # start of button color experimentation zone      
        
        font = self.b.loader.loadFont("Compyx-Solid.ttf")
        font.setPixelsPerUnit(100)
        
        blue = (0,0,1,1)
        red = (1,0.2,0.2,1)
        white = (1,1,1,1)
        black = (0,0,0,1)
        
        font.set_outline(white,0.5,0.1)
        font.set_fg(blue)
        
        b1_text_node = b.getTextNode()
        b1_text_node.set_font(font)
                
        b2.setup("hunter2",0.5)
        b1_text_node.set_text_color(red)
        b.setup("hello text",0.1) # display text and the bevel width
                        
        # end of button color experimentation zone.
        
        textnode1.set_font(font)
        
        textNodePath1.setScale(0.1)
        textNodePath2.setScale(0.05)
        textNodePath1.setPos((-1,0,-0.8))
        textNodePath2.setPos((-0.2,0,-0.5))
        
        F = PGVirtualFrame("Marco")
        F2 = PGVirtualFrame("Polo")
        
        E = PGEntry("Lima")
        
        SF = PGScrollFrame("Alice")
        
        F.setup(0.2,0.3) # dimensions
        F2.setup(0.5,0.1)
        
        E.setup(10,3) # width and lines
        
        E.setText("this")
        frame_style = E.getFrameStyle(1)
        frame_style.setColor(0,0,0,1)
        
        # state 1 is INACTIVE
        E.setFrameStyle(1,frame_style)
        # state 1 is active
        E.setFrameStyle(0,frame_style)
        
        # big frame, (inner x4), slider width, bevel
        SF.setup(0.5,0.5,-0.4,0.4,-0.8,0.8,0.1,0.05)
            
        button_node_path = self.b.aspect2d.attachNewNode(b)
        button_node_path2 = self.b.aspect2d.attachNewNode(b2)
        
        frame_node_path = self.b.aspect2d.attachNewNode(F)
        frame_node_path2 = self.b.aspect2d.attachNewNode(F2)
        
        entry_path = self.b.aspect2d.attachNewNode(E)
        SF_path = self.b.aspect2d.attachNewNode(SF)
        
        my_id = b.get_id()
        print(my_id)
        
        # this is how to combine the hardcoded signals (see DGG above)
        # with the id of the button
        self.event_handler.accept("within-"+str(my_id),print,["hello there"])
        self.event_handler.accept("without-"+str(my_id),print,["goodbye"])
        self.event_handler.accept("click-mouse1-"+str(my_id),print,["ACTIVATE"])
        
        # which didn't work for the frames for some reason
        my_id = F.get_id()
        
        self.event_handler.accept("within-"+str(my_id),print,["hello there"])
        
        my_id = F2.get_id()
        
        self.event_handler.accept("within-"+str(my_id),print,["hello there"])
        
        
        # this is some positioning but it basically works just
        # as you would expect, so it's not really worth mentioning.
        
        button_node_path.set_scale(0.15)
        button_node_path.set_pos(-0.8,0,0.15)
        
        button_node_path2.set_scale(0.3)
        button_node_path2.set_pos(0,0,0.5)
        
        frame_node_path.set_scale(1)
        frame_node_path.set_pos(-0.3,0,-0.3)
        frame_node_path.set_hpr(0,0,45)
        
        frame_node_path2.set_scale(1)
        frame_node_path2.set_pos(0.3,0,-0.5)
        frame_node_path2.set_hpr(45,45,0)
        
        entry_path.set_scale(0.1)
        entry_path.set_pos(0,0,0.15)
        
        SF_path.set_scale(1)
        SF_path.set_pos(0.8,0,-0.8)

def main():
    W = Wrapper()

    
    while True:
        W.b.taskMgr.step()

if __name__ == "__main__":
    main()
