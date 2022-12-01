package twentytwo.one;

import java.util.Comparator;
import java.util.List;

public class PartOne {

    public static void main(String[] args) {
        List<Elf> elves = Elf.getElvesFromFile("src/twentytwo/one/input.txt");

        Elf max = elves.stream().max(Comparator.comparing(Elf::getTotal)).orElse(new Elf());

        System.out.println(max.getTotal()); // 67633
    }
}

