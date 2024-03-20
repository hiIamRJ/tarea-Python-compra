from customer import Customer
from item import Item
from seller import Seller

vendedor = Seller("Tienda DIC")
for i in range(10):
    Item("CPU", 40830, vendedor)
    Item("Memoria", 13880, vendedor)
    Item("Placa Base", 28980, vendedor)
    Item("Unidad de Alimentación", 8980, vendedor)
    Item("Caja de PC", 8727, vendedor)
    Item("HDD de 3.5 pulgadas", 10980, vendedor)
    Item("SSD de 2.5 pulgadas", 13370, vendedor)
    Item("SSD M.2", 12980, vendedor)
    Item("Refrigeración de CPU", 13400, vendedor)
    Item("Tarjeta Gráfica", 23800, vendedor)

print("🤖 Por favor, dime tu nombre")
cliente = Customer(input())

print("🏧 Por favor, introduce la cantidad a cargar en tu billetera")
cliente.wallet.deposit(int(input()))

print("🛍️ Comenzando las compras")
fin_compras = False
while not fin_compras:
    print("📜 Lista de productos")
    vendedor.show_items()

    print("️️⛏ Por favor, introduce el número del producto")
    numero = int(input())

    print("⛏ Por favor, introduce la cantidad de productos")
    cantidad = int(input())

    productos = vendedor.pick_items(numero, cantidad)
    for producto in productos:
        cliente.cart.add(producto)
    print("🛒 Contenido del carrito")
    cliente.cart.show_items()
    print(f"🤑 Total: {cliente.cart.total_amount()}")

    print("😭 ¿Deseas finalizar las compras? (s/n)")
    fin_compras = input() == "s"

print("💸 ¿Deseas confirmar la compra? (s/n)")
if input() == "s":
    cliente.cart.check_out()

print("୨୧┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈ Resultados ┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈୨୧")
print(f"️🛍️ ️{cliente.name}'s possessions")
cliente.show_items()
print(f"😱👛 Saldo en la billetera de {cliente.name}: {cliente.wallet.balance}")

print(f"📦 Inventario de {vendedor.name}")
vendedor.show_items()
print(f"😻👛 Saldo en la billetera de {vendedor.name}: {vendedor.wallet.balance}")

print("🛒 Contenido del carrito")
cliente.cart.show_items()
print(f"🌚 Total: {cliente.cart.total_amount()}")

print("🎉 Fin")
