import { readFileSync } from "fs";
import { Bag, BagGroup } from "./classes.mjs";

function bagsFromFile(p) {
    const allFileContents = readFileSync(p, { encoding: 'utf-8' }).split("\n");

    let result = [];
    if (allFileContents && allFileContents.length) {
        result = allFileContents.map((contents) => new Bag(contents));
    }
    return result;
}

function partOne() {
    const bags = bagsFromFile('./input.txt');
    
    let score = 0;
    bags.forEach((b) => {
        score += b.sharedItem.priority;
    });

    console.log("part 1", score); // 8240
}

function partTwo() {
    const bags = bagsFromFile('./input.txt');
    
    const groups = [];
    for (let i = 0; i < bags.length; i += 3) {
        groups.push(new BagGroup(bags[i], bags[i + 1], bags[i + 2]));
    }
    
    let score = 0;
    groups.forEach((b) => {
        score += b.sharedItem.priority;
    });

    console.log("part 2", score); // 2587
}

partOne();
partTwo();