// 1.Write a method that accepts a value and create a new node, assign it to the list head, and return a pointer to the new head node.
// Define the Node class
class Node {
    constructor(data) {
        this.data = data;
        this.next = null;
    }
}

// Define the SLL class
class SLL {
    constructor() {
        this.head = null;
    }
    
    // Method to add a new node at the front of the list
    addFront(value) {
        let newNode = new Node(value);
        newNode.next = this.head;
        this.head = newNode;
        return this.head;
    }

    // Method to remove the head node from the list
    removeFront() {
        if (!this.head) {
            return null; // List is empty
        }
        let removedNode = this.head;
        this.head = this.head.next;
        removedNode.next = null;
        return this.head;
    }

    // Method to return the value at the head of the list
    front() {
        return this.head ? this.head.data : null;
    }
}

// Example usage:

let SLL1 = new SLL();
console.log(SLL1.addFront(18));  // Output: Node { data: 18, next: null }
console.log(SLL1.addFront(5));   // Output: Node { data: 5, next: Node { data: 18, next: null } }
console.log(SLL1.addFront(73));  // Output: Node { data: 73, next: Node { data: 5, next: Node { data: 18, next: null } } }

SLL1 = new SLL(); // Reinitialize SLL1 for the next example

SLL1.addFront(18);
SLL1.addFront(5);
console.log(SLL1.removeFront());  // Output: Node { data: 5, next: Node { data: 18, next: null } }
console.log(SLL1.removeFront());  // Output: Node { data: 18, next: null }
console.log(SLL1.removeFront());  // Output: null (empty list)

SLL1 = new SLL(); // Reinitialize SLL1 for the next example

SLL1.addFront(18);
console.log(SLL1.front());         // Output: 18
console.log(SLL1.removeFront());   // Output: null
console.log(SLL1.front());         // Output: null
