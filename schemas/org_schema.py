def org_serializer(org) -> dict:
    return {
        'id':str(org["_id"]),
        'name':org["name"],
    }

def orgs_serializer(orgs) -> list:
    return [org_serializer(org) for org in orgs]