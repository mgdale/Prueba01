class User:
    def __init__(self, user_id, name, email, phone, address):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.phone = phone  # Agregar campo de teléfono
        self.address = address  # Agregar campo de dirección

    def serialize(self):
        return {
            'user_id': self.user_id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'address': self.address
        }
