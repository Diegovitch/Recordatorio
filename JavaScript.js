//1. Como hacer una variable en JavaScript: Para hacer una variable en JS es necesario usar el codigo "var" para poder declarar una variable, además de usar el ";" al final de cada variable
//var que = "so"; // Esta variable con un string porque lleva "."
//var numero = 30; // Esta variable que tiene un valor Númerico

//2. Como hacer un cuadro de advertencia: Para hacer un cuadro de advertencia usaras la función "alert"
//alert("Advertence");

//3. Como hacer un diálogo: Con la función "Prompt" podras hacer un diálogo, un dialogo se usa para para interactuar con el navegador respondiendo sus mensajes
//prompt("Ecriba su nombre");

//4. como aumentar el valor de una variable: Usamos el "++" y si queremos disminuirlo es "--"
//var valor = 10;
//++valor;
//--valor;

//Y si nescesitas reducirlo o aumentar su valor predeterminado sin usar el "++" coloca este código:
//valor +=5;
//valor -=5;

//Puedes probar con diferentes operaciones arimeticas como estas
//valor /=5;
//valor *=5;

//5. Como contar un string: Para contar una variable con string tendrás que usar la función "Length"
//var cantidad = "Paramericurucutuguaro";
//cantidad.length;
//Para tambien si quieres llamar una letra según su número utiliza este código
//cantidad[4]

//6. Los arreglos: los arreglos son listas que tienes varios elementos:
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

//7. Distintos tipos de datos de un arreglo: Se puede colocar diferentes tipos de datos dentro de un arreglo, como si fuera una lista dentro de otra
//var figuritas = ["Triangulos", 3, [4, 2], 14]

//8. Condicional If en JS:Los condicionales IF, son una estructura de control condicional, también llamadas estructuras selectivas de casos simples (porque solo definen un posible flujo), las cuales nos permiten tomar cierta decisión al interior de nuestro algoritmo, es decir, determinar qué acciones ejecutar según cierta condición sea
//var palabra=prompt("Escribe una palabra")
//if(palabra.length >7){
//    document.write("Es una palabra larga")//Este código se corre en pagianas webs
//}

//9. Condicional ELSE en JS:El condicional Else sirve en conjunto con el condicional IF, se usa si se cumple cierta condición en IF, para que else corra otra respuesta
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
//document.write("Comienza a ejucutar el comando for")
//for (var contador = 0; contador < 12; contador++) {
//    document.write(contador + " ")
//}
//document.write("dejo de contar")

//12. Objeto en JS: un objeto en JS es una variable que tiene aspectos especificos, como por ejemplo:
// var empanada_carnemolida = {
//     aliños: "Agí, cebolla, pimenton",
//     relleno: "Carne molida",
//     salsas: "salsa rosada y wasakaka se le pueden hechar"
// }

//   //13. Como modificar un objeto
// var empanada_carnemechada = {
//     aliños: "Agí y pimenton",
//     relleno: "carnemolida",
//     salsas: "mayonesa"
// }

// var empanada_carnemechada = new Object();
// empanada_carnemechada.relleno = "Carne Mechada"
// empanada_carnemechada.salsas = "Salsa rosada y mayonesa"
// empanada_carnemechada.aliños = "Agí y pimenton"

//13. Códigos que configuran los obejetos
  //Instrucción console.log: esta instrucción asegura si hay una propiedad o no, funcionan con las condicionales true y false
// var carrito_verdura = {
//     verduras: "papa, yuca y ñame"
// }

//console.log("verduras" in carrito_verdura)
  
  //Insttrucción delete: esta instrucción te permite borrar una propiedad del objeto
// var preparar_cereal = {
//     soporte: "tazón",
//     liquido: "leche",
//     cereal: "crunch flakes",
//     sobras: "cambur"
//}

//delete preparar_cereal.sobras

// 14. Un arreglo de objetos: Un arreglo de objetos es una lista que tiene varios objetos

// var calificaciones_estudiantes = [
//     {nombre: "Samuel", calificiones_matemáticas: 10},
//     {nombre: "Diego", calificiones_matemáticas: 7},
//     {nombre: "Krislady", calificiones_matemáticas: 4},
// ];

 // Otra forma de hacer un arreglo 

// var libros = {
//     "El ente": {
//         autor: "frank de felita",
//         paginas: 477
//     },
//     "Monigote pamplinas": {
//         autor: "Colmenares, Hugo",
//         páginas: "??"
//     }
// };

// 15. Una función: Las funciones pueden generar valores utilizados en el programa que están definidas

//var simplificación = function(numero) {
//  return numero*2
//}

//simplificación(90/40)

 // Tambien puedes probar en hacer funciones de primer grado
//var fex_1 = function(x) {
//  return 3*x +5
//}
 // Crear una función que sirva como contador
//var contador = function(tiempo){
//  for (var contador = 0; contador < tiempo; contador ++){
//    document.write(contador+ "");
//  }
//};

 // Además puedes hacer que las funciones que creaste se dividan, multipliquen, sumen y resten con valores externos
//var cuadrado = function(elevado2){
//  return elevado2*2 
//}

//90/cuadrado(30)

// 16. Algunas funciones de JS predefinidas
//Math.random() // Hace números aleatorios
//Math.floor(6475,09040932)// Hace transformar números decimales en enteros

 // También con las funciones vistas podemos unirlas o dicho combinarlas como el siguiente ejemplo
//Math.floor(Math.random()*100)

 // Además de combinar funciones con otras funciones podemos hacer un arreglo o lista
var frutas = ("Pera", "Manzana", "Fresa")
contaralazar = Math.floor(Math.random()*frutas.length)

 // Otro modo para jugar con las funciones es hacer funciones que tenga otras funciones, como en este ejemplo
var alazar = function(elegir){
  return elegir[Math.floor(Math.random()*elegir.length)]
};
var palabras = ["¿Donde", "están", "las", "Rubias?"];
alazar(palabras)