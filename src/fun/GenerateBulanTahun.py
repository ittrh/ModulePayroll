import locale
from datetime import datetime

def generate_bulan_tahun():
    try:
        locale.setlocale(locale.LC_TIME, 'id_ID.utf8')
    except locale.Error:
        locale.setlocale(locale.LC_TIME, 'Indonesian')
        
    sekarang = datetime.now()
    
    hasil = sekarang.strftime("%B %Y")
    return hasil

# try:
#     locale.setlocale(locale.LC_TIME, 'id_ID.utf8')
# except locale.Error:
#     locale.setlocale(locale.LC_TIME, 'Indonesian')
        
# sekarang = datetime.now()
    
# hasil = sekarang.strftime("%B %Y")
# print(hasil)