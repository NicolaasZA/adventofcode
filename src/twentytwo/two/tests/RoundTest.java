package twentytwo.two.tests;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import twentytwo.two.Hand;
import twentytwo.two.Round;
import twentytwo.two.enums.HandType;

import static org.junit.jupiter.api.Assertions.*;

class RoundTest {

    @Test
    @DisplayName("Testing calculateScore")
    void test_calculateScore() {

        // Test losses
        Round loss1 = new Round(new Hand(HandType.PAPER), new Hand(HandType.ROCK));
        Round loss2 = new Round(new Hand(HandType.SCISSORS), new Hand(HandType.PAPER));
        Round loss3 = new Round(new Hand(HandType.ROCK), new Hand(HandType.SCISSORS));

        // Test draw scores
        Round draw1 = new Round(new Hand(HandType.ROCK), new Hand(HandType.ROCK));
        Round draw2 = new Round(new Hand(HandType.PAPER), new Hand(HandType.PAPER));
        Round draw3 = new Round(new Hand(HandType.SCISSORS), new Hand(HandType.SCISSORS));

        // Test wins
        Round win1 = new Round(new Hand(HandType.SCISSORS), new Hand(HandType.ROCK));
        Round win2 = new Round(new Hand(HandType.ROCK), new Hand(HandType.PAPER));
        Round win3 = new Round(new Hand(HandType.PAPER), new Hand(HandType.SCISSORS));

        assertAll(
                () -> assertEquals(1, loss1.calculateScore()),
                () -> assertEquals(2, loss2.calculateScore()),
                () -> assertEquals(3, loss3.calculateScore()),

                () -> assertEquals(4, draw1.calculateScore()),
                () -> assertEquals(5, draw2.calculateScore()),
                () -> assertEquals(6, draw3.calculateScore()),

                () -> assertEquals(7, win1.calculateScore()),
                () -> assertEquals(8, win2.calculateScore()),
                () -> assertEquals(9, win3.calculateScore())
        );
    }
}