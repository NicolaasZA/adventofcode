package twentytwo.two;

import twentytwo.two.enums.HandType;
import twentytwo.two.enums.Outcome;

public class Hand {

    private final HandType type;

    public Hand(HandType type) {
        this.type = type;
    }

    /**
     * Convert a character representation of a hand to Hand.
     */
    public static Hand fromInput(String value) {
        return switch (value) {
            case "A", "X" -> new Hand(HandType.ROCK);
            case "B", "Y" -> new Hand(HandType.PAPER);
            case "C", "Z" -> new Hand(HandType.SCISSORS);
            default -> null;
        };
    }

    /**
     * When given an opponent's hand, returns the hand that will lose to it.
     */
    public static Hand willLoseTo(Hand opponentHand) {
        if (opponentHand.getType() == HandType.ROCK) {
            return new Hand(HandType.SCISSORS);
        } else if (opponentHand.getType() == HandType.PAPER) {
            return new Hand(HandType.ROCK);
        }
        return new Hand(HandType.PAPER);
    }

    /**
     * When given an opponent's hand, returns the hand that will win against it.
     */
    public static Hand willWinAgainst(Hand opponentHand) {
        if (opponentHand.getType() == HandType.ROCK) {
            return new Hand(HandType.PAPER);
        } else if (opponentHand.getType() == HandType.PAPER) {
            return new Hand(HandType.SCISSORS);
        }
        return new Hand(HandType.ROCK);
    }

    /**
     * When given an opponent's hand and a desired outcome, returns the hand that will give that outcome.
     */
    public static Hand fromOutcome(Outcome outcome, Hand opponentHand) {
        if (outcome == Outcome.LOSS) {
            return Hand.willLoseTo(opponentHand);
        } else if (outcome == Outcome.WIN) {
            return Hand.willWinAgainst(opponentHand);
        }
        return new Hand(opponentHand.getType());
    }

    public HandType getType() {
        return type;
    }

    public Outcome getOutcome(Hand opponent) {
        if (this.type == Hand.willWinAgainst(opponent).getType()) {
            return Outcome.WIN;
        } else if (this.type == Hand.willLoseTo(opponent).getType()) {
            return Outcome.LOSS;
        }
        return Outcome.DRAW;
    }

    @Override
    public String toString() {
        return this.getType().toString();
    }
}
