import time
import os
import sqlite3
import numpy as np
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException

from utilityFunctions.realState_url import realState_url

#funciones utilitarias para obtener url, links y datos
def get_links(driver, init, fin):
    '''
    Extrae los links de cada página de la web especificada
    '''
    links = []
    for i in range(init,fin,1):
        #connect to the website page
        website = realState_url(i)
        print(website)
        driver.get(website)
        time.sleep(7)

        prices_link = driver.find_elements("xpath", '//a[@class="proplist_price"]')

        for price_link in prices_link:
            #extract the links
            links.append(price_link.get_attribute("href"))
            #print(price_link.get_attribute("href"))
    return links

def get_data(driver, links, conn):
    '''
    Obtiene los datos desde los links especificados
    '''
    cursor = conn.cursor()
    create_table_query = '''
CREATE TABLE IF NOT EXISTS properties (
    titulo TEXT,
    descripcion TEXT,
    precio REAL,
    ubicacion_descr TEXT,
    ambientes INTEGER,
    no_baños INTEGER,
    terreno_m2 REAL,
    fecha_mes_constr TEXT,
    año_constr INTEGER,
    no_dormitorios INTEGER,
    area_constr_m2 REAL,
    estacionamientos INTEGER,
    latitud REAL,
    longitud REAL
)
'''
    cursor.execute(create_table_query)
    conn.commit()

    counter = 1

    for link in links:
        print(f"\n\npropiedad no. {counter}")
        print(link)
        counter += 1

        #extract info from each page
        driver.get(link)
        time.sleep(5)
        row_data = []
        try:
            titulo = driver.find_element("xpath", '//h1[@itemprop="name"]')
            row_data.append(titulo.get_attribute("innerHTML"))
            print('titulo:',titulo.get_attribute("innerHTML"))
        except NoSuchElementException:
            row_data.append(None)
            continue
        try:
            descripcion = driver.find_element("xpath", '//h2[@class="fts-mark fts-small"]')
            row_data.append(descripcion.get_attribute("innerHTML"))
            print('descripcion:', descripcion.get_attribute("innerHTML"))
        except NoSuchElementException:
            row_data.append(None)
            continue
        try:
            precio = driver.find_element("xpath", '//a[@itemprop="price"]')
            row_data.append(precio.get_attribute("content"))
            print('precio:', precio.get_attribute("content"))
        except NoSuchElementException:
            row_data.append(None)
            continue

        try:
            ubicacion_descr = driver.find_element("xpath", '//div[@class="col-xs-12 key-address fts-mark"]')
            row_data.append(ubicacion_descr.get_attribute("innerHTML"))
            print('ubicacion_descr:', ubicacion_descr.get_attribute("innerHTML"))
        except NoSuchElementException:
            row_data.append(None)
            continue

        try:
            ambientes = driver.find_element("xpath", "//div[@class='data-item-row']//div[@class='data-item-label' and span='Total de Ambientes:']/following-sibling::div[@class='data-item-value']/span")
            row_data.append(ambientes.get_attribute("innerHTML"))
            print('ambientes:', ambientes.get_attribute("innerHTML"))
        except NoSuchElementException:
            row_data.append(None)
            print('no ambientes')

        try:
            no_baños = driver.find_element("xpath", "//div[@class='data-item-row']//div[@class='data-item-label' and span='Baños:']/following-sibling::div[@class='data-item-value']/span")
            row_data.append(no_baños.get_attribute("innerHTML"))
            print('no_baños', no_baños.get_attribute("innerHTML"))
        except NoSuchElementException:
            row_data.append(None)
            print('no numero baños')

        try:
            terreno_m2 = driver.find_element("xpath", "//div[@class='data-item-row']//div[@class='data-item-label' and span='Terreno (m2)']/following-sibling::div[@class='data-item-value']/span")
            row_data.append(terreno_m2.get_attribute("innerHTML"))
            print('terreno_m2:', terreno_m2.get_attribute("innerHTML"))
        except NoSuchElementException:
            row_data.append(None)
            print('no terreno_m2')

        try:
            fecha_mes_constr = driver.find_element("xpath", "//div[@class='data-item-row']//div[@class='data-item-label' and span='Año/Mes construido']/following-sibling::div[@class='data-item-value']/span")
            row_data.append(fecha_mes_constr.get_attribute("innerHTML"))
            print('fecha_mes_constr', fecha_mes_constr.get_attribute("innerHTML"))
        except NoSuchElementException:
            row_data.append(None)
            print("no fecha/mes")
        try:
            año_constr = driver.find_element("xpath", "//div[@class='data-item-row']//div[@class='data-item-label' and span='Año Construcción']/following-sibling::div[@class='data-item-value']/span")
            row_data.append(año_constr.get_attribute("innerHTML"))
            print('año_constr/mes', año_constr.get_attribute("innerHTML"))
        except NoSuchElementException:
            row_data.append(None)
            print("no fecha/mes")
        try:
            no_dormitorios = driver.find_element("xpath", "//div[@class='data-item-row']//div[@class='data-item-label' and span='Num. de Dormitorios:']/following-sibling::div[@class='data-item-value']/span")
            print('dormitorios', no_dormitorios.get_attribute("innerHTML"))
            row_data.append(no_dormitorios.get_attribute("innerHTML"))
        except NoSuchElementException:
            print("no dormitorios")
            row_data.append(None)
        try:
            area_constr_m2 = driver.find_element("xpath", "//div[@class='data-item-row']//div[@class='data-item-label' and span='Area Construcción (m²)']/following-sibling::div[@class='data-item-value']/span")
            print('area_constr_m2', area_constr_m2.get_attribute("innerHTML"))
            row_data.append(area_constr_m2.get_attribute("innerHTML"))
        except NoSuchElementException:
            print("no area_constr_m2")
            row_data.append(None)
        try:
            estacionamientos = driver.find_element("xpath", "//div[@class='data-item-row']//div[@class='data-item-label' and span='Estacionamientos']/following-sibling::div[@class='data-item-value']/span")
            print('estacionamientos', estacionamientos.get_attribute("innerHTML"))
            row_data.append(estacionamientos.get_attribute("innerHTML"))
        except NoSuchElementException:
            print("no estacionamientos")
            row_data.append(None)

        try:
            location = driver.find_element("xpath", '//input[@id="listingfull-map-toggler"]')
            lat = location.get_attribute("data-lat")
            row_data.append(lat)
            lng = location.get_attribute("data-lng")
            row_data.append(lng)
            print(f"Latitude: {lat}, Longitude: {lng}")
        except:
            row_data.append(None)
            row_data.append(None)
            print('no coordenadas')

        insert_query = '''INSERT INTO properties VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
        cursor.execute(insert_query, row_data)
        conn.commit()

    return None

def export_2_db_data(driver, links, db_name):
    '''
    Exporta los datos a una base de datos
    '''
    #inicializando la base de datos
    database_path = f'../data/{db_name}'
    conn = sqlite3.connect(database_path)

    #retrieve the data
    get_data(driver, links, conn)

    #cerrar conección
    conn.close()

    return None

# Main

#inicializando selenium
service_path = '../chromedriver/chromedriver.exe'
service = Service(service_path)
driver = webdriver.Chrome(service = service)

#obteniendo los datos desde pag_init hasta pag_fin
pag_init = 60
pag_fin = 61 #última revisión: pag_fin=62+1 (python range)
db_name = 'raw_realState_data_testFunction.db'

#webscraping (24 propiedades por página)
links = get_links(driver, pag_init, pag_fin)
export_2_db_data(driver, links[1:2], db_name)

#cerrando webdriver
driver.quit()
