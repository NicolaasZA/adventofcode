package twentytwo.two.enums;

public enum HandType {
    ROCK,
    PAPER,
    SCISSORS;

    public static Outcome asOutcome(HandType type) {
        if (type == HandType.ROCK) {
            return Outcome.LOSS;
        } else if (type == HandType.PAPER) {
            return Outcome.DRAW;
        }
        return Outcome.WIN;
    }
}
