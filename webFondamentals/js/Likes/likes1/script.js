var like=3;
var likeElement = document.querySelector("#like");

function addLikes(){
    like++;
    likeElement.innerText = like + "like(s)"
}