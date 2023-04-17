alert('durrr')
const letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";


const text = document.querySelector(".texteffect");
let flash = true;
const interval2 = setInterval(() => {
    if(iterations%5==0)
        if(flash)
            flash = false;
        else
            flash = true;
    if(flash)
        text.target.innerText = text.target.innerText.substring(0,length-1) + '\xa0' //blank char
    else
        text.target.innerText = text.target.innerText.substring(0,length-1) + "_" //underscore
        iterations += 1;
}, 30);



document.querySelector(".texteffect").onmouseover = event => {
    let iterations = 0;
    let length = event.target.dataset.value.length;

    const interval = setInterval(() => {
        //Split at every character
        event.target.innerText = event.target.innerText.split("")
        .map((letter, index) => {
            if(index < iterations){
                return event.target.dataset.value[index];
            }
            if(letter == '_')
                return '_'
            return letters[Math.floor(Math.random()*26)]
        })
        .join("");  //join them back together
        


        
        //set max iteration count to length of the word
        if(iterations >= event.target.dataset.value.length){
            clearInterval(interval);
            
        }
        
        iterations += 1;
    }, 30);
}