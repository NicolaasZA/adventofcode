package twentytwo.two;

import twentytwo.two.enums.HandType;
import twentytwo.two.enums.Outcome;

import java.util.List;

public class PartTwo {

    public static void main(String[] args) {
        List<Round> rounds = Round.getFromFile("src/twentytwo/two/input.txt");

        int score = 0;
        for( Round r : rounds ) {

            Hand myCurrentHand = r.getMyHand();
            Hand opponentHand = r.getOpponentHand();

            Outcome desiredOutcome = HandType.asOutcome(myCurrentHand.getType());

            Hand myNewHand = Hand.fromOutcome(desiredOutcome, opponentHand);

            r.setMyHand(myNewHand);

            score += r.calculateScore();
        }

        System.out.println(score); // 16862
    }

}
