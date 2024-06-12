const days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
let date = new Date();
let day = date.getDay()
for(let i = 0; i < 7; i++){
    document.querySelector("#day" + (i + 1)).textContent = days[(i + day ) % 7] ;
}