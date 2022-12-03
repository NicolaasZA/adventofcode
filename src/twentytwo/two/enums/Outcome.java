package twentytwo.two.enums;

public enum Outcome {
    LOSS,
    DRAW,
    WIN;
    
    public static Outcome convertFromHandType(HandType type) {
        if (type == HandType.ROCK) {
            return Outcome.LOSS;
        } else if (type == HandType.PAPER) {
            return Outcome.DRAW;
        }
        return Outcome.WIN;
    }
}
