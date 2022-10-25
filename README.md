# palpitando
Clone o repositorio
```
git clone https://github.com/lennercp/desen-web-django.git
cd desen-web-django
```
Ative o ambiente virtual
```
venv/Scripts/activate
```
ou
```
venv/Scripts/activate.ps1
```
Caso der erro execute esse comando
```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Instale as dependencias
```
pip install -r requirements.txt
```

Para tornar executavel (cada alteração tem q fazer dnv, eu acho :))
```
pyinstaller --onefile -w main.py
```
