class ImmutableMappingError(Exception):
    pass

def enforce_stability(existing_locked: bool):
    if existing_locked:
        raise ImmutableMappingError("Mapping is locked and cannot be changed.")