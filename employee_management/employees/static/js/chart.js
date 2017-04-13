document.addEventListener("DOMContentLoaded", function(){
window.onload = function () {
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
			text: "Wydajność pracownika"
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
}

});