export class Sequence {

    // 1-based
    cycles = [
        { start: 1, end: 1 }
    ];

    constructor(operations) {
        if (operations && operations.length) {
            this.build(operations);
        }
    }

    build(operations) {
        // Convert instructions to cycle data
        this.cycles = [ { start: 1, end: 1 } ];
        if (operations && operations.length) {
            operations.forEach(iText => {
                const currentValue = this.cycles[this.cycles.length - 1].end + 0;
                if (iText.startsWith("noop")) {
                    // For one cycle, the value of X remains same
                    this.cycles.push({ start: currentValue, end: currentValue });
                } else if (iText.startsWith("addx")) {
                    // For one cycle remain same, next cycle end with new value
                    const modValue = parseInt(iText.replace("addx ", ""), 10);
                    this.cycles.push({ start: currentValue, end: currentValue});
                    this.cycles.push({ start: currentValue, end: currentValue + modValue});
                }
            });
        }
    }

    valueAt(cycle) {
        if (!cycle || cycle < 0) { this.cycles[0]; }

        if (cycle >= this.cycles.length) { 
            return this.cycles[this.cycles.length-1];
        }

        return this.cycles[cycle];
    }
}