<!DOCTYPE html>
<html>
<script>
function myFunction() {

  let b = document.getElementById("bench").value;

  let text;
  if (isNaN(b) || b < 1 || b > 1000) {
    text = "Bench Input not valid";}
  document.getElementById("ben").innerHTML = text;

  let s = document.getElementById("squat").value;

  let text;
  if (isNaN(s) || s < 1 || s > 1000) {
    text = "Squat Input not valid";}
  document.getElementById("squa").innerHTML = text;


  let d = document.getElementById("deadlift").value;

  let text;
  if (isNaN(d) || d < 1 || d > 1000) {
    text = "Deadlift Input not valid";}
  document.getElementById("dead").innerHTML = text;
}
</script>
<body style="background-color:orange;">

<h1>Power Lifting Club</h1>
<h2>2023 - 2024 interest form</h2>
<img src= "https://vtlogo.com/wp-content/uploads/2021/05/greenwich-country-day-school-vector-logo-small.png" alt="Trulli" width="500" height="333">
<form name = "MyForm" >action="thanks.html" method="get"
  <label for="fname">First name:</label><br>
  <input type="text" id="fname" name="fname"><br>
  <label for="lname">Last name:</label><br>
  <input type="text" id="lname" name="lname"><br>


<p> Enter Your Grade:</p>

  <input type="radio" id="ninth" name="fav_language" value="ninth">
  <label for="ninth">9th</label><br>
  <input type="radio" id="tenth" name="fav_language" value="tenth">
  <label for="tenth">10th</label><br>
  <input type="radio" id="eleventh" name="fav_language" value="eleventh">
  <label for="eleventh">11th</label><br>
  <input type="radio" id="twelth" name="fav_language" value="twelth">
  <label for="twelth">12th</label><br>


<p> Enter Seasons available:</p>

  <input type="checkbox" id="fall" name="fall" value="fall">
  <label for="fall"> Fall</label><br>
  <input type="checkbox" id="winter" name="winter" value="winter">
  <label for="winter"> Winter</label><br>
  <input type="checkbox" id="spring" name="spring" value="spring">
  <label for="spring"> Spring</label>


<p> Enter Your What You Lift(lbs):</p>

  <label for="bench">Bench:</label><br>


  <input type="text" id="bench" name="bench"><br>
  <label for="squat">Squat:</label><br>
  <input type="text" id="squat" name="squat"><br>
  <label for="deadlift">Deadlift:</label><br>
  <input type="text" id="deadlift" name="deadlift"><br>
  <input type="submit" value="Submit" onclick="myFunction()">
<p id="ben"></p>
<p id="squa"></p>
<p id="dead"></p>
</form>


</body>
</html>

    main()