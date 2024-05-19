
from django.db import models
from cryptography.fernet import Fernet
import base64
from django.conf import settings

# Generar una clave y almacenarla de forma segura
# Puede hacer esto una vez y luego almacenar la clave en settings.SECRET_KEY o en una variable de entorno
# key = Fernet.generate_key()
# print(key)

# Para este ejemplo, usaremos una clave almacenada en settings
key = base64.urlsafe_b64encode(settings.SECRET_KEY.encode('utf-8')[:32])
fernet = Fernet(key)

class MyModel(models.Model):
    encrypted_data = models.TextField()

    def set_data(self, data):
        encrypted_data = fernet.encrypt(data.encode())
        self.encrypted_data = encrypted_data.decode()

    def get_data(self):
        encrypted_data = self.encrypted_data.encode()
        return fernet.decrypt(encrypted_data).decode()
