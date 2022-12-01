package twentytwo.one;

import java.util.Comparator;
import java.util.List;

public class PartOne {

    public static void main(String[] args) {
        List<Elf> elves = Elf.getFromShelf("src/twentytwo/one/input.txt");

        Elf max = elves.stream().max(Comparator.comparing(Elf::getCalories)).orElse(new Elf());

        System.out.println(max.getCalories()); // 67633
    }
}

