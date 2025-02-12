classDiagram
    Benvinguda --> Login
    Login --> Registre
    Login --> Recuperar_Contrasenya
    Login --> User_Home
    
    User_Home --> Lista_Niños
    User_Home --> Info_User
    
    Lista_Niños --> MenuChild
    Lista_Niños --> Perfil
    
    Registre --> Login
    
    Recuperar_Contrasenya --> Verificacio
    Verificacio --> Login
    
    class Benvinguda {
        +entrarPagina(): void
    }
    
    class Login {
        +registrarNouUsuari(): Registre
        +recuperarContrasenya(): Recuperar_Contrasenya
        +iniciarSessio(): User_Home
    }
    
    class Registre {
        +usuariRegistrat(): Login
    }
    
    class Recuperar_Contrasenya {
        +verificacioUsuari(): Verificacio
    }
    
    class Verificacio {
        +introduirCodi(): Login
    }
    
    class User_Home {
        +veureLlistaNens(): Lista_Niños
        +informacioUsuari(): Info_User
    }
    
    class Lista_Niños {
        +veureMenuNen(): MenuChild
        +anarPerfil(): Perfil
    }
    
    class Info_User {
        +mostrarInfo(): void
    }
    
    class MenuChild {
        +mostrarMenu(): void
    }
    
    class Perfil {
        +mostrarPerfil(): void
    }
