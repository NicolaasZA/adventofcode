package twentytwo.two;

import twentytwo.two.enums.Outcome;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

public class Round {

    public static final int SCORE_LOSS = 0;
    public static final int SCORE_DRAW = 3;
    public static final int SCORE_WIN = 6;
    private Hand myHand;
    private final Hand opponentHand;

    public Round(Hand opponentHand, Hand myHand) {
        this.opponentHand = opponentHand;
        this.myHand = myHand;
    }

    public Round(String opponent, String mine) {
        this.opponentHand = Hand.fromInput(opponent);
        this.myHand = Hand.fromInput(mine);
    }

    public static List<Round> getFromFile(String path) {
        List<Round> result = new ArrayList<>();

        try {

            List<String> allLines = Files.readAllLines(Paths.get(path));


            for (String line : allLines) {
                String[] s = line.split(" ");
                result.add(new Round(s[0], s[1]));
            }

        } catch (IOException e) {
            e.printStackTrace();
        }

        return result;
    }

    public int calculateScore() {
        // Get score from hand played
        int playScore = myHand.getType().ordinal() + 1;

        // Get score from match outcome.
        Outcome matchResult = myHand.getOutcome(opponentHand);
        int outcomeScore = SCORE_DRAW;
        if (matchResult == Outcome.WIN) {
            outcomeScore = SCORE_WIN;
        } else if (matchResult == Outcome.LOSS) {
            outcomeScore = SCORE_LOSS;
        }

        return outcomeScore + playScore;
    }

    public Hand getMyHand() {
        return myHand;
    }

    public void setMyHand(Hand newValue) {
        this.myHand = newValue;
    }

    public Hand getOpponentHand() {
        return opponentHand;
    }
}
