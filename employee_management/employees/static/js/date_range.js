document.addEventListener("DOMContentLoaded", function(){

var btn = document.querySelector("#choose")

btn.addEventListener("click", function (event) {

var from_date = document.querySelector("#from")
var to_date = document.querySelector("#to")
var tasks = document.querySelectorAll("p")

console.log(from_date.value)
console.log(to_date.value)
console.log(tasks)
for(var i = 0; i < tasks.length; i++){
    console.log(tasks[i].value2)
}
if(from_date.value <= to_date.value){

}
});

});