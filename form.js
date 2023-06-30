let button=document.getElementById('sb')
button.onclick=button1
function button1(){
let eng=parseInt(document.getElementById('em').value);
let hin=parseInt(document.getElementById('hm').value);
let mat=parseInt(document.getElementById('mm').value);
let comp=parseInt(document.getElementById('csm').value);
let stats=parseInt(document.getElementById('sm').value);
let phy=parseInt(document.getElementById('pm').value);
let total= eng+hin+mat+comp+stats+phy;
document.write("Total : "+total +"<br>");
let percent=(eng+hin+mat+comp+stats+phy)/6;
document.write("Percentage : " )
document.write(percent + "<br>");
if(percent>=85){
	document.write("Grade : A  <br> Result : Passed <br>");
}
else
if((percent>=70)&&(percent<85)){
	document.write("Grade : B  <br> Result : Passed <br>");
}
else
if((percent>=60)&&(percent<70)){
	document.write("Grade : C  <br> Result : Passed <br>");
}
else
if((percent>=45)&&(percent<60)){
	document.write("Grade : D <br> Result : Passed")
}
else
{
	document.write("Result : Fail <br>")
}
}







