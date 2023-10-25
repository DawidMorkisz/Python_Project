class Box:
    def __init__(self,width,height,depth):
        self.width = width
        self.height = height
        self.depth = depth
        self.contents = []
    
    def add_object(self, obj):
        if self.can_fit(obj):
            self.contents.append(obj)
            
            return True
        else: 
            print("cant add object")
            
    def can_fit(self, obj):
        used_space = sum(o.width * o.height * o.depth for o in self.contents)
        available_space = self.width * self.height * self.depth - used_space
        available_width = self.width - used_space // (self.height * self.depth)
        available_height = self.height - used_space // (self.width * self.depth)
        available_depth = self.depth - used_space // (self.width * self.height)
        return (
            obj.width <= available_width and
            obj.height <= available_height and
            obj.depth <= available_depth 
        )

class Object:
    def __init__(self,name,width,height,depth):
        self.name = name
        self.width = width
        self.height = height
        self.depth = depth

My_Box = Box(10,20,10)
Fieldmouse = Object("Fieldmouse",5,3,3)
Housemouse = Object("Housemouse",7,2,2)
Snail = Object("Snail",3,3,3)
Leaf = Object("Leaf",3,2,1)
Stone = Object("Stone",2,2,1)
test = Object("test",10,18,5)
My_Box.add_object(test)


for obj in My_Box.contents:
    print(obj.name)