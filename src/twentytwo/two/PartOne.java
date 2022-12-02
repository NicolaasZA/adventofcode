package twentytwo.two;

import java.util.List;

public class PartOne {

    public static void main(String[] args) {
        List<Round> rounds = Round.getFromFile("src/twentytwo/two/input.txt");

        int score = 0;
        for (Round r : rounds) {
            score += r.calculateScore();
        }

        System.out.println(score); // 11475
    }
}
