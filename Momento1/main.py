# Instanciamos clase estudiante
class Estudiante:
    ID = 0
    # cuando iniciemos nuevo estudiante
    # vamos a pasarle direcamente los datos
    def __init__(self, notas, nombre, genero, curso):
        self.id = Estudiante.ID # int
        self.nombre = nombre # string
        self.notas = notas # [float]
        self.genero = genero # string
        self.curso = curso # string
        Estudiante.ID += 1
  
    
    def calcular_promedio(self):
        '''
        Utilizando las funciones sum() y len() que nos otorga python
        podemos calcular el promedio facilmente
        sum -> retorna la suma de todos los elementos en una lista
        len -> retorna el numero de elementos en una lista
        '''
        return sum(self.notas) / len(self.notas)

# Clase que se va a encargar de manejar todas las operaciones referente a estudiantes
# tambien contiene la lista de estudiantes (para manejarla)
class Controlador:
    def __init__(self):
        self.lista_estudiantes = []
    
    # llamando este metodo agregamos un nuevo estudiante
    # tambien nos imprime informacion acerca del estudiante agregado
    def agregar_estudiante(self, estudiante):
        self.lista_estudiantes.append(estudiante)
        print(f"Estudiante {estudiante.nombre} añadido al curso {estudiante.curso}")
        print(f"notas {estudiante.notas} : {estudiante.calcular_promedio()}")
    
    # llamando este metodo nos muestra todos los estudiantes agregados
    def mostrar_estudiantes(self):
        for st in self.lista_estudiantes:
            promedio = st.calcular_promedio()
            msg = f"""
            Estudiante {st.nombre} : ID {st.id}
            curso: {st.curso}
            genero: {st.genero}
            notas: {st.notas}
            promedio: {promedio}
            status: {"no aprobado" if int(promedio) < 3 else "aprobado"}
            ------------------------------------------------------------
            """
            print(msg)
    
    '''
    Nos va a mostrar el menu de opciones y dependiendo de la opcion elegida
    se llamara un metodo del controlador distinto
    '''
    def menu(self):
        while 1:
            print(f"1 - Agregar estudiante\n2 - mostrar estudiantes\n3 - salir")
            option = int(input("Elija opcion => "))
            if option == 1:
                print("Nombre del estudiante a agregar")
                nombre = input("> ")
                print("Curso del estudiante a agregar")
                curso = input("> ")
                print("Genero del estudiante a agregar")
                genero = input("> ")
                print("Notas del estudiante (numeros separados por espacios) a agregar")
                notas = list(float(x) for x in input("> ").split(" "))
                nuevo_estudiante = Estudiante(notas, nombre, genero, curso)
                self.agregar_estudiante(nuevo_estudiante)
                continue
            if option == 2:
                self.mostrar_estudiantes()
                continue
            if option == 3:
                print("bye!")
                break
                

# instanciamos nuestra clase controlador
controlador = Controlador()
# abrimos el menu de opciones
controlador.menu()
