package twentytwo.one;

import java.util.List;

public class PartTwo {

    public static final int ELVES_TO_COUNT = 3;

    public static void main(String[] args) {
        List<Elf> elves = Elf.getFromShelf("src/twentytwo/one/input.txt");

        elves.sort((e1, e2) -> e1.getCalories() > e2.getCalories() ? -1 : 1);

        List<Elf> topElves = elves.subList(0, ELVES_TO_COUNT);

        System.out.println(topElves.stream().mapToInt(Elf::getCalories).sum()); // 199628
    }

}
