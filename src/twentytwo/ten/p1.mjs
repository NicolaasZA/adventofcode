import { Sequence } from './classes.mjs';
import { readFileSync } from 'fs';


function readInstructions(p) {
    const allFileContents = readFileSync(p, { encoding: 'utf-8' }).split("\n");
    let result = [];
    if (allFileContents && allFileContents.length) {
        result = allFileContents.map((line) => line.replace("\n", ""));
    }
    return result;
}

const instructions = readInstructions("./input.txt");
const sequence = new Sequence(instructions);

let sum = 0;
for (const c of [20,60,100,140,180,220]) {
    sum += (c * sequence.valueAt(c).start);
}
console.log(sum);