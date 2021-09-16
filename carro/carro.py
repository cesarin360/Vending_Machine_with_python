class Carro:
    def __init__(self, request):
        self.request=request
        self.session=request.session
        carro=self.session.get("carro")
        if not carro:
            carro=self.session["carro"]={}
        self.carro=carro
    def add(self, producto):
        if(str(producto.id) not in self.carro.keys()):
            self.carro[producto.id]={
                "producto_id":producto.id,
                "nombre":producto.nombre,
                "precio":str(producto.precio),
                "cantidad":1,
                "imagen":producto.imagen.url,
                "code":producto.code
            }
        else:
           for key, value in self.carro.items():
               if key==str(producto.id):
                   value["cantidad"]=value["cantidad"]+1   
                   value["precio"]=float(value["precio"])+producto.precio
                   break 
        self.save_car()
    def save_car(self):
        self.session["carro"]=self.carro
        self.session.modified=True
    def delete(self, producto):
        producto.id=str(producto.id)
        if producto.id in self.carro:
            del self.carro[producto.id]
            self.save_car()
    def restar_pr(self, producto):
        for key, value in self.carro.items():
               if key==str(producto.id):
                   value["cantidad"]=value["cantidad"]-1
                   value["precio"]=float(value["precio"])-producto.precio
                   if value["cantidad"]<1:
                       self.delete(producto)
                   break
        self.save_car()
    def clear_car(self):
        self.session["carro"]={}
        try:
            self.session["cambio"]=0
        except:
            pass
        self.session.modified=True
            