import { readFileSync } from 'fs';
import { Vector, Point } from './classes.mjs'; 

function movesFromFile(p) {
    const allFileContents = readFileSync(p, { encoding: 'utf-8' }).split("\n");

    let result = [];
    if (allFileContents && allFileContents.length) {
        result = allFileContents.map((line) => {
            const _ = new Vector(0,0);
            _.calcFromMove(line);
            return _;
        });
    }

    return result;
}


const head = new Point(0, 0);
const tail = new Point(0, 0);
const moves = movesFromFile("input.txt");

moves.forEach((moveVector) => {
    head.move(moveVector);

    let moveToPerform = tail.calculateMove(head);

    let iter = 0;
    while (moveToPerform != null) {
        tail.move(moveToPerform, true);
        moveToPerform = tail.calculateMove(head);
        iter += 1;
    }
})

console.log(tail.history.length) // 6243