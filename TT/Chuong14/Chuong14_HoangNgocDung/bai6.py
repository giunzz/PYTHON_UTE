class Converter:
    def __init__(self,length,unit):
        self.length=length
        self.unit=unit
    def feet(self):
        if(self.unit=='feet'):
            return self.length
        elif(self.unit=='inches'):
            return self.length/12
        elif(self.unit=='yards'):
            return self.length/0.333
        elif(self.unit=='miles'):
            return self.length/0.000189
        elif(self.unit=='millimeters'):
            return self.length/304.8
        elif(self.unit=='centimeters'):
            return self.length/30.48
        elif(self.unit=='meters'):
            return self.length/0.305
        elif(self.unit=='kilometers'):
            return self.length/0.000305
    def inches(self):
        if(self.unit=='feet'):
            return self.length*12
        elif(self.unit=='inches'):
            return self.length
        elif(self.unit=='yards'):
            return self.length*36
        elif(self.unit=='miles'):
            return self.length*63360
        elif(self.unit=='millimeters'):
            return self.length*0.0393701
        elif(self.unit=='centimeters'):
            return self.length*0.393701
        elif(self.unit=='meters'):
            return self.length*39.3701
        elif(self.unit=='kilometers'):
            return self.length*39370.1
    def yards(self):
        if(self.unit=='feet'):
            return self.length*0.333333
        elif(self.unit=='inches'):
            return self.length*0.0277778
        elif(self.unit=='yards'):
            return self.length
        elif(self.unit=='miles'):
            return self.length*1760
        elif(self.unit=='millimeters'):
            return self.length*0.00109361
        elif(self.unit=='centimeters'):
            return self.length*0.0109361
        elif(self.unit=='meters'):
            return self.length*1.09361
        elif(self.unit=='kilometers'):
            return self.length*1093.61
    
    def miles(self):
        if(self.unit=='feet'):
            return self.length*0.000189394
        elif(self.unit=='inches'):
            return self.length*63360
        elif(self.unit=='yards'):
            return self.length*0.027777728
        elif(self.unit=='miles'):
            return self.length
        elif(self.unit=='millimeters'):
            return self.length/1609344
        elif(self.unit=='centimeters'):
            return self.length/160934.4
        elif(self.unit=='meters'):
            return self.length/1609.344
        elif(self.unit=='kilometers'):
            return self.length/1.609
    def kilometers(self):
        if(self.unit=='feet'):
            return self.length/3280.84
        elif(self.unit=='inches'):
            return self.length/39370.1
        elif(self.unit=='yards'):
            return self.length/1093.61
        elif(self.unit=='miles'):
            return self.length/0.621371
        elif(self.unit=='millimeters'):
            return self.length/1000000
        elif(self.unit=='centimeters'):
            return self.length/100000
        elif(self.unit=='meters'):
            return self.length/1000
        elif(self.unit=='kilometers'):
            return self.length
    def meters(self):
        if(self.unit=='feet'):
            return self.length/3.28084
        elif(self.unit=='inches'):
            return self.length/39.3701
        elif(self.unit=='yards'):
            return self.length/1.09361
        elif(self.unit=='miles'):
            return self.length/0.000621371
        elif(self.unit=='millimeters'):
            return self.length/1000
        elif(self.unit=='centimeters'):
            return self.length/100
        elif(self.unit=='meters'):
            return self.length
        elif(self.unit=='kilometers'):
            return self.length/0.001
    def centimeters(self):
        if(self.unit=='feet'):
            return self.length/0.0328084
        elif(self.unit=='inches'):
            return self.length/0.393701
        elif(self.unit=='yards'):
            return self.length/0.0109361
        elif(self.unit=='miles'):
            return self.length*160934
        elif(self.unit=='millimeters'):
            return self.length/10
        elif(self.unit=='centimeters'):
            return self.length
        elif(self.unit=='meters'):
            return self.length*100
        elif(self.unit=='kilometers'):
            return self.length*100000
    def millimeters(self):
        if(self.unit=='feet'):
            return self.length*304.8
        elif(self.unit=='inches'):
            return self.length/0.0393701
        elif(self.unit=='yards'):
            return self.length/0.00109361
        elif(self.unit=='miles'):
            return self.length*1609340
        elif(self.unit=='millimeters'):
            return self.length
        elif(self.unit=='centimeters'):
            return self.length*10
        elif(self.unit=='meters'):
            return self.length*100
        elif(self.unit=='kilometers'):
            return self.length*1000000
    
len=int(input("Enter length: "))
type=input("Enter unit type: inches,feet,yards,miles,millimeters,centimeters,meters,kilometers---> ")
c=Converter(len,type)
print("Length in Feet: ",round(c.feet(),3))
print("Length in Inches: ",round(c.inches(),3))
print("Length in Yards: ",round(c.yards(),3))
print("Length in Miles: ",round(c.miles(),3))
print("Length in Kilometers: ",round(c.kilometers(),3))
print("Length in Meters: ",round(c.meters(),3))
print("Length in Centimeters: ",round(c.centimeters(),3))
print("Length in Millimeters: ",round(c.millimeters(),3))