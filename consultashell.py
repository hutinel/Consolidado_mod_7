#obtener todos los objetos de laboratorio, directorGeneral, y Producto
from laboratorio.models import Laboratorio, DirectorGeneral, Producto

# Obtener todos los objetos
laboratorios = Laboratorio.objects.all()
directores = DirectorGeneral.objects.all()
productos = Producto.objects.all()

print("Laboratorios:")
for lab in laboratorios:
    print(lab)

print("\nDirectores Generales:")
for dir in directores:
    print(dir)

print("\nProductos:")
for prod in productos:
    print(prod)


#obtener el laboratorio del producto cuyo nombre es 'Producto1'
producto_1 = Producto.objects.get(nombre='Producto 1')
laboratorio_producto_1 = producto_1.laboratorio
print(f"El laboratorio del Producto 1 es: {laboratorio_producto_1}")


#ordenar todos los productos por nombre y mostrar los valores de nombre y laboratorio
productos_ordenados = Producto.objects.all().order_by('nombre')
for prod in productos_ordenados:
    print(f"Producto: {prod.nombre}, Laboratorio: {prod.laboratorio}")


#realizar uina consulta que imprima por pantalla los laboratiorios de todos los productos
productos = Producto.objects.all()
laboratorios_set = set(prod.laboratorio for prod in productos)
print("Laboratorios de todos los productos:")
for lab in laboratorios_set:
    print(lab)
