from configparser import ConfigParser

def config(filename = r'C:\\Users\\kkozh\\OneDrive\\Documents\\PrinProg2\\PP2_2025\\PP2\\lab10\\1\\database.ini', section = 'postgresql'):
    parser = ConfigParser()
    parser.read(filename)

    db = {}
    if parser.has_section(section):
        confs = parser.items(section)
        for conf in confs:
            db[conf[0]] = conf[1]
    
    else:
        raise Exception(f'Section {section} not found in the {filename} file')
    
    return db