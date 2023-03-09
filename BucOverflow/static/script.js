const letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
document.querySelector(".texteffect").onmouseover = event => {
    let iterations = 0;

    const interval = setInterval(() => {
        //Split at every character
        event.target.innerText = event.target.innerText.split("")
        .map((letter, index) => {
            if(index < iterations){
                return event.target.dataset.value[index];
            }
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