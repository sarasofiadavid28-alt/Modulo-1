import random

try:
    from faker import Faker
except ImportError:
    Faker = None

from service import create_user

ROLES = ["admin", "editor", "usuario"]


def generate_fake_users(n: int = 5) -> list:
    if Faker is None:
        print("[ERROR] La librería 'faker' no está instalada.")
        print("  Ejecuta: pip install faker")
        return []

    fake = Faker("es_MX")
    created = []
    skipped = 0

    print(f"\nGenerando {n} usuario(s) de prueba...")

    for _ in range(n):
        try:
            user_data = {
                "name": fake.name(),
                "email": fake.unique.email(),
                "age": random.randint(18, 65),
                "role": random.choice(ROLES),
            }

            user = create_user(user_data)
            created.append(user)

        except ValueError:
            skipped += 1

    print(f"✓ {len(created)} creado(s), {skipped} omitido(s).")
    return created
