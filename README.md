# Estimador de Precios de Viviendas en Santa Cruz de la Sierra
## Resumen del proyecto
* Se creó una herramienta que permite **estimar el precio de viviendas** en Santa Cruz de la Sierra. Esto con el fin de proveer una primera aproximación del precio para una diversidad de escenarios.
* Los datos se extrajeron de páginas donde se ofertan viviendas, en las cuales vienen incluidos el precio y una diferentes características de las mismas. Se utilizó técnicas de **web scraping** para este propósito.
* Se preprocesaron y se aplicaron técnicas de **feature engineering** a los datos para extraer características útiles para el modelado.
* Se entrenaron diversos algortimos de regression, utilizando **grid search** para optimizar los *hiperparámetros* y obtener el mejor modelo. Los modelos puestos a prueba fueron: *Lasso Regression*, *Ridge Regression*, *Random Rorest Regressor*, *Support Vector Regression*, *Gradient Boosting Regressor* y *KNN regressor*.
* Se contruyó una **página web** que permite utilizar el modelo seleccionado. En la misma tambén se hace accesible un **dashboard** para explorar la base de datos utilizada.

## Página Web
La herramienta se hace accesible a través de la siguiente página web, hosting provisto por Google Cloud:

[https://bienes-raices-scz-ohh5653uva-uc.a.run.app/](https://bienes-raices-scz-ohh5653uva-uc.a.run.app/)

## Requerimientos
* **Versión de Python:** 3.10
* **Librerias:** selenium, numpy, pandas, matplotlib, seaborn, scikit-learn, plotly, dash
* **Requerimientos para reproducir el analisis:** requirements.txt
* **Conda environment:** environment.yml
* **Requerimientos para la app:** requirements_app.txt

## Web Scraping
Los datos se obtuvieron de páginas en las que se ofertan viviendas. Junto con el precio, también se listan diversas características tales como dimensiones, número de ambientes, ubicación, entre otros. 

De ellas se escogieron las siguientes: Descripción de la propiedad, Precio, Descripción de la ubicación, Número de ambientes, Número de baños, Terreno (en m2), Año de construcción, Número de dormitorios, Área construida, Número de estacionamientos, Ubicación: latitud y longitud.

Para este paso se utilizó **Selenium** y se obtuvo un total de 1520 propiedades para su posterior análisis.

## Prepocesado de los datos
Los datos tuvieron que pasar por un proceso de preprocesado para asegurar la calidad de los mismos. Los pasos:
* De la descripción de la ubicación se extrajo la ciudad y la zona.
* Se aseguró la consistencia de la fecha de construcción y únicamente se tomó el año.
* Se quitaron decimales a las coordenadas, por temas de privacidad.
* Al inspeccionar los valores repetidos, se pudo constatar que en su mayoría corresponde a diferentes propiedades pero dentro del mismo proyecto inmobiliario. Por ello, se conservan estos puntos para el modelado.

## Análisis Exploratorio de los Datos
El primer paso en esta etapa fue explorar los valores faltantes y escoger técnicas de imputación de los mismos para cada caso. En el caso del número de ambientes, se seleccionó *KNN-imputer* donde el número de *neighbors* se tomó como *hiperparámetro* a seleccionar en la siguiente etapa.

Luego, se aseguró el correcto formato, *data type*, de cada columna.

Una vez se tuvo una base de datos limpia, se procedió a analizar distintas visualizaciones. A continuación se muestran las más destacadas.

<img src="images/arma.png" alt="Alt text 1" width="400"/> 

picture1 picture2_1 picture2_2 picture3_1

## Licencia 
GNU General Public License v2.0

## Autor
Antonio Jimenez Caballero
