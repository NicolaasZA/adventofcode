import { Sequence } from './classes.mjs';
import { readFileSync } from 'fs';


function readInstructions(p) {
    const allFileContents = readFileSync(p, { encoding: 'utf-8' }).split("\n");
    return (allFileContents && allFileContents.length) ? allFileContents : [];
}

const instructions = readInstructions("./input.txt");
const sequence = new Sequence(instructions);

const crt = [
    '                                        '.split(""),
    '                                        '.split(""),
    '                                        '.split(""),
    '                                        '.split(""),
    '                                        '.split(""),
    '                                        '.split("")
];

for (let i = 0; i < 240; i++) {
    const row = Math.floor(i / 40);
    const col = i % 40;
    const spriteX = sequence.valueAt(i + 1).start;

    crt[row][col] = [spriteX - 1, spriteX, spriteX + 1].includes(col) ? '#' : ' ';
}

for (const row of crt) {
    console.log(row.join(""));
}