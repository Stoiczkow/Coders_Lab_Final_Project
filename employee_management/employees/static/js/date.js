document.addEventListener("DOMContentLoaded", function(){

var start = document.querySelector("#id_start_date")
var end = document.querySelector("#id_end_date")
start.removeAttribute("type")
start.setAttribute("type", "date")

end.removeAttribute("type")
end.setAttribute("type", "date")

});