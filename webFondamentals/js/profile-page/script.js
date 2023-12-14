console.log("page loaded...");


// function editName(newName) {
//     const userName = document.querySelector('.card-main h1');
//     userName.textContent = newName;
// }


// function removePerson(personi) {
//     document.getElementById(personi).remove()
//     var numriRequestave = parseInt(document.getElementById('requestNumbers').innerText)

//     document.getElementById('requestNumbers').innerText = numriRequestave - 1
// }


function removeUser(element){
var useriPare = document.getElementById("user1");
var useriDyte = document.getElementById("user2");

if(element){
    useriPare.remove();
}
else{
    useriDyte.remove();
}

    var nrRequests=parseInt(document.getElementById("request").innerText);
    nrRequests=nrRequests-1;
    document.getElementById("request").innerText = nrRequests;
}



function addRequests(){
    var nrRequests=parseInt(document.getElementById("request").innerText);
    nrRequests=nrRequests+1;
    document.getElementById("request").innerText = nrRequests;

}

// ndryshon emrin e userit te pare ne prof page

function changeUser(){
    var newUser= prompt("Shkruani emrin e ri te perdoruesit:");
    
    if(newUser===null){
        return;
    }

    var usernameElement= document.getElementById("username");
    if(usernameElement){
        usernameElement.textContent= newUser;
    }
    else{
        console.log("Elementi nuk u gjet!")
    }


}

// function addconectionRequest(){
//     var nrRequests=document.getElementById("request").innerText;
//     nrRequests=+1;
//     document.getElementById("request").innerText = nrRequests;
//     console.log(nrRequests);
    
// }