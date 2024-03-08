// Create display() that uses a while loop and a runner to return a string containing all list values. Build what you wish console.log(myList) did!
class Node {
    constructor(data) {
        this.data = data;
        this.next = null;
    }
}

class SLL {
    constructor() {
        this.head = null;
    }
    
    addFront(value) {
        let newNode = new Node(value);
        newNode.next = this.head;
        this.head = newNode;
        return this.head;
    }

    removeFront() {
        if (!this.head) {
            return null; // List is empty
        }
        let removedNode = this.head;
        this.head = this.head.next;
        removedNode.next = null;
        return this.head;
    }

    front() {
        return this.head ? this.head.data : null;
    }

    display() {
        let current = this.head;
        let result = '';
        while (current) {
            result += current.data;
            if (current.next) {
                result += ', ';
            }
            current = current.next;
        }
        return result;
    }
}

// Example usage:
let SLL1 = new SLL();
SLL1.addFront(76);
SLL1.addFront(2);
console.log(SLL1.display());  // Output: "2, 76"
SLL1.addFront(11.41);
console.log(SLL1.display());  // Output: "11.41, 2, 76"