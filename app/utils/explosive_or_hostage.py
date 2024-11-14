

def contain_explosive(person):
    # Check if any value in the `person` dictionary contains the word "explosive"
    return any("explosive" in str(value).lower() for value in person.())
def contain_hostage(person):
    return True