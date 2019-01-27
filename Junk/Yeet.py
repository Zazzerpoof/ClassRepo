class person:
    def __init__(self,first_name,last_name,middle_name,favorite_color,fart,eyes,hair,height,weight,age):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.favorite_color = favorite_color
        self.fart = fart
        self.eyes = eyes
        self.hair = hair
        self.height = height
        self.weight = weight
        self.age = age
       
    def list(self):
        return "First Name: {}\nMiddle Name: {}\nLast Name: {}\nAge: {}\nEye Color: {}\nHair Color: {}\nHeight: {}\nWeight: {}\nFavorite Color: {}\nFart Smell: {}".format(self.first_name,self.middle_name,self.last_name,self.age,self.eyes,self.hair,self.height,self.weight,self.favorite_color,self.fart)
     

p1 = person("Geoff","Stevenson","Cliff","Blue","Yeet","Blue","Brown","5' 11","179 lbs", "23")
p2 = person("Steve","Robertson","Cliff","Green","Really Awful","Purple","Grey","1' 11","307 lbs","26")

x = p1.list()
y = p2.list()

t = input("Who do you want to check?\n")
while t != "p1" and t != "p2":
    t = input("Invalid Dood triy ugen\n")

if t == "p1":
    print(x)
else:
    print(y)
