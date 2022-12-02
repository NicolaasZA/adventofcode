package twentytwo.two.tests;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import twentytwo.two.Hand;
import twentytwo.two.enums.HandType;
import twentytwo.two.enums.Outcome;

import static org.junit.jupiter.api.Assertions.assertAll;
import static org.junit.jupiter.api.Assertions.assertEquals;

class HandTest {

    @Test
    @DisplayName("Testing fromInput")
    void test_fromInput() {
        assertAll(
                () -> assertEquals(HandType.ROCK, Hand.fromInput("A").getType()),
                () -> assertEquals(HandType.PAPER, Hand.fromInput("B").getType()),
                () -> assertEquals(HandType.SCISSORS, Hand.fromInput("C").getType()),

                () -> assertEquals(HandType.ROCK, Hand.fromInput("X").getType()),
                () -> assertEquals(HandType.PAPER, Hand.fromInput("Y").getType()),
                () -> assertEquals(HandType.SCISSORS, Hand.fromInput("Z").getType())
        );
    }

    @Test
    @DisplayName("Testing willLoseTo")
    void test_willLoseTo() {
        Hand rock = new Hand(HandType.ROCK);
        Hand paper = new Hand(HandType.PAPER);
        Hand scissors = new Hand(HandType.SCISSORS);

        assertAll(
                () -> assertEquals(HandType.SCISSORS, Hand.willLoseTo(rock).getType()),
                () -> assertEquals(HandType.ROCK, Hand.willLoseTo(paper).getType()),
                () -> assertEquals(HandType.PAPER, Hand.willLoseTo(scissors).getType())
        );
    }

    @Test
    @DisplayName("Testing willWinAgainst")
    void test_willWinAgainst() {
        Hand rock = new Hand(HandType.ROCK);
        Hand paper = new Hand(HandType.PAPER);
        Hand scissors = new Hand(HandType.SCISSORS);

        assertAll(
                () -> assertEquals(HandType.PAPER, Hand.willWinAgainst(rock).getType()),
                () -> assertEquals(HandType.SCISSORS, Hand.willWinAgainst(paper).getType()),
                () -> assertEquals(HandType.ROCK, Hand.willWinAgainst(scissors).getType())
        );
    }

    @Test
    @DisplayName("Testing fromOutcome")
    void test_fromOutcome() {
        assertAll(
                () -> assertEquals(HandType.SCISSORS, Hand.fromOutcome(Outcome.LOSS, new Hand(HandType.ROCK)).getType()),
                () -> assertEquals(HandType.ROCK, Hand.fromOutcome(Outcome.DRAW, new Hand(HandType.ROCK)).getType()),
                () -> assertEquals(HandType.PAPER, Hand.fromOutcome(Outcome.WIN, new Hand(HandType.ROCK)).getType()),

                () -> assertEquals(HandType.ROCK, Hand.fromOutcome(Outcome.LOSS, new Hand(HandType.PAPER)).getType()),
                () -> assertEquals(HandType.PAPER, Hand.fromOutcome(Outcome.DRAW, new Hand(HandType.PAPER)).getType()),
                () -> assertEquals(HandType.SCISSORS, Hand.fromOutcome(Outcome.WIN, new Hand(HandType.PAPER)).getType()),

                () -> assertEquals(HandType.PAPER, Hand.fromOutcome(Outcome.LOSS, new Hand(HandType.SCISSORS)).getType()),
                () -> assertEquals(HandType.SCISSORS, Hand.fromOutcome(Outcome.DRAW, new Hand(HandType.SCISSORS)).getType()),
                () -> assertEquals(HandType.ROCK, Hand.fromOutcome(Outcome.WIN, new Hand(HandType.SCISSORS)).getType())
        );
    }

    @Test
    @DisplayName("Testing getOutcome")
    void getOutcome() {
        Hand rock = new Hand(HandType.ROCK);
        Hand paper = new Hand(HandType.PAPER);
        Hand scissors = new Hand(HandType.SCISSORS);

        assertAll(
                () -> assertEquals(Outcome.LOSS, rock.getOutcome(new Hand(HandType.PAPER))),
                () -> assertEquals(Outcome.DRAW, rock.getOutcome(new Hand(HandType.ROCK))),
                () -> assertEquals(Outcome.WIN, rock.getOutcome(new Hand(HandType.SCISSORS))),

                () -> assertEquals(Outcome.LOSS, paper.getOutcome(new Hand(HandType.SCISSORS))),
                () -> assertEquals(Outcome.DRAW, paper.getOutcome(new Hand(HandType.PAPER))),
                () -> assertEquals(Outcome.WIN, paper.getOutcome(new Hand(HandType.ROCK))),

                () -> assertEquals(Outcome.LOSS, scissors.getOutcome(new Hand(HandType.ROCK))),
                () -> assertEquals(Outcome.DRAW, scissors.getOutcome(new Hand(HandType.SCISSORS))),
                () -> assertEquals(Outcome.WIN, scissors.getOutcome(new Hand(HandType.PAPER)))
        );
    }
}