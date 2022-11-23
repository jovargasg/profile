from claseprofile import Profile           

def main():
    profile1 = Profile(1,input("Nombre de usuario: "),input("Correo: "),input("Contraseña: "),input("Escoge una frase para tu perfil: "),0)
    profile1.imprimir()
    
    profile2 = Profile(2,input("\nNombre de usuario: "),input("Correo: "),input("Contraseña: "),input("Escoge una frase para tu perfil: "),0)
    
    while profile1.password == profile2.password :
        if profile1.password == profile2.password :
            print("CONTRASEÑA INVALIDA, YA EXISTE")
            profile2 = Profile(2,input("\nNombre de usuario: "),input("Correo: "),input("Contraseña: "),input("Escoge una frase para tu perfil: "))
            profile2.imprimir()

        else:
            profile2.imprimir()
    
main()
