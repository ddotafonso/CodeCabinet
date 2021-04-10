class Node {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}

class Stack {
    constructor() {
        this.top = null;
        this.bottom = null;
        this.length = 0;

    }

    peek() {
        this.top = this.length - 1;
        this.value = this.top
    }

    push(value) {
        newNode
    }
    pop() {}
    isEmpty() {
        return this.length == 0;
    }
}