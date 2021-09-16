def import_total(request):
    total = 0
    cambio = 0
    if 'cambio' in request.session:
        total = int(request.session["cambio"])
    elif 'carro' in request.session:
        for key, value in request.session["carro"].items():
            total = total+float(value["precio"])
    if 'restar_100' in request.session:
        total = int(request.session["cambio"]) - 100
        request.session["cambio"] = total
        del request.session["restar_100"]
    elif 'restar_50' in request.session:
        total = int(request.session["cambio"]) - 50
        request.session["cambio"] = total
        del request.session["restar_50"]
    elif 'restar_20' in request.session:
        total = int(request.session["cambio"]) - 20
        request.session["cambio"] = total
        del request.session["restar_20"]
    elif 'restar_10' in request.session:
        total = int(request.session["cambio"]) - 10
        request.session["cambio"] = total
        del request.session["restar_10"]
    if total <= 0:
        cambio = abs(total)
        total = 0
        try:
            del request.session["carro"]
            del request.session["cambio"]
        except:
            pass
    return {"import_total": total, "cambio":cambio}

