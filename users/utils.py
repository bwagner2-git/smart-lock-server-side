import uuid

def get_random_code():
    code=str(uuid.uuid4())[:8].replace('-','').lower()    ###trying uuid4 instead of 5 change back and figure out if this gives problems
    return code