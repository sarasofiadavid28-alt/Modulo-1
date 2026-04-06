"""
service.py — Lógica de negocio (CRUD)
Operaciones sobre la colección de usuarios + persistencia.
"""

import uuid
from file import load_records, save_records
from validate import validate_user


# ── Helpers internos ─────────────────────────────────────────

def _get_all() -> list:
    return load_records()


def _save_all(users: list) -> None:
    save_records(users)


def _find_by_id(users: list, user_id: str) -> dict | None:
    matches = [u for u in users if u["id"] == user_id]
    return matches[0] if matches else None


# ── CRUD ─────────────────────────────────────────────────────

def create_user(user_data: dict) -> dict:
    """Crea un nuevo usuario"""
    user = {
        "id": str(uuid.uuid4())[:8],
        "name": user_data.get("name", ""),
        "email": user_data.get("email", ""),
        "age": int(user_data.get("age", 0)),
        "role": user_data.get("role", "usuario"),
    }

    # Validación
    errors = validate_user(user)
    if errors:
        raise ValueError(errors)

    users = _get_all()

    # Validar email único (set comprehension)
    existing_emails = {u["email"].lower() for u in users}
    if user["email"].lower() in existing_emails:
        raise ValueError("El email ya existe")

    users.append(user)
    _save_all(users)

    return user


def list_users() -> list:
    """Retorna todos los usuarios"""
    return _get_all()


def search_user(user_id: str) -> dict | None:
    """Buscar usuario por ID"""
    users = _get_all()
    return _find_by_id(users, user_id)


def update_user(user_id: str, new_data: dict) -> bool:
    """Actualizar usuario"""
    users = _get_all()
    user = _find_by_id(users, user_id)

    if not user:
        return False

    user.update(new_data)

    errors = validate_user(user)
    if errors:
        raise ValueError(errors)

    _save_all(users)
    return True


def delete_user(user_id: str) -> bool:
    """Eliminar usuario"""
    users = _get_all()
    user = _find_by_id(users, user_id)

    if not user:
        return False

    # Uso de lambda (requisito)
    updated = list(filter(lambda u: u["id"] != user_id, users))

    _save_all(updated)
    return True
