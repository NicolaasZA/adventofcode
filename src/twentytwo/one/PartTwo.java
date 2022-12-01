package twentytwo.one;

import java.util.List;

public class PartTwo {

    public static void main(String[] args) {
        List<Elf> elves = Elf.getElvesFromFile("src/twentytwo/one/input.txt");

        // sort by calories
        elves.sort((e1, e2) -> e1.getTotal() > e2.getTotal() ? -1 : 1);

        int sum = elves.get(0).getTotal() + elves.get(1).getTotal() + elves.get(2).getTotal();

        System.out.println(sum); // 199628
    }

}
