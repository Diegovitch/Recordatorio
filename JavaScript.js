// 1. Como hacer una variable en JavaScript: Para hacer una variable en JS es necesario usar el codigo "var" para poder declarar una variable, además de usar el ";" al final de cada variable
//var que = "so"; // Esta variable con un string porque lleva "."
//var numero = 30; // Esta variable que tiene un valor Númerico

// 2. Como hacer un cuadro de advertencia: Para hacer un cuadro de advertencia usaras la función "alert"
//alert("Advertence");

// 3. Como hacer un diálogo: Con la función "Prompt" podras hacer un diálogo, un dialogo se usa para para interactuar con el navegador respondiendo sus mensajes
//prompt("Ecriba su nombre");

// 4. como aumentar el valor de una variable: Usamos el "++" y si queremos disminuirlo es "--"
//var valor = 10;
//++valor;
//--valor;

//Y si nescesitas reducirlo o aumentar su valor predeterminado sin usar el "++" coloca este código:
//valor +=5;
//valor -=5;

//Puedes probar con diferentes operaciones arimeticas como estas
//valor /=5;
//valor *=5;

// 5. Como contar un string: Para contar una variable con string tendrás que usar la función "Length"
//var cantidad = "Paramericurucutuguaro";
//cantidad.length;
//Para tambien si quieres llamar una letra según su número utiliza este código
//cantidad[4]

// 6. Los arreglos: los arreglos son listas que tienes varios elementos:
//var frutas = ["Cambur", "Manzana", "Pera", "Parchita"]

//Como añadir un nuevo elemento al arreglo:
//frutas[2] = "kiwi"

//Como añadir un elemento de ultimo a un arreglo:
//frutas.push("Mandarina")

//Contar los elementos de un arreglo
//frutas.length

//Como añadir un elemento al inicio del arreglo:
//frutas.unshift("Plátano")

//Como eliminar un elemento de un arreglo:
//frutas.pop("Cambur")

//Eliminar el primer elemento de un arreglo:
//frutas.shift()

//Unificar elementos de un arreglo:
//var computadoras = ["hP", "AlienWare"]
//var computadoras2 = ["Lenovo", "Dell"]
//var unificar = computadoras.concat(computadoras2)

// Como saber el valor de un elemento de un arreglo:
//frutas.indexOf("Manzana")

// 7. Distintos tipos de datos de un arreglo: Se puede colocar diferentes tipos de datos dentro de un arreglo, como si fuera una lista dentro de otra
//var figuritas = ["Triangulos", 3, [4, 2], 14]

// 8. Condicional If en JS:Los condicionales IF, son una estructura de control condicional, también llamadas estructuras selectivas de casos simples (porque solo definen un posible flujo), las cuales nos permiten tomar cierta decisión al interior de nuestro algoritmo, es decir, determinar qué acciones ejecutar según cierta condición sea
//var palabra=prompt("Escribe una palabra")
//if(palabra.length >7){
//    document.write("Es una palabra larga")//Este código se corre en pagianas webs
//}

// 9. Condicional ELSE en JS:El condicional Else sirve en conjunto con el condicional IF, se usa si se cumple cierta condición en IF, para que else corra otra respuesta
//var palabra=prompt("Escribe una palabra")
//if(palabra.length >7){
//    document.write("Es una palabra larga")
//}else{
//    document.write("Es una palabra corta")
//}

//10. Condicional While: La condicional While es una de las condicioanles más importantes ya que repite una condición
//document.write("Comienza contar")
//var contador = 0;
//while(contador < 12) {
//    document. write(contador + " ")
//    contador++;
//}
//document.write("Dejo de contar")

//11. instrucción for: La instrucción for permite repetir una instrucción o una instrucción compuesta un número especificado de veces, más o menos como hace While
document.write("Comienza a ejucutar el comando for")
for (var contador = 0; contador < 12; contador++) {
    document.write(contador + " ")
}
document.write("dejo de contar")