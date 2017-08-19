from models import daftar_buku
def run_view():
    print('Daftar Teman')
    print('---')

    for db in daftar_buku:
        print(db)