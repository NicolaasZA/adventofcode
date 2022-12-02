package twentytwo.two;

import java.util.List;

public class PartTwo {

    public static void main(String[] args) {
        List<Round> rounds = Round.getFromFile("src/twentytwo/two/input.txt");

        int score = 0;

        for( Round r : rounds ) {
            if (r.getMyPlay().equals(Round.M_LOSS)) {

                if (r.getOpponentPlay().equals(Round.O_ROCK)) {
                    r.setMyPlay(Round.M_SCISSORS);
                } else if (r.getOpponentPlay().equals(Round.O_PAPER)) {
                    r.setMyPlay(Round.M_ROCK);
                } else {
                    r.setMyPlay(Round.M_PAPER);
                }

            } else if (r.getMyPlay().equals(Round.M_DRAW)) {

                r.setMyPlay(r.getMySame(r.getOpponentPlay()));

            } else if (r.getMyPlay().equals(Round.M_WIN)) {

                if (r.getOpponentPlay().equals(Round.O_ROCK)) {
                    r.setMyPlay(Round.M_PAPER);
                } else if (r.getOpponentPlay().equals(Round.O_PAPER)) {
                    r.setMyPlay(Round.M_SCISSORS);
                } else {
                    r.setMyPlay(Round.M_ROCK);
                }

            }

            score += r.calculateScore();
        }

        System.out.println(score); // 16862
    }

}
