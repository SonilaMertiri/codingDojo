var numberOfLikes = [9, 12, 9];

function addLikes(id) {
  if (id === "post1") {
    numberOfLikes[0] += 1;
    document.querySelector("#post1").innerText = numberOfLikes[0] + " like(s)";
  } else if (id === "post2") {
    numberOfLikes[1] += 1;
    document.querySelector("#post2").innerText = numberOfLikes[1] + " like(s)";
  } else {
    numberOfLikes[2] += 1;
    document.querySelector("#post3").innerText = numberOfLikes[2] + " like(s)";
  }
}








// function addLikes(idPost){
//     var nrLikeve= parseInt(document.getElementById(idPost).innerText)
//     document.getElementById(idPost).innerText= nrLikeve+1 +" like(s)"
// }







// kjo me numeron ne klik te cdo posti me nga 1

// var numberOfLikes=[9,12,9];
// var post=[document.querySelector("#post1"), document.querySelector("#post2"), document.querySelector("#post3")];

// function addLikes(){
//     for(var i=0;i<post.length; i++){
//         numberOfLikes[i]++;
//         post[i].innerText= numberOfLikes[i] +"like"
//     }
// }






// kjo i ben add cdo posti numrin qe i eshte shtuar postit pararendes

// var numberOfLikes=[9,12,9];

// function addLikes(id){
//     for(var i=0;i<numberOfLikes.length;i++){
//         numberOfLikes[i]= numberOfLikes[i]+1;
//         if(id==='post1'){
//             document.querySelector("#post1").innerText= numberOfLikes[i] +" like(s)";
//         }
//         else if(id==='post2'){
//             document.querySelector("#post2").innerText= numberOfLikes[i] +" like(s)";
//         }
//         else{
//             document.querySelector("#post3").innerText= numberOfLikes[i] +" like(s)";
//         }
//     }
//     }
