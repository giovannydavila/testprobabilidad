async function predecir(x) {
    const sexo = document.getElementsByName("SEXO");
    const edad = document.getElementsByName("EDAD");
    const neumonia = document.getElementsByName("NEUMONIA");
    const diabetes = document.getElementsByName("DIABETES");
    const epoc = document.getElementsByName("EPOC");
    const asma = document.getElementsByName("ASMA");
    const inmusupr = document.getElementsByName("INMUSUPR");
    const hipertension = document.getElementsByName("HIPERTENSION");
    const cardiovascular = document.getElementsByName("CARDIOVASCULAR");
    const obesidad = document.getElementsByName("OBESIDAD");
    const renal_cronica = document.getElementsByName("RENAL_CRONICA");
    const tabaquismo= document.getElementsByName("TABAQUISMO");
    const covid = document.getElementsByName("COVID");
    const otra_com = document.getElementsByName("OTRA_COM");
    //const deceso = document.getElementsByName("DECESO");
        
    enviarDatosPost(
        getJson(
            sexo,
            edad,
            neumonia,
            diabetes,
            epoc,
            asma,
            inmusupr,
            hipertension,
            cardiovascular, 
            obesidad,
            renal_cronica,
            tabaquismo,
            covid,
            otra_com,
            //deceso,
            x
        )
        
    );
}

function Result(
    sexo,
    edad,
    neumonia,
    diabetes,
    epoc,
    asma,
    inmusupr,
    hipertension,
    cardiovascular, 
    obesidad,
    renal_cronica,
    tabaquismo,
    covid,
    otra_com,
    //deceso,
    x
    
) {
    this.sexo = sexo,
    this.edad = edad,
    this.neumonia = neumonia,
    this.diabetes = diabetes,
    this.epoc = epoc,
    this.asma = asma,
    this.inmusupr = inmusupr,
    this.hipertension = hipertension,
    this.cardiovascular = cardiovascular, 
    this.obesidad = obesidad,
    this.renal_cronica = renal_cronica,
    this.tabaquismo = tabaquismo,
    this.covid = covid,
    this.otra_com = otra_com,
    //this.deceso = deceso,
    this.x = x;
}

const getJson = (
    sexo,    
    edad,
    neumonia,
    diabetes,
    epoc,
    asma,
    inmusupr,
    hipertension,
    cardiovascular, 
    obesidad,
    renal_cronica,
    tabaquismo,
    covid,
    otra_com,
    // deceso,
    x
) => {
    const json = { result: [] };
    json.result.push(
        new Result(
            sexo[0].value,
            edad[0].value,
            neumonia[0].value,
            diabetes[0].value,
            epoc[0].value,
            asma[0].value,
            inmusupr[0].value,
            hipertension[0].value,
            cardiovascular[0].value, 
            obesidad[0].value,
            renal_cronica[0].value,
            tabaquismo[0].value,
            covid[0].value,
            otra_com[0].value,
            //deceso[0].value,
            x
        )
    );
    return json;
};


const enviarPost = (json) => {
    return {
        method: "POST", // or 'PUT'
        body: JSON.stringify(json), // data can be `string` or {object}!
        headers: {
            "Content-Type": "application/json",
        },
    };
};

const enviarDatosPost = (json) => {
    const url = `/machine-learning/${json.result[0].x}`;
    fetch(url, enviarPost(json))
        .then((response) => response.json())
        .catch((error) => alert(error))
        .then((response) => {
            tipoPrediccion(response, json);
        });
};

const isContain = (prediction,className) =>
    prediction.classList.contains(className);

const renameImages = (modifyName,img) =>{    
    const point = img.lastIndexOf(".")
    const sub = img.slice(0,point)
    return `${sub + modifyName}.png`        
}
const presentImage = (modifyName) =>
    [...document.querySelectorAll(".analisis")].map((img) =>
        img.src = `static/webapp/img/${renameImages(modifyName,img.alt)}?v=${new Date().getTime()}/`
    );
const initPrediction = (json) => {
    let title = "Método: ";
    let titleModal = document.querySelector(".modal-title");
    let prediction = document.querySelector("#arbol");
    if (json.result[0].x == 1) {        
        if (!isContain(prediction, "invisible"))
            prediction.classList.add("invisible");
        titleModal.innerHTML = `${title} Naive Bayes`;
        presentImage("1");
    } else {
        if (isContain(prediction,"invisible"))
            prediction.classList.remove("invisible");
        titleModal.innerHTML = `${title} Árbol de Decisión`;
        presentImage("2");
    }
};
const diagnostic = (responseText, json) => {
    let text =
        "Aplicando el método METODO CAMBIAR se obtiene la siguiente predicción: El paciente presenta";
    const inlineReplace = (metodo) =>
        text.replace("METODO CAMBIAR", `<b>${metodo}</b>`);
    text =
        json.result[0].x == 1
            ? inlineReplace("Naive Bayes")
            : inlineReplace("Árbol de Decisión");            
    let recomendacion = document.querySelectorAll(".score1");
    if (responseText.result == "1"){//score
        recomendacion[0].innerHTML = `${text} <b>alto riesgo</b> de fallecer. <b>Necesita atención urgente</b>`;
        recomendacion[1].innerHTML = `Este método tiene una precisión del ${responseText.score}%`
    }
        
    else{
        recomendacion[0].innerHTML = `${text} <b>bajo riesgo</b> de fallecer. <b>Necesita de cuidados</b>`;    
        recomendacion[1].innerHTML = `Este método tiene una precisión del ${responseText.score}%`
    }
        
};

const tipoPrediccion = (responseText, json) => {
    let opacity = document.querySelector(".container-fluid");
    if(isContain(opacity,"opa"))
        opacity.classList.remove("opa");    
    initPrediction(json);
    diagnostic(responseText, json);
};

const form = () => {
    const form = document.querySelector("#naiveBayes");
    form.addEventListener("submit", validar);
};

const conditionButton = (condition) =>
    condition === false ? "btn btn-primary" : "btn btn-secondary";

const botones = (condition) =>
    [...document.getElementsByName("botoncito[]")].map((button) => {
        button.disabled = condition;
        button.className = conditionButton(condition);
    });
const addMachineLearning = () => {
    const a = document.getElementById("id_EDAD");
    a.addEventListener("change", () => {
        if (a.value != "") botones(false);
        else botones(true);
    });
};