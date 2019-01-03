

function run_get_output(){
	var source_code = document.getElementById("source_code").value;
	var csrf_token = Cookies.get("csrftoken");
	fetch("http://localhost:8000/api/get_output/",{
		method: "POST",
		headers: {
			"Content-Type":"application/json",
			"X-CSRFToken":csrf_token
		},
		body: JSON.stringify({"source_code":source_code})
	}).then(function(res){
		return res.json();
	}).then(function(data){
		document.getElementById("output").value = data.output;
	})
}

document.getElementById("run").onclick = run_get_output;