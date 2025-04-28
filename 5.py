from enum import Enum
class CuentaBancaria:
    
    class TipoCuenta(Enum):
        AHORROS = "Cuenta de Ahorros"
        CORRIENTE = "Cuenta Corriente"

    def __init__(self, nombres, apellidos, numero_cuenta, tipo_cuenta):
        self.nombres = nombres
        self.apellidos = apellidos
        self.numero_cuenta = numero_cuenta
        self.tipo_cuenta = tipo_cuenta
        self.saldo = 0  # Saldo inicial es cero

    def imprimir_cuenta(self):
        print(f"Titular: {self.nombres} {self.apellidos}")
        print(f"Número de Cuenta: {self.numero_cuenta}")
        print(f"Tipo de Cuenta: {self.tipo_cuenta.value}")  
        print(f"Saldo: ${self.saldo:.2f}")

    def consultar_saldo(self):
        print(f"Saldo actual: ${self.saldo:.2f}")
        return self.saldo

    def consignar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Se ha consignado ${valor:.2f}. Nuevo saldo: ${self.saldo:.2f}")
        else:
            print("El valor a consignar debe ser mayor que cero.")

    def retirar(self, valor):
        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                print(f"Se ha retirado ${valor:.2f}. Nuevo saldo: ${self.saldo:.2f}")
            else:
                print("Fondos insuficientes para realizar el retiro.")
        else:
            print("El valor a retirar debe ser mayor que cero.")



if __name__ == "__main__":
    cuenta = CuentaBancaria("Juan", "Pérez", "123456789", CuentaBancaria.TipoCuenta.AHORROS)
    cuenta.imprimir_cuenta()
    cuenta.consignar(50000)
    cuenta.retirar(20000)
    cuenta.consultar_saldo()

