import { readFileSync } from 'fs';
import { Vector, Point } from './classes.mjs';

class PointChain {

    exact = false;

    constructor(p, n = null) {
        this.point = p;
        this.next = n;
    }

    setExact(val) {
        this.exact = val ? true : false;
    }

    moveTowards(target) {
        if (this.exact) {
            this.point.x = target.x;
            this.point.y = target.y;

            if (!this.point.history) {
                this.point.history = [];
            }
            this.point.addHistory(new Point(this.point.x, this.point.y));

            if (this.next) {
                this.next.moveTowards(this.point);
            }
        } else {
            let move = this.point.calculateMove(target);
            while (move) {
                this.point.move(move, true);

                if (this.next) {
                    this.next.moveTowards(this.point);
                }

                move = this.point.calculateMove(target);
            }
        }
    }
}

function movesFromFile(p) {
    const allFileContents = readFileSync(p, { encoding: 'utf-8' }).split("\n");

    let result = [];
    if (allFileContents && allFileContents.length) {
        result = allFileContents.map((line) => {
            const _ = new Vector(0, 0);
            _.calcFromMove(line);
            return _;
        });
    }

    return result;
}

const tail = new PointChain(new Point(0, 0, 'T'), null);
const eight = new PointChain(new Point(0, 0, '8'), tail);
const seven = new PointChain(new Point(0, 0, '7'), eight);
const six = new PointChain(new Point(0, 0, '6'), seven);
const five = new PointChain(new Point(0, 0, '5'), six);
const four = new PointChain(new Point(0, 0, '4'), five);
const three = new PointChain(new Point(0, 0, '3'), four);
const two = new PointChain(new Point(0, 0, '2'), three);
const one = new PointChain(new Point(0, 0, '1'), two);
const head = new PointChain(new Point(0, 0, 'H'), one);
head.setExact(true);

const moves = movesFromFile("input.txt");
const target = new Point(0, 0);

moves.forEach((moveVector) => {
    target.x += moveVector.x;
    target.y += moveVector.y;

    head.moveTowards(target);
});

[tail, eight, seven, six, five, four, three, two, one, head].forEach((_) => console.log(_.point.text, _.point.history ? _.point.history.length + 1 : 1));
