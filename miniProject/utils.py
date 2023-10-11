from datetime import datetime

def getDatetime():
    return str(datetime.today()).split('.')[0].replace(' ', '_').replace('-', '').replace(':', '') + '_'
