def update_user(users, user_id, new_data):
    for u in users:
        if u["id"] == user_id:
            u.update(new_data)
            return True
    return False
