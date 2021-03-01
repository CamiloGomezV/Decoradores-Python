# Laboratorio 7
## Problema planteado

Se necesita la implementacion de un software que facilite el conteo de puntos durante un combate de taekwondo. En estos combates se suele utilizar equipo electronico, con el cual, dada una potencia se manda una senal indicando el tipo de punto, ya sea punto a la cabeza o punto al torso y con ello, se suma al contador del debido peleador. En algunos casos estos equipos electronicos fallan, cuando esto pasa, los jueces presentes en el combate, marcan los puntos mediante un sistema de control remoto, en este caso, cada que un competidor ejecuta un ataque, indican la zona en la que fue realizada el ataque y si esta fue valida o no. Es decir, si el competidor de color rojo realiza una tecnica a la cabeza, los jueces indicaran que la tecnica fue a la cabeza y si fue valida (True) o si no (invalida).

## Solucion
Se plantea una funcion inicial la cual se encarga de sumar los puntos que marca cada competidor de acuerdo al lugar del cuerpo donde se marco el punto (Cabeza o parte media). Se implementa un decorador que, si se recibe una lista con la calificacion de los jueces respecto a una tecnica (una lista de booleanos) se rectifica si en esta lista hay por lo menos 2 valores verdaderos, de lo contrario se notificara que el punto fue invalido.
