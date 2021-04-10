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
        // this.top = this.length - 1;
        // this.value = this.top
        return this.top;
    }

    push(value) {
        this.value = this.top
        this.length++;
    }
    pop() {}
    isEmpty() {
        return this.length == 0;
    }
}