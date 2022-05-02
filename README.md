## TPs de Algoritmos y Programación 1

Ejercicios y TPs hechos durante la cursada de la materia [Algoritmos y Programación 1, curso Essaya](https://algoritmos1rw.ddns.net/). Es la primera materia de programación para los alumnos de ingeniería informática en la Facultad de Ingeniería de la Universidad de Buenos Aires. Yo la cursé mientras hacía mi Doctorado, durante el segundo cuatrimestre de 2019. Los TPs consistieron en programar el juego de la "viborita" (snake) y en resolver un laberinto usando backtracking.

### Snake
Para jugar al Snake, desde la terminal de Linux ubicarse en la carpeta TP1-Snake y correr

`python3 snake_segundaentrega.py`

En esta primera versión el juego consiste en comer "frutas" hasta una cantidad máxima tras lo cual se gana el juego. Cada vez que se come una fruta la viborita se alarga. Se pierde si la viborita toca una pared o a si misma.

![](https://github.com/lucaspavlov/algoritmos1/blob/master/TP1-Snake/snake.gif)


### Snake++

En la versión "mejorada" del Snake se agregan distintos niveles, obstáculos en el medio del tablero, y "efectos especiales" (cambio en la velocidad o en el largo de la viborita). Cuando la viborita come alguno de estos especiales, los mismos se guardan en una mochila y luego se pueden activar tocando alguna tecla. Para jugar, pararse en la carpeta TP2-Snake++ desde la Terminal y correr

`python3 snakeplus.py`

![](https://github.com/lucaspavlov/algoritmos1/blob/master/TP2-Snake%2B%2B/snake%2B%2B.gif)

La interacción entre la terminal y el usuario se hace a partir de un archivo .py provisto por la cátedra.
