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
       
    def list():
        retVal = "First Name: {}\nMiddle Name: {}\nLast Name: {}\nAge: {}\nEye Color: {}\nHair Color: {}\nHeight: {}\nWeight: {}\nFavorite Color: {}\nFart Smell: {}"
        return retVal

p1 = person("Geoff","Stevenson","Cliff","Blue","Yeet"."Blue","Brown","5' 11","179 lbs", "23")

x = person.list

print(x.format((self.first_name,self.middle_name,self.last_name,self.age,self.eyes,self.hair,self.height,self.weight,self.favorite_color,self.fart)))
#print(.format(self.first_name,self.middle_name,self.last_name,self.age,self.eyes,self.hair,self.height,self.weight,self.favorite_color,self.fart)