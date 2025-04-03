class Empleado:
    def __init__(self, nombre, cargo, salario_base, horas_extras=0, pago_por_hora_extra=0):
        """
       
        """
        self.nombre = nombre
        self.cargo = cargo
        self.salario_base = salario_base
        self.horas_extras = horas_extras
        self.pago_por_hora_extra = pago_por_hora_extra

    def calcular_salario(self):
        """
        """
        salario_total = self.salario_base + (self.horas_extras * self.pago_por_hora_extra)
        return salario_total

    def mostrar_informacion(self):
        """
        """
        print(f"Empleado: {self.nombre}")
        print(f"Cargo: {self.cargo}")
        print(f"Salario Base: ${self.salario_base:.2f}")
        print(f"Horas Extras: {self.horas_extras} horas")
        print(f"Pago por Hora Extra: ${self.pago_por_hora_extra:.2f}")
        print(f"Salario Total: ${self.calcular_salario():.2f}")

# Ejemplo de uso:
empleado1 = Empleado(nombre="samy arias", cargo="Desarrollador", salario_base=3000, horas_extras=10, pago_por_hora_extra=20)
empleado1.mostrar_informacion()
