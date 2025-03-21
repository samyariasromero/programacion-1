from abc import ABC, abstractmethod

class MetodoPago(ABC):
    @abstractmethod
    def pagar(self, monto: float) -> str:
        pass

class Nequi(MetodoPago):
    def pagar(self, monto: float) -> str:
        return f"Pago de ${monto:.2f} realizado con Nequi."

class PSE(MetodoPago):
    def pagar(self, monto: float) -> str:
        return f"Pago de ${monto:.2f} realizado con PSE."

class Daviplata(MetodoPago):
    def pagar(self, monto: float) -> str:
        return f"Pago de ${monto:.2f} realizado con Daviplata."

class TarjetaCredito(MetodoPago):
    def pagar(self, monto: float) -> str:
        return f"Pago de ${monto:.2f} realizado con Tarjeta de Crédito."

class TarjetaDebito(MetodoPago):
    def pagar(self, monto: float) -> str:
        return f"Pago de ${monto:.2f} realizado con Tarjeta de Débito."

class Efectivo(MetodoPago):
    def pagar(self, monto: float) -> str:
        return f"Pago de ${monto:.2f} realizado en Efectivo."

def procesar_pago(metodo: MetodoPago, monto: float) -> None:
    print(metodo.pagar(monto))


if __name__ == "__main__":
    nequi = Nequi()
    pse = PSE()
    daviplata = Daviplata()
    tarjeta_credito = TarjetaCredito()
    tarjeta_debito = TarjetaDebito()
    efectivo = Efectivo()
    
    procesar_pago(nequi, 25.0)
    procesar_pago(pse, 73.0)
    procesar_pago(daviplata, 36.0)
    procesar_pago(tarjeta_credito, 69.0)
    procesar_pago(tarjeta_debito, 29.0)
    procesar_pago(efectivo, 88.0)

