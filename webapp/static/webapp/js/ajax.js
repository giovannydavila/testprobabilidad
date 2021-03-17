const initParams = () => {
	return {
		method: "get",
		headers: new Headers(),
		mode: "cors",
		cache: "default"
	}
};

const request = (id = 0) => {
	const base = "/home";
	const url = [`${base}/inicio`, `${base}/machine_learning`, `${base}/arbol_decision`];

	return new Request(url[id], initParams());
}

const pestanasTodas = (id = 0) => {
	fetch(request(id))
		.then((response) => response.text())
		.then((response) => {
			document.getElementById("pestanas").innerHTML = response;
			machineLearning(id);
		});

}
const loading = () =>	
	[...document.getElementsByClassName("spin")].map((element)=>{
		element.innerHTML = `
		<div class="spinner-border">
		  <span class="visually-hidden"></span>
		</div>
		`;
	});
function machineLearning(id) {
	if (id == 1) {		
		const myModalEl = document.getElementById("staticBackdrop");
		myModalEl.addEventListener('show.bs.modal', (e) =>loading());
		myModalEl.addEventListener("hide.bs.modal",(e) =>{
			let opacity = document.querySelector(".container-fluid");
			if(!opacity.classList.contains("opa"))
				opacity.classList.add("opa");    		
		});
		addMachineLearning();
	}

}
// pestanasTodas();
addMachineLearning()  