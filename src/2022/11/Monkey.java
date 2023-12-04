package twentytwo.eleven;

import java.math.BigInteger;
import java.util.List;
import java.util.function.ToIntFunction;
import java.util.function.ToLongFunction;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Monkey {
    private int id;
    private List<BigInteger> items;
    private int operationId;
    private BigInteger operationValue;

    private int trueTarget;
    private int falseTarget;

    private BigInteger testValue;

    private int checkCount;

    public Monkey(List<String> initText) {
        this.checkCount = 0;

        for (String line : initText) {

            line = line.trim();

            if (line.startsWith("Monkey")) {

                this.id = Integer.parseInt(line.replace("Monkey ", "").replace(":", ""));

            } else if (line.startsWith("Starting")) {

                this.items = Stream
                        .of(line.replace("Starting items: ", "").replace(",", "").split(" "))
                        .map(Long::parseLong)
                        .map(BigInteger::valueOf).collect(Collectors.toList());

            } else if (line.startsWith("Operation")) {

                List<String> elements = List.of(line.replace("Operation: new = ", "").split(" "));

                if (elements.get(1).equals("+")) {
                    if (elements.get(2).equals("old")) {
                        this.operationId = 0;
                    } else {
                        this.operationValue = BigInteger.valueOf(Long.parseLong(elements.get(2)));
                        this.operationId = 1;
                    }
                } else {
                    if (elements.get(2).equals("old")) {
                        this.operationId = 2;
                    } else {
                        this.operationValue = BigInteger.valueOf(Long.parseLong(elements.get(2)));
                        this.operationId = 3;
                    }
                }

            } else if (line.startsWith("If true")) {
                this.trueTarget = Integer.parseInt(line.replace("If true: throw to monkey ", ""));
            } else if (line.startsWith("If false")) {
                this.falseTarget = Integer.parseInt(line.replace("If false: throw to monkey ", ""));
            } else if (line.startsWith("Test:")) {
                this.testValue = BigInteger.valueOf(Long.parseLong(line.replace("Test: divisible by ", "")));
            } else {
                System.out.println("Unknown line: " + line);
            }
        }
    }

    public BigInteger operate(BigInteger inputValue) {
        switch (this.operationId) {
            case 0:
                return inputValue.add(inputValue);
            case 1:
                return inputValue.add(this.operationValue);
            case 2:
                return inputValue.multiply(inputValue);
            case 3:
                return inputValue.multiply(this.operationValue);
        }
        return null;
    }

    public void addCount(int count) {
        this.checkCount += count;
    }

    public int getCount() {
        return this.checkCount;
    }

    public List<BigInteger> getItems() {
        return this.items;
    }

    public void addItem(BigInteger item) {
        this.items.add(item);
    }

    public void setItems(List<BigInteger> newItems) {
        this.items = newItems;
    }

    public int getId() {
        return id;
    }

    public int getTrueTarget() {
        return trueTarget;
    }

    public int getFalseTarget() {
        return falseTarget;
    }

    public BigInteger getTestValue() {
        return testValue;
    }

    @Override
    public String toString() {
        return "Monkey#" + this.id + " (items=" + this.items + ", true=" + this.trueTarget + ", false=" + this.falseTarget + ", test=" + this.testValue + ", operationId=" + this.operationId + ", operationValue=" + this.operationValue + ")";
    }
}
