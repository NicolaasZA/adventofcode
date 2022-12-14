package twentytwo.one;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

public class Elf {
    private final List<Integer> calories;

    public Elf() {
        calories = new java.util.ArrayList<>();
    }

    public static List<Elf> getFromShelf(String path) {
        List<Elf> elves = new ArrayList<>();

        try {

            List<String> allLines = Files.readAllLines(Paths.get(path));

            Elf currentElf = new Elf();

            for (String line : allLines) {
                if (line.equals("")) {
                    elves.add(currentElf);
                    currentElf = new Elf();
                } else {
                    currentElf.carry(Integer.parseInt(line));
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        return elves;
    }

    protected void carry(Integer value) {
        calories.add(value);
    }

    public int getCalories() {
        return calories.stream().reduce(0, Integer::sum);
    }
}
