def validate_request(structure, payload):
    errors = []
    for entity in structure:
        if structure[entity]["required"]:
            entity_value = payload.get(entity, None)
            if entity_value is None:
                errors.append(f"{structure[entity]['verbose_name']} not provided")

    return len(errors) == 0, errors
