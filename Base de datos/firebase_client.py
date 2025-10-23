import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate(r"C:\Users\Estudiante\Documents\POO\App gestion inventario\configuracion\ServiceAccountService.json")
firebase_admin.initialize_app(cred)


