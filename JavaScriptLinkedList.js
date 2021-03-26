class LinkedList {
    constructor(value) {
        this.head = {
            value: value,
            next: null
        }
        this.tail = this.head
        this.length = 1;
    }

    append(value) {
        const newNode = {
            value: value,
            next: null
        };
        this.tail.next = newNode;
        this.tail = newNode;
        this.length++;
        return this;
    }

    prepend(value) {
        const firstNode = {
            value: value,
            next: null
        };
        firstNode.next = this.head;
        this.head = firstNode;
        this.length++;
        return this;
    }

}

const myLinkedList = new LinkedList(590);
myLinkedList.append(5);
myLinkedList.append(16);
// myLinkedList.prepend(800);
console.log(myLinkedList)