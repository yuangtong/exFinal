function incrementarNumero()
{
    numeroAumentar = document.getElementById('num')
    nuevoNumero = Number(numeroAumentar.innerHTML) + 1
    numeroAumentar.innerHTML = String(nuevoNumero)
}

function disminuirNumero()
{
    numeroAumentar = document.getElementById('num')
    nuevoNumero = Number(numeroAumentar.innerHTML) - 1
    numeroAumentar.innerHTML = String(nuevoNumero)
}

function cambiarColor()
{
    console.log("El mouse esta sobre el Div")
    divisionColor = document.getElementById('divisionColor')
    divisionColor.style.backgroundColor = 'red'
}

function devolverColor()
{
    console.log("El mouse salio del Div")
    divisionColor = document.getElementById('divisionColor')
    divisionColor.style.backgroundColor = 'blue'
}

function imprimirSeleccion()
{
    console.log("Se ha ingresado a imprimirSeleccion")
    numSeleccionado = document.getElementById('numSeleccionado')
    console.log("Se ha seleccionado %s",numSeleccionado.value)
    nuevoNumero = document.getElementById('nuevoNumero')
    nuevoNumero.value = numSeleccionado.value
}

function agregarNumero()
{
    nuevoNumero = document.getElementById('nuevoNumero')
    listaNumeros = document.getElementById('listaNumeros')
    listaNumeros.innerHTML = listaNumeros.innerHTML + `<li class='numeroLista'>${nuevoNumero.value}</li>`
}

function sumarTodosNumeros()
{
    arregloLista = document.querySelectorAll('.numeroLista')
    let sumaTotal = 0
    for(let i = 0; i < arregloLista.length; i++)
    {
        numTemp = Number(arregloLista[i].innerHTML)
        sumaTotal = sumaTotal + numTemp
    }
    sumaFinal = document.getElementById('sumaFinal')
    sumaFinal.innerHTML = String(sumaTotal)
}