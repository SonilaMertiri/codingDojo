var x= document.getElementById('myVideo')

function playVideo() {
    x.play('myVideo')

}

function pauseVideo() {
    x.pause('myVideo')
}

function muteVideo(){
    x.muted=true;
}


console.log("page loaded...");