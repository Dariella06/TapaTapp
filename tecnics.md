# Requisits Tècnics

## 1. Backend (Servidor i Gestió de Dades)
El backend és la part essencial del sistema, responsable de manejar les dades, gestionar usuaris i processar la lògica central.

### a. Requisits del Servidor
- **Allotjament**: Hosting Compartit
- **Base de Dades**: MySQL
- **Sistema Operatiu**: Linux
- **APIs i Serveis Web**: RESTful, utilitzant Flask

### b. Llenguatges de Programació
- **Python**

### c. Seguretat
- Autenticació i autorització d'usuaris
- Encriptació de les dades
- Còpies de seguretat automàtiques per evitar pèrdues d'informació

## 2. Frontend
### a. Tipus de Clients
- **Plataforma**: Consola Python, aplicació d'escriptori
- **Llenguatges**: Flutter, Python (per la consola)
- **Compatibilitat de Dispositius**: Flutter permet executar l'aplicació en diversos dispositius (Web, escriptori, mòbil Android i iOS)

## 3. Requisits Generals
### a. Gestió d'Usuari i Autenticació
- **Rols**: Administrador, Tutor, Cuidador
- **Base de Dades**: MySQL
- **Seguretat**: Emmagatzematge de contrasenyes en format Md5 a la base de dades
- **Mètode d'Autenticació**: Login mitjançant usuari o correu electrònic i contrasenya, amb autenticació per Token

### b. Emmagatzematge Local i Sincronització
- **Emmagatzematge Local**: Es guarden dades sensibles com el Token, id d'usuari i nickname.
- **Seguretat**: Utilització de HTTPS i validació a través de Token

### c. Gestió d'Accessibilitat
- Compliment dels nivells A, AA i AAA d'accessibilitat web

## 4. Requisits d'Infraestructura
- **Xarxa**: Connexió a Internet
- **Emmagatzematge al núvol**: 1TB suficient per les necessitats de l'aplicació
- **APIs de Tercers**: No s'utilitzen APIs externes

## 5. Requisits del Procés de Desenvolupament
- **IDE**: Visual Studio Code, Miniconda3 per Python
- **Extensions VSCode**: Python, Python Snippets
- **Control de Versions**: Git, GitHub
- **Metodologia de Desenvolupament**: Utilització d'una metodologia àgil com Scrum per desenvolupar funcionalitats de manera iterativa, validant amb usuaris reals
- **Proves de Qualitat (QA)**: Proves unitàries per garantir la qualitat del codi
