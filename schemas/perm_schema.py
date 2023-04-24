def perm_serializer(perm) -> dict:
    return {
        'id':str(perm["_id"]),
        'org_name':perm["org_name"],
        "user_id":perm["user_id"],
        'access_level':perm["access_level"]
    }

def perms_serializer(perms) -> list:
    return [perm_serializer(perm) for perm in perms]