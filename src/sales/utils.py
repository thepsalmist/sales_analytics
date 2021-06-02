import uuid


def generate_code():
    # generates a uuid replaces all the hyphens with and limits to 12 characters
    code = str(uuid.uuid4()).replace("-", "")[:12]
    return code
