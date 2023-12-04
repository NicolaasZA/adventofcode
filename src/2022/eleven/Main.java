package twentytwo.eleven;

import java.io.IOException;
import java.math.BigInteger;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class Main {
    public static final String INPUT_FILE = "src/twentytwo/eleven/input.txt";

    public static void main(String[] args) {
        System.out.println("1 => " + run(20, 3));
        System.out.println("2 => " + run(10000, 1));
    }

    public static BigInteger run(int roundCount, long worryDivider) {
        List<Monkey> monkeys = readFile();
        long modulo = 9699690;

        for (int r = 0; r < roundCount; r++) {
            for (Monkey m : monkeys) {
                List<BigInteger> items = m.getItems();
                for (BigInteger item : items) {
                    BigInteger worryLevel = m.operate(item);

                    if (worryDivider > 1) {
                        worryLevel = worryLevel.divide(BigInteger.valueOf(worryDivider));
                    } else {
                        worryLevel = worryLevel.mod(BigInteger.valueOf(modulo));
                    }

                    if (worryLevel.mod(m.getTestValue()).longValue() == 0) {
                        // Go to true monkey
                        monkeys.get(m.getTrueTarget()).addItem(worryLevel);
                    } else {
                        // Go to false monkey
                        monkeys.get(m.getFalseTarget()).addItem(worryLevel);
                    }
                }
                // Count these checks
                m.addCount(items.size());
                // Every item should now be thrown, so monkey no has items
                m.setItems(new ArrayList<>());
            }
        }

        List<Integer> collect = monkeys.stream().map(Monkey::getCount).sorted((e1, e2) -> e1 > e2 ? -1 : 1).toList();
        BigInteger a = BigInteger.valueOf(collect.get(0));
        BigInteger b = BigInteger.valueOf(collect.get(1));

        return a.multiply(b);
    }

    protected static List<Monkey> readFile() {
        List<Monkey> monkeys = new ArrayList<>();

        try {

            List<String> allLines = Files.readAllLines(Paths.get(INPUT_FILE));

            List<String> monkeyLines = new ArrayList<>();

            for (String line : allLines) {
                if (line.equals("")) {
                    monkeys.add(new Monkey(monkeyLines));
                    monkeyLines = new ArrayList<>();
                } else {
                    monkeyLines.add(line);
                }
            }

            if (monkeyLines.size() > 0) {
                monkeys.add(new Monkey(monkeyLines));
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        return monkeys;
    }


}
