# Estimador de Precios de Viviendas en Santa Cruz de la Sierra
## Resumen del proyecto
* Se creó una herramienta que permite **estimar el precio de viviendas** en Santa Cruz de la Sierra. Esto con el fin de proveer una primera aproximación del precio para una diversidad de escenarios.
* Los datos se extrajeron de páginas donde se ofertan viviendas, en las cuales vienen incluidos el precio y una diferentes características de las mismas. Se utilizó técnicas de **webscraping** para este propósito.
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

## Licencia 
GNU General Public License v2.0

## Autor
Antonio Jimenez Caballero
