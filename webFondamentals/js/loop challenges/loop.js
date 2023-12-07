//1. print odds 1-20
for(var i=1;i<=20;i++){
    if(i%2!=0){
        console.log(i);
    }
}
// 2.decreasing multiples of 3
for(var a=100;a>=0;a-=3){
    console.log(a);
}
//3. print the sequence
for(var b=4;b>=-3.5;b-=1.5){
    console.log(b);
}
// 4.sigma
var sum=0;
for(var value=1;value<=100;value++){
    sum+=value;
}
console.log(sum);

// 5.factorial
var product=1;
for(var multiply=1;multiply<=12;multiply++){
    product*=multiply;
}
console.log(product);