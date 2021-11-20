# EB-2021-1-CC51 Trending Youtube Video Statistics: Administración De La Información
# Objetivos
En este proyecto final, se va a realizar un Análisis Exploratorio de Datos y , con ello, ofrecer una solución  a un problema de Modelización de datos. En este sentido, el proyecto nos pide evaluar y predecir las tendencias de	los videos de Youtube de un determinado país. Con el conocimiento generado a partir de un conjunto de datos que recopila todos los registros diarios de los videos con mayor tendencia de Youtube, se atenderá la necesidad de una importante empresa de marketing digital que desea responder a diversos requerimientos de información.
# Autores 
* Paredes Villagra, Renzo Arturo      renzorapv@gmail.com
* Flores Ñahuis, Sergio Andres        flores.ofiuco.sergio@gmail.com
# Breve Descripción
Dentro de este documento se responden los siguiente temas relacionado con el conjunto de datos llamado Trending Youtube Video Statistics: CASOS DE ANALISIS, CONJUNTO DE DATOS (DATA SET), ANÁLISIS EXPLORATORIO DE DATOS, MODELIZAR Y EVALUAR LOS DATOS, CONCLUSIONES DEL PROYECTO. Y el código presente en este GitHub permite ayudar a comprender y responder todos los temas del documento.
# Conclusiones
1. Las categorías de videos con mayor tendencia son Gaming, Movies y Music.

2. Las categorías de videos que más gustan con respecto a los likes son Pets & Animals, Gaming y Music; y los que menos gustan son Travel & Events, Shows y News & Politics. Y con respecto a los dislikes los videos que más gustan son Travel & Events, Autos & Vehicles y Shows y News & Politics; y los que menos gustan son Gaming, Music y Film & Animation.

3. Las categorías de videos que tienen la mejor proporción de “Me gusta” / “No me gusta” son Education, Pets & Animals y Nonprofits & Activism.

4. Las categorías de videos que tienen la mejor proporción de “Vistas” / “Comentarios” son Sports, Travel & Events y Entertainment.

5. Con respecto a la cantidad de videos en tendencia, tuvo un gran aumento en el mes de Diciembre de 2017 luego se mantuvo con aproximadamente la misma cantidad hasta el mes de Mayo de 2018, y por último  al siguiente mes disminuyó  bastante la cantidad de videos en tendencia.

6. Los canales de YouTube que son tendencia más frecuentemente son etvteluguindia, VikatanTV y Flowers Comedy, y con respecto a los que son tendencia menos frecuentes se encuentran bastantes canales, ya que estos tan solo cuentan con tan solo una aparición en tendencia y los más posible que estos nunca vuelvan a estar en tendencia de nuevo, algunos de estos canales son Trending Today , Business Of Cinema, Bollywood Sins y Ilumination.

7. Los Estados que presentan el mayor número de “Vistas” son West Bengal, Andhra Pradesh y Chandigarh.
Los Estados que presentan el mayor número de “Me gusta” son West Bengal, Nagaland y Haryana.
Los Estados que presentan el mayor número de “No me gusta” son Chandigarh, Andhra Pradesh y West Bengal.

8. Luego de haber efectuado un modelo de regresión logística para medir la factibilidad de predicción del número de “Vistas” o “Me gusta” o “No me gusta”, se descubrió lo siguiente:
En el caso de “Vistas”, hubo una precisión del 43% para identificar correctamente los valores de la clase “alto”, una precisión del 82% para identificar correctamente los valores de la clase “medio” y una precisión del 74% para identificar correctamente los valores de la clase “bajo” de la variable “views”. Adicionalmente, se detectó una precisión ponderada total del 77%. Por lo tanto, podemos afirmar que es posible predecir a qué clase puede pertenecer la cantidad de “Vistas” de un video en tendencias.

En el caso de “Me gusta”, hubo una precisión del 74% para identificar correctamente los valores de la clase “alto”, una precisión del 67% para identificar correctamente los valores de la clase “medio” y una precisión del 85% para identificar correctamente los valores de la clase “bajo” de la variable “views”. Adicionalmente, se detectó una precisión ponderada total del 80% . Por tal razón, podemos afirmar que es posible predecir a qué clase puede pertenecer la cantidad de “Vistas” de un video en tendencias.


En el caso de “No me gusta”, hubo una precisión del 5% para identificar correctamente los valores de la clase “alto”, una precisión del 37% para identificar correctamente los valores de la clase “medio” y una precisión del 82% para identificar correctamente los valores de la clase “bajo” de la variable “views”. Adicionalmente, se detectó una precisión ponderada total del 66%, lo cual no resulta ser un porcentaje alto o aceptable de aciertos que produjo nuestro modelo. Por ese motivo, no es muy adecuado predecir a qué clase puede pertenecer la cantidad de “Vistas” de un video en tendencias.

9. Si, los videos en tendencia son los que mayor cantidad de comentarios positivos reciben.
# Licencia
Se ha acordado usar para este proyecto analítico la licencia [Atribución-NoComercial-CompartirIgual 4.0 Internacional (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.es)

