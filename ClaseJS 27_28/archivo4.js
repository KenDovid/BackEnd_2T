let var1 = true;
let var2 = false;

if (var1 === true && var2 === true){
    console.log("Ambos son verdaderos.")
}

else if(var1 === true || var2 === true){
    console.log("Una de las dos variables son verdaderas.")
}

else{
    console.log("Ninguna de las dos variables son verdaderas.")
}