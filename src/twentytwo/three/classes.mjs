export class Item {
    key;
    priority;

    constructor(key) {
        this.key = key;
        this.priority = this.calculatePriority(key);
    }

    calculatePriority(key) {
        return "0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".indexOf(key);
    }
}

export class Bag {
    compartmentA = []; // List[Item]
    compartmentB = []; // List[Item]

    sharedItem; // Item

    constructor(contents) {
        if (contents) {
            this.compartmentA = contents.substring(0, contents.length / 2).split("").map((key) => new Item(key));
            this.compartmentB = contents.substring(contents.length / 2).split("").map((key) => new Item(key));

            this.sharedItem = this.findSharedItem();
        }
    }

    findSharedItem() {
        for (let i = 0; i < this.compartmentA.length; i++) {
            const a = this.compartmentA[i];
            if (this.compartmentB.some((b) => b.priority == a.priority)) {
                return a;
            }
        }
        return new Item('0');
    }

    getItems() {
        let x = [];
        return x
            .concat(JSON.parse(JSON.stringify(this.compartmentA)))
            .concat(JSON.parse(JSON.stringify(this.compartmentB)));
    }
}

export class BagGroup {
    bagA; // Bag
    bagB; // Bag
    bagC; // Bag

    sharedItem; // Item

    constructor(a, b, c) {
        this.bagA = a;
        this.bagB = b;
        this.bagC = c;

        this.sharedItem = this.findSharedItem();
    }

    findSharedItem() {
        let shared = new Item('0');

        const aContents = this.bagA.getItems();
        const bContents = this.bagB.getItems();
        const cContents = this.bagC.getItems();

        for (let i = 0; i < aContents.length; i++) {
            const a = aContents[i];

            const isInBagB = bContents.some((b) => b.priority == a.priority);
            const isInBagC = cContents.some((c) => c.priority == a.priority);
            if (isInBagB && isInBagC) {
                return a;
            }
        };
        return shared;
    }
}