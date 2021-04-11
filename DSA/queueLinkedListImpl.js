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
            this.holdingPosition = this.first;
            this.first = newNode;
            this.first.next = this.holdingPosition
        }
        this.length++;
        return this;
    }
    dequeue(value) {
        if (!this.first) {
            return null;
        }
        const unwantedNode = this.first;
        this.first = this.first.next;
        this.length--;
        return this;

    }
    isEmpty() {}
}