def realState_url(page):
    '''
    Construye la url de remax. Para modificar los valores es necesario
    ir a la página y seleccionar los diversos filtros
    '''
    tt = '261' #En Venta
    mpts = '19418,19420,19430' #Departamentos, Casa, Penthouse
    pt = '19418'
    page = str(page)
    pm = '50487'
    lsgeo = '2800,50487,0,0' #Andres Ibañés
    sid = 'e1083e16-9f2d-4c67-bab4-45bdb9ec1b0a' #Sesión'

    url = f'''https://www.remax.bo/publiclistinglist.aspx#mode=list&\
tt={tt}&\
mpts={mpts}&pt={pt}&\
cur=USD&\
sb=PriceIncreasing&\
page={page}&\
sc=120&\
pm={pm}&lsgeo={lsgeo}&\
sid={sid}'''
    return url