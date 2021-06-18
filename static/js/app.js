console.log("app.js connected");


function buttonClick() {
  d3.text('/magic').then (function(d){
    // console.log(d)
    document.getElementById("prediction").textContent = ('Our Random Forest Model Predicts the Income to be: '  + d)
  });
}

function clearButton() {
  var pTag = (document.getElementById('prediction').innerHTML = '');
}


