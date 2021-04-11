class Stack {
    constructor() {
        this.array = [];

    }

    peek() {
        return this.array[this.array.length - 1];
    }

    push(value) {
        this.array.push(value);
    }
    pop() {
        this.array.pop();
        return this;
    }
    isEmpty() {
        return this.length == 0;
    }
}


const myStack = new Stack();
myStack.push('Angola');
myStack.push('Congo');
myStack.push('Zambia');
myStack.pop();
myStack.pop();
myStack.pop();