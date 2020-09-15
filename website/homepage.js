function post_data(){
    var age         = document.getElementById("age").value;
    var sex         = document.getElementById("sex").value;
    var cp          = document.getElementById("cp").value;
    var trestbps    = document.getElementById("trestbps").value;
    var chol        = document.getElementById("chol").value;
    var fbs         = document.getElementById("fbs").value;
    var restecg     = document.getElementById("restecg").value;
    var thalach     = document.getElementById("thalach").value;
    var exang       = document.getElementById("exang").value;
    var oldpeak     = document.getElementById("oldpeak").value;
    var slope       = document.getElementById("slope").value;
    var ca          = document.getElementById("ca").value;
    var thal        = document.getElementById("thal").value;
    var submit      = document.getElementById("submit").value;

    $.post('http://127.0.0.1:8000/predict/', 
    {
        age     : age     ,    
        sex     : sex     ,    
        cp      : cp      ,    
        trestbps: trestbps,    
        chol    : chol    ,    
        fbs     : fbs     ,    
        restecg : restecg ,    
        thalach : thalach ,    
        exang   : exang   ,    
        oldpeak : oldpeak ,    
        slope   : slope   ,    
        ca      : ca      ,    
        thal    : thal    ,    
        submit  : submit  ,    
    }, 
	function(data){
        console.log(data);
        document.getElementById("result").innerHTML="You have a " + data.result*100 + 
                                                    " percent chance of having a heart disease.";
        document.getElementById("result").style.visibility="visible";
        document.getElementById("result").style.height="50px";
	});
}