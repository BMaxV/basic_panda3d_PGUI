from panda3d.core import PGButton
from panda3d.core import PGVirtualFrame
from panda3d.core import NodePath

from direct.showbase.ShowBase import ShowBase

class Wrapper:
    def __init__(self):
        self.b = ShowBase()

def main():
    W = Wrapper()
    b = PGButton("hello") # this is not the text, this is the NAME
    b2 = PGButton("there")
    F = PGVirtualFrame("Marco")
    F2 = PGVirtualFrame("Polo")
    
    b.setup("hello text",0.1) #this sets up the text on the button and the bevel width
    b2.setup("hunter2",0.5) 
    F.setup(0.2,0.3)
    F2.setup(0.5,0.1)
        
    button_node_path = W.b.aspect2d.attachNewNode(b)
    button_node_path2 = W.b.aspect2d.attachNewNode(b2)
    frame_node_path = W.b.aspect2d.attachNewNode(F)
    frame_node_path2 = W.b.aspect2d.attachNewNode(F2)
    
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
    
    while True:
        W.b.taskMgr.step()

if __name__ == "__main__":
    main()
