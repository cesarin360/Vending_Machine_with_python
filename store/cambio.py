class Cambio:
    def __init__(self, request):
        self.request=request
        self.session=request.session
        cambio=self.session.get("cambio")
        self.cambio = cambio
    def restar_100(self):
        if not self.cambio:
            total = 0
            for key, value in self.request.session["carro"].items():
                total = total+float(value["precio"])
            self.cambio=self.session["cambio"]=total
            self.session.modified=True
        self.session["restar_100"]=self.cambio
        self.session.modified=True
    def restar_50(self):
        if not self.cambio:
            total = 0
            for key, value in self.request.session["carro"].items():
                total = total+float(value["precio"])
            self.cambio=self.session["cambio"]=total
            self.session.modified=True
        self.session["restar_50"]=self.cambio
        self.session.modified=True
    def restar_20(self):
        if not self.cambio:
            total = 0
            for key, value in self.request.session["carro"].items():
                total = total+float(value["precio"])
            self.cambio=self.session["cambio"]=total
            self.session.modified=True
        self.session["restar_20"]=self.cambio
        self.session.modified=True
    def restar_10(self):
        if not self.cambio:
            total = 0
            for key, value in self.request.session["carro"].items():
                total = total+float(value["precio"])
            self.cambio=self.session["cambio"]=total
            self.session.modified=True
        self.session["restar_10"]=self.cambio
        self.session.modified=True
        