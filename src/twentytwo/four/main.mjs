import { readFileSync } from "fs";

class Pair {
    startOne = 0;
    endOne = 0;
    startTwo = 0;
    endTwo = 0;

    constructor(line) {
        const pieces = line.split(',');
        const one = pieces[0].split('-');
        const two = pieces[1].split('-');

        this.startOne = parseInt(one[0], 10);
        this.endOne = parseInt(one[1], 10);
        this.startTwo = parseInt(two[0], 10);
        this.endTwo = parseInt(two[1], 10);
    }

    hasFullOverlap() {
        if ((this.startOne >= this.startTwo) && (this.endOne <= this.endTwo)) {
            return true;
        }

        if ((this.startTwo >= this.startOne) && (this.endTwo <= this.endOne)) {
            return true;
        }

        return false;

    }

    hasAnyOverlap() {
        if ((this.startOne <= this.startTwo) && (this.endOne >= this.startTwo)) {
            return true;
        }

        if ((this.startTwo <= this.startOne) && (this.endTwo >= this.startOne)) {
            return true;
        }

        return false;
    }
}

function pairsFromFile(p) {
    const allFileContents = readFileSync(p, { encoding: 'utf-8' }).split("\n");

    let result = [];
    if (allFileContents && allFileContents.length) {
        result = allFileContents.map((line) => new Pair(line));
    }

    return result;
}

function partOne() {
    const pairs = pairsFromFile("./input.txt");

    const hasOverlaps = pairs.map((p) => p.hasFullOverlap()).filter((o) => o);

    console.log(hasOverlaps.length); // 530
}

function partTwo() {
    const pairs = pairsFromFile("./input.txt");

    const hasOverlaps = pairs.map((p) => p.hasAnyOverlap()).filter((o) => o == true);

    console.log(hasOverlaps.length); // 903
    
}

partOne();
partTwo();