from .icontroller import IController
from lighting.lamp import Lamp
from lighting.shutter import Shutter

class LightingController(IController):
    def __init__(self):
        IController.__init__(self,"LichtController")
        self.lamps=[]
        self.shutters=[]

    def addLamp(self, room):
        lamp = Lamp(room)
        self.lamps.append(lamp)

    def addShutter(self, room):
        shutter = Shutter(room)
        self.shutters.append(shutter)

    def lightRoom(self,room):
        if self.status==1:
            if self.getLightRoom(room) <= 80:
                for lamp in self.lamps:
                    if lamp.room == room:
                        lamp.light()
                    else:
                        print("Keine Lampe im Raum: ",room.name," verfügbar")

            if self.getLightRoom(room) >=50:
                for shutter in self.shutters:
                    if shutter.room == room:
                        shutter.open()
                    else:
                        print("Keine Rollläden im Raum: ",room.name," verfügbar")

    def dimRoom(self,room):
        if self.status==1:
            for lamp in self.lamps:
                if lamp.room == room:
                    lamp.dim()
                else:
                    print("Keine Lampe im Raum: ",room.name," verfügbar")

            for shutter in self.shutters:
                if shutter.room == room:
                    shutter.close()
                else:
                    print("Keine Rollläden im Raum: ",room.name," verfügbar")

    def getLightRoom(self,room):
        return room.lsensor.getData()