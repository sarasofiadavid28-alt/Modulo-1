"""
test_service.py — Pruebas unitarias del sistema
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import pytest
from unittest.mock import patch

# ── Test 1: Validación de usuario correcto ────────────────────
def test_validate_user_valid():
    from validate import validate_user
    user = {
        "name": "Sara Sofia",
        "email": "sara@gmail.com",
        "age": 20,
        "role": "admin"
    }
    errors = validate_user(user)
    assert errors == []

# ── Test 2: Validación falla con email inválido ───────────────
def test_validate_user_invalid_email():
    from validate import validate_user
    user = {
        "name": "Sara Sofia",
        "email": "correo-invalido",
        "age": 20,
        "role": "admin"
    }
    errors = validate_user(user)
    assert len(errors) > 0

# ── Test 3: Validación falla con edad inválida ────────────────
def test_validate_user_invalid_age():
    from validate import validate_user
    user = {
        "name": "Sara Sofia",
        "email": "sara@gmail.com",
        "age": -5,
        "role": "admin"
    }
    errors = validate_user(user)
    assert len(errors) > 0

# ── Test 4: Crear usuario guarda correctamente ────────────────
def test_create_user():
    from service import create_user
    with patch("service.load_records", return_value=[]):
        with patch("service.save_records", return_value=True):
            user = create_user({
                "name": "Sara Sofia",
                "email": "sara@gmail.com",
                "age": 20,
                "role": "admin"
            })
            assert user["name"] == "Sara Sofia"
            assert user["email"] == "sara@gmail.com"
            assert "id" in user
