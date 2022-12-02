package twentytwo.two;

import twentytwo.one.Elf;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

public class Round {

    private String opponentPlay;
    private String myPlay;

    private final List<String> myPossibleValues = new ArrayList<>();

    public static final String O_ROCK = "A";
    public static final String O_PAPER = "B";
    public static final String O_SCISSORS = "C";

    public static final String M_ROCK = "X";
    public static final String M_PAPER = "Y";
    public static final String M_SCISSORS = "Z";

    public static final String M_LOSS = "X";
    public static final String M_DRAW = "Y";
    public static final String M_WIN = "Z";

    public static final int SCORE_LOSS = 0;
    public static final int SCORE_DRAW = 3;
    public static final int SCORE_WIN = 6;

    public Round(String opponentPlay, String myPlay) {
        this.opponentPlay = opponentPlay;
        this.myPlay = myPlay;

        myPossibleValues.add(M_ROCK);
        myPossibleValues.add(M_PAPER);
        myPossibleValues.add(M_SCISSORS);
    }

    public int calculateScore() {
        int outcomeScore = SCORE_DRAW;

        if (myPlay.equals(M_ROCK)) {

            if (opponentPlay.equals(O_PAPER)) {
                outcomeScore = SCORE_LOSS;
            } else if (opponentPlay.equals(O_SCISSORS)) {
                outcomeScore = SCORE_WIN;
            }

        } else if (myPlay.equals(M_PAPER)) {

            if (opponentPlay.equals(O_SCISSORS)) {
                outcomeScore = SCORE_LOSS;
            } else if (opponentPlay.equals(O_ROCK)) {
                outcomeScore = SCORE_WIN;
            }

        } else if (myPlay.equals(M_SCISSORS)) {

            if (opponentPlay.equals(O_ROCK)) {
                outcomeScore = SCORE_LOSS;
            } else if (opponentPlay.equals(O_PAPER)) {
                outcomeScore = SCORE_WIN;
            }

        }

        int playScore = myPossibleValues.indexOf(this.myPlay) + 1;

        return outcomeScore + playScore;
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

    public String getOpponentPlay() {
        return this.opponentPlay;
    }

    public void setOpponentPlay(String opponentPlay) {
        this.opponentPlay = opponentPlay;
    }

    public String getMyPlay() {
        return this.myPlay;
    }

    public void setMyPlay(String myPlay) {
        this.myPlay = myPlay;
    }

    public String getMySame(String opponentPlay) {
        if (opponentPlay.equals(O_ROCK)) {
            return M_ROCK;
        } else if (opponentPlay.equals(O_PAPER)) {
            return M_PAPER;
        }
        return M_SCISSORS;
    }

}
