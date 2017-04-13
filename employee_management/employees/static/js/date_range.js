document.addEventListener("DOMContentLoaded", function(){

var btn = document.querySelector("#choose")

btn.addEventListener("click", function (event) {

var from_date = document.querySelector("#from")
var to_date = document.querySelector("#to")
var tasks = document.querySelectorAll(".label-info")
from_date = new Date(from_date.value)
to_date = new Date(to_date.value)

for(var i = 0; i < tasks.length; i++){
    var compare_date = new Date(tasks[i].getAttribute("value2"))

    if(from_date <= compare_date  && compare_date <= to_date){
        tasks[i].classList.remove("hidden")
    }else{
        tasks[i].classList.add("hidden")
    }

}


});

btn.addEventListener("click", function (event) {

var tasks= document.querySelectorAll('.label')
    var dataTasks = []
    for(var i = 0; i < tasks.length; i++){
        if(tasks[i].classList.contains("hidden")){
            continue;
        }else{
            dataTasks.push({ label: String(tasks[i].getAttribute('value2')),  y: parseInt(tasks[i].getAttribute('value')) })
        }

    }

	var chart = new CanvasJS.Chart("chartContainer", {
		title:{
			text: "Wydajność"
		},
		data: [
		{
			// Change type to "doughnut", "line", "splineArea", etc.
			type: "line",
			dataPoints: dataTasks
		}
		]
	});
	chart.render();
});

var btn2 = document.querySelector("#choose_whole")

btn2.addEventListener("click", function (){
    location.reload();
});

});
