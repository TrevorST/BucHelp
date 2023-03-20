const letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
alert("yo");
document.querySelector(".texteffect").onmouseover = event => {
    let iterations = 0;
    let length = event.target.dataset.value.length;
    let flash = true;
    

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
        if(iterations >= event.target.dataset.value.length*5){
            clearInterval(interval);
            
        }
        
        iterations += 1;
    }, 30);
}