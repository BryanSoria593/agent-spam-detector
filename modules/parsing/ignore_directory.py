def get_non_ignored_directory(path):
    try:
        words = ['incoming']
        if any(word in path for word in words):
            return False
        return True

    except Exception as e:
        prin('No tiene permisos para leer el directorio' + str(e))