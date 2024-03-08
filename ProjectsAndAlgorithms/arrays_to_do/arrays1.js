//ush1: Push Front
// add the new element in the front of the table
function pushFront(arr, value) {
    for (let i = arr.length; i > 0; i--) {
        arr[i] = arr[i - 1];
    }
    arr[0] = value;
    return arr;
}

console.log(pushFront([5,7,2,3], 8));
console.log(pushFront([99], 7));  

// ush2: Pop Front
function popFront(arr) {
    const firstElement = arr[0];

    // Remove the first element from the array
    for (let i = 0; i < arr.length- 1; i++) {
        arr[i] = arr[i + 1];
    }

    arr.length--;

    console.log(firstElement + " returned, with [" + arr.join(',') + "] printed in the function");

    return firstElement;
}

console.log(popFront([0,5,10,15]));
console.log(popFront([4,5,7,9])); 

// ush3: Insert At
function insertAt(arr, index, value) {
    
    for (let i = arr.length; i > index; i--) {
        arr[i] = arr[i - 1];
    }
    
    arr[index] = value;
    
    return arr;
}

console.log(insertAt([100,200,5], 2, 311));
console.log(insertAt([9,33,7], 1, 42)); 

// # 3.Given an array, index, and additional value, insert the value into array at given index. You can think of pushFront(arr,val) as equivalent to insertAt(arr,0,val). You may use .push(), you are able do this without it though!
function insertAt(arr, index, value) {
    // Check if the index is out of bounds
    if (index < 0 || index > arr.length) {
        console.error("Index out of bounds");
        return;
    }

    // Shift elements to the right to make space for the new value
    for (let i = arr.length; i > index; i--) {
        arr[i] = arr[i - 1];
    }

    // Insert the new value at the specified index
    arr[index] = value;

    // Return the modified array
    return arr;
}

// Example usage:
let arr = [1, 2, 3, 4, 5];
let index = 2;
let value = 10;

console.log(insertAt(arr, index, value)); // Output: [1, 2, 10, 3, 4, 5]

// # 4.Given an array and an index into array, remove and return the array value at that index. Prove the value is removed from the array by printing it. Think of popFront(arr) as equivalent to removeAt(arr,0).
function removeAt(arr, index) {
    // Check if the index is out of bounds
    if (index < 0 || index >= arr.length) {
        console.error("Index out of bounds");
        return;
    }

    // Remove the value at the specified index and store it
    let removedValue = arr.splice(index, 1)[0];

    // Return the removed value
    return removedValue;
}

// Example usage:
let arrr = [1, 2, 3, 4, 5];
let indexRemove = 2;

let removedValue = removeAt(arrr, indexRemove);
console.log("Removed value:", removedValue); // Output: Removed value: 3
console.log("Array after removal:", arrr); // Use arrr instead of arr
   // Output: Array after removal: [1, 2, 4, 5]

//    # 5.Given a sorted array, remove duplicate values. Because array elements are already in order, all duplicate values will be grouped together. If you already made the Remove At function, you are welcome to use that! If you solved this using nested loops, for an extra challenge, try to do it without any nested loops!
function removeDuplicates(arr) {
    if (arr.length <= 1) {
        return arr; // If array has 0 or 1 element, it's already unique
    }

    let uniqueIndex = 0; // Index to track the position of unique elements
    
    // Iterate through the array
    for (let i = 1; i < arr.length; i++) {
        // If the current element is different from the previous one, move it to the next unique position
        if (arr[i] !== arr[uniqueIndex]) {
            uniqueIndex++;
            arr[uniqueIndex] = arr[i];
        }
    }

    // Remove the duplicate elements from the array
    arr.length = uniqueIndex + 1;

    return arr;
}

// Example usage:
let sortedArray = [1, 2, 2, 3, 4, 4, 4, 5, 5];
console.log("Original array:", sortedArray);
removeDuplicates(sortedArray);
console.log("Array after removing duplicates:", sortedArray);


