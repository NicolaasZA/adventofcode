export class Vector {
    x = 0;
    y = 0;

    text = '';

    constructor(x, y, text = '') {
        this.x = x;
        this.y = y;
        this.text = text;
    }

    calcFromMove(moveText) {
        this.text = "" + moveText;
        let pp = "" + moveText;
        const moveConstant = parseInt(pp.slice(2));
        if (pp.startsWith("U")) {
            this.x = 0;
            this.y = moveConstant;
        } else if (pp.startsWith("D")) {
            this.x = 0;
            this.y = 0 - moveConstant;
        } else if (pp.startsWith("L")) {
            this.x = 0 - moveConstant;
            this.y = 0;
        } else if (pp.startsWith("R")) {
            this.x = moveConstant;
            this.y = 0;
        }
    }

    asUnitVector() {
        let y = 0;
        let x = 0;

        if (this.y > 0) {
            y = 1;
        } else if (this.y < 0) {
            y = -1;
        }

        if (this.x > 0) {
            x = 1;
        } else if (this.x < 0) {
            x = -1;
        }

        return new Vector(x, y);
    }
}

export class Point extends Vector {

    constructor(x, y, text = '') {
        super(x, y, text);
    }

    wasAt(point) {
        if (!this.history) { return false; }
        return this.history.some((p) => p.x === point.x && p.y === point.y);
    }

    move(vector, track = false) {
        this.x += vector.x;
        this.y += vector.y;
        if (track) {
            const copy = new Point(this.x, this.y);
            this.addHistory(copy);
        }
    }

    addHistory(p) {
        if (!this.wasAt(p)) {
            if (!this.history) {
                this.history = [];
            }
            this.history.push(p);
        }
    }

    distanceTo(pointB) {
        // good old 'goras
        return Math.sqrt(Math.pow(pointB.x - this.x, 2) + Math.pow(pointB.y - this.y, 2))
    }

    calculateMove(targetPoint, exact = false) {
        // Determine which direction to move in to go nearer to target point
        if (this.distanceTo(targetPoint) > Math.sqrt(2) || exact) {
            // left/right
            if (targetPoint.y === this.y) {
                return new Vector(targetPoint.x < this.x ? -1 : 1, 0, this.text + '');
            }

            // up/down
            if (targetPoint.x === this.x) {
                return new Vector(0, targetPoint.y < this.y ? -1 : 1, this.text + '');
            }

            // diagonal
            return new Vector(targetPoint.x < this.x ? -1 : 1, targetPoint.y < this.y ? -1 : 1, this.text + '');
        } else {
            return null;
        }
    }
}