from vehiculo_app.models import *

def crear_vehiculo(patente,marca,modelo,year):
    auto = Vehiculo(patente=patente,marca=marca,modelo=modelo,year=year)
    auto.save()
    return auto

def crear_chofer(rut, nombre, apellido, activo, creacion_reg):
    chofer = Chofer(rut=rut, nombre=nombre,apellido=apellido,activo=activo,creacion_reg=creacion_reg,)
    chofer.save()
    return chofer

def crear_registro_contable(fecha_compra,valor,vehiculo):
    registro = RegistroContabilidad(fecha_compra=fecha_compra,valor=valor,vehiculo=vehiculo)
    registro.save()
    return registro

def deshabilitar_chofer(pk_id):
    try:
        chofer = Chofer.objects.get(id=pk_id)
        chofer.activo = False
        chofer.save()
        return False
    except:
        print("error en deshabilitar chofer")

def habilitar_chofer(pk_id):
    try:
        chofer = Chofer.objects.get(id=pk_id)
        chofer.activo = True
        chofer.save()
        return True
    except:
        print("error en habilitar chofer")

def deshabilitar_vehiculo(pk_id):
    try:
        auto = Vehiculo.objects.get(id=pk_id)
        auto.activo= False
        auto.save()
        return False
    except:
        print("error en deshabilitar vehiculo")

def habilitar_vehiculo(pk_id):
    try:
        auto = Vehiculo.objects.get(id=pk_id)
        auto.activo= True
        auto.save()
        return True
    except:
        print("error en habilitar vehiculo")

def obtener_vehiculo(pk_id):
    try:
        auto = Vehiculo.objects.get(id=pk_id)
        return auto
    except:
        print("error en obtener vehiculo")

def obtener_chofer(pk_id):
    try:
        chofer = Chofer.objects.get(id=pk_id)
        return chofer
    except:
        print("error en obtener chofer")

def asignar_chofer_a_vehiculo(pk_id_chofer, pk_id_vehiculo):
    try:
        chofer = Chofer.objects.get(id=pk_id_chofer)
        auto = Vehiculo.objects.get(id=pk_id_vehiculo)
        auto.chofer = chofer
        auto.save()
        return True
    except:
        print("error en asignar chofer a vehiculo")

def imprimir_datos_vehiculos():
    autos = Vehiculo.objects.all()
    for auto in autos:
        print("id: ", auto.id)
        print(f"Patente: {auto.patente}, Marca: {auto.marca}, Modelo: {auto.modelo}, Año: {auto.year}")

