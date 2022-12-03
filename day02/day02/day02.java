import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;
import java.util.HashMap;
import java.util.stream.Stream;

public class day02{
    public static String sampleFileName = "/home/jon/git/AOC2022/day02/day02/sample";
    public static String inputFileName = "/home/jon/git/AOC2022/day02/day02/input";

    public static void main(String[] args) throws IOException
    {
        // Path inputPath = Paths.get(sampleFileName);
        Path inputPath = Paths.get(inputFileName);

        List <String> lines = Files.readAllLines(inputPath, StandardCharsets.UTF_8);
        // lines.forEach(line -> System.out.println(line));

        System.out.println("Part 1: " + part1(lines));
        System.out.println("Part 2: " + part2(lines));
    }


    public static int part1(List<String> lines){
        HashMap<String, Integer> scores = new HashMap<>();
        Integer totalScore = 0;

        scores.put("A X", 4);
        scores.put("A Y", 8);
        scores.put("A Z", 3);
        scores.put("B X", 1);
        scores.put("B Y", 5);
        scores.put("B Z", 9);
        scores.put("C X", 7);
        scores.put("C Y", 2);
        scores.put("C Z", 6);

        // totalScore = Stream.of(lines)
        //                    .map(move -> scores.get(move))
        //                    .reduce(0, Integer::sum);
        for (String move: lines)
            totalScore += scores.get(move);
        return totalScore;
    }

    public static int part2(List<String> lines){
        HashMap<String, Integer> scores = new HashMap<>();
        int totalScore = 0;

        scores.put("A X", 3);
        scores.put("A Y", 4);
        scores.put("A Z", 8);
        scores.put("B X", 1);
        scores.put("B Y", 5);
        scores.put("B Z", 9);
        scores.put("C X", 2);
        scores.put("C Y", 6);
        scores.put("C Z", 7);

        // totalScore = lines.map(move -> scores.get(move)).sum();
        for (String move: lines)
            totalScore += scores.get(move);
        return totalScore;
    }
}