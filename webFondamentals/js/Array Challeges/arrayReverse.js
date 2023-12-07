function reverse(arr) {
    var result=[];
    for(var i=arr.length-1;i>=0;i--){
        result.push(arr[i])

    }
    // your code here
    return result;
}
   
var result = reverse(["a", "b", "c", "d", "e"]);
console.log(result); // we expect back ["e", "d", "c", "b", "a"]
