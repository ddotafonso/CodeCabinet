class DoublyLinkedList {
    constructor(value) {
        this.head = {
            value: value,
            next: null,
            prev: null
        }
        this.tail = this.head
        this.length = 1;
    }

    append(value) {
        const newNode = {
            value: value,
            next: null,
            prev: null
        };
        newNode.prev = this.tail;
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

    printList() {
        const array = [];
        let currentNode = this.head;
        while (currentNode !== null) {
            array.push(currentNode.value);
            currentNode = currentNode.next;
        }
        return array;

    }

    insert(index, value) {
        if (index >= this.length) {
            return this.append(value);
        }

        const newNode = {
            value: value,
            next: null
        };

        // X(leader) ---> X(holdingPosition)
        //     \        /
        //        X
        const leader = this.traverseToIndex(index - 1);
        const holdingPosition = leader.next;
        leader.next = newNode;
        newNode.next = holdingPosition;
        this.length++;
        return this.printList();
    }

    traverseToIndex(index) {
        //check params
        let counter = 0;
        let currentNode = this.head;
        while (counter !== index) {
            currentNode = currentNode.next;
            counter++;
        }
        return currentNode;
    }

    remove(index) {
        if (index > this.length) {
            return null;
        }

        const leader = this.traverseToIndex(index - 1);
        const unwantedNode = leader.next;
        leader.next = unwantedNode.next;
        this.length--;
        return this.printList();

    }

}

const myLinkedList = new DoublyLinkedList(790);
myLinkedList.append(5);
myLinkedList.append(16);
// myLinkedList.prepend(800);
myLinkedList.insert(2);
myLinkedList.printList()