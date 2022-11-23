class Profile:
    ##atributos##
    # username=''
    # email=''
    # password=''
    ##fin atributos##

    ##metodos##
    def __init__(self,id,username,email,password,status="online",level=0):
        self.id=id
        self.username=username
        self.email=email
        self.password=password
        self.status=status
        self.level=level

    def imprimir(self):
        print("\nEl id es: ",self.id)
        print("El username es: ",self.username)
        print("El email es: ",self.email)
        print("La contraseña es: ",self.password)
        print("Frase de perfil: ",self.status)
        print("Nivel: ",self.level)
