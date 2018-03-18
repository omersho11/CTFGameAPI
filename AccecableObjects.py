

class _Actions(object):
    dict = {}
    
    def _addAction(self,obj,action,l):
        if not obj in self.dict.keys():
            self.dict[obj] = []
        self.dict[obj].append( (action, l) ) #Inserting Tuples

    def _get_dict(self):
        return self.dict

class Location(object):
    def __init__(self,_x,_y):
        self.x = int(_x)
        self.y = int(_y)
        
    def get_location(self): return self

    def get_x(self): return self.x

    def get_y(self): return self.y

    def __str__(self):
        return '('+str(self.x)+','+str(self.y)+')'

    def __repr__(self):
        return self.__str__()

    def __add__(self,loc):
        return Location(self.x+ loc.x,self.y +loc.y)

    def __sub__(self,loc):
        return Location(self.x - loc.x,self.y - loc.y)

    def __mul__(self,scalar):
        scalar = float(scalar);return Location(self.x * scalar,self.y * scalar)

    def __div__(self,scalar):
        scalar = float(scalar);return self*(1/scalar)

    def distance(self,loc):
        return (float(((self.x-loc.x)**2)+((self.y-loc.y)**2)) )**0.5

    def towards(self,loc,dist):
        t = float(dist)/ self.distance(loc)
        return self+((self*-1) + loc)*t



class _Game(object):
    pass
    

class _GameObject(_Actions):
    def __init__(self,objstr,location,obj_id,team):
        self.objstr = objstr
        self.location = location
        self.id = obj_id
        self.team = team

    def get_location(self): return self.location

    def __set__(self, instance, value): raise AttributeError

    def __str__(self):
        return '('+str(self.objstr)+' >> ID: '+str(self.id)+' OWNER: '+str(self.team)+' LOCATION: '+str(self.location)+')'
    
class Pirate(_GameObject):
    def __init__(self,location,push_distance,push_range,team,cooldown,max_speed,pirate_id):
        _GameObject.__init__(self,'Pirate',location,pirate_id,team)
        self.speed = max_speed
        self.push_distance,self.push_range = push_distance,push_range
        self.push_cooldown = cooldown
        

    def move(self,gameobj):
        if gameobj.get_location().distance(self.location) > self.speed:
            self.addAction(self,'move', [self.location.towards(gameobj.get_location(),self.speed)])
        else:
            self.addAction(self,'move',[gameobj.get_location()])
            
class Flag(_GameObject):
    def __init__(self,location,id):
        _GameObject.__init__(self,'Flag',location,id,-1)
    

class HomeBase(_GameObject):
    def __init__(self,location,unload_range,team,id):
        _GameObject.__init__(self,'HomeBase',location,id,team)
        self.unload_range = unload_range


#Testing vars        
a = Location(500,0)
b = Location(600,0)
            
push_dist = 600
push_r = 300
cd = 2
max_s = 300
p = [Pirate(a,push_dist,push_r,0,cd,max_s,0),Pirate(b,push_dist,push_r,1,cd,max_s,0)]
