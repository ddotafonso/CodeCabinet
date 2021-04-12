class Node {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}

class Queue {
    constructor(value) {
        this.first = value;
        this.last = null;
        this.length = 0;
    }

    peek() {
        return this.first;
    }
    enqueue(value) {
        const newNode = new Node();
        if (length === 0) {
            this.first = newNode;
            this.last = newNode;
        } else {
            // this.holdingPosition = this.first;  We could include the line 24 if we want to save the variable.
            this.last.next = newNode;
            this.last = newNode;
        }
        this.length++;
        return this;
    }
    dequeue(value) {
        if (!this.first) {
            return null;
        }
        if (this.first === this.last) {
            this.last = null;
        }
        this.first = this.first.next;
        this.length--;
        return this;
    }
    isEmpty() {
        return this.length === 0;
    }
}