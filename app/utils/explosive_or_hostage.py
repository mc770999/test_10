

def contain_explosive(person):
    return any("explosive" in str(value).lower() for value in person["sentences"])


def contain_hostage(person):
    return any("hostage" in str(value).lower() for value in person["sentences"])