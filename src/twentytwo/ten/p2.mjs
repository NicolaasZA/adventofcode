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

const crt = [
    '########################################'.split(""),
    '########################################'.split(""),
    '########################################'.split(""),
    '########################################'.split(""),
    '########################################'.split(""),
    '########################################'.split("")
];

for (let i = 0; i < 240; i ++) {
    const index = i % 240;
    const row = Math.floor(index / 40);
    const col = index % 40;

    const spriteX = sequence.valueAt(i+1).start;
    const pixel = [spriteX-1, spriteX, spriteX+1].includes(col) ? '#' : '.';

    crt[row][col] = pixel;
}

for (const row of crt) {
    console.log(row.join(""));
}