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
        // this.value = this.top
        // this.length++;
        const newNode = new Node(value)
            // If stack is empty and this is the very new item, top and bottom will be the same item.
        if (this.length === 0) {
            this.top = newNode;
            this.bottom = newNode;
        } else {
            const holdingPointer = this.top;
            this.top = newNode;
            this.top.next = holdingPointer;
        }
        this.length++;
        return this;
    }
    pop() {
        if (!this.top) {
            return null;
        }
        // Javascript being a garbage collector language, it automatically deletes unwantedNode var since it's not being used.
        const unwantedNode = this.top;
        this.top = this.top.next;
        this.length--;
        return this;
    }
    isEmpty() {
        return this.length == 0;
    }
}


const myStack = new Stack();
myStack.push('google');
myStack.push('instagram');
myStack.push('twitter');
myStack.push('facebook');