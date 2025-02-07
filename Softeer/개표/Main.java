// import java.io.InputStreamReader;
// import java.util.LinkedList;
// import java.util.List;
// import java.util.Scanner;

public class Main {
//   public static void main(String[] args) {
//     final Solver solver = new Solver(args);
//     System.out.println(solver.getAnswer());
//   }

//   private static class Solver {
//     private final static String Bundle_Vote = "++++";
//     private final static String Single_Vote = "|";

//     private int t;
//     private List<Integer> votes;

//     public Solver(String[] args) {
//       final BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
//       t = Integer.parseInt(reader.readLine());
//       assert (t >= 1 && t <= 100);

//       votes = new LinkedList<>();
//       for (int i = 1; i <= t; i++) { 
//         final int n = Integer.parseInt(reader.readLine());
//         assert (n >= 1 && n <= 100);
//         votes.add(n);
//       }
//     }

//     public String getAnswer() {
//       return getVoteMarks();
//     }

//     private String getVoteMarks() {
//       final List<String> buffer = new LinkedList<>();

//       for (int vote : votes) {
//         buffer.add(getVoteMark(vote));
//       }
      
//       final String marks = String.join("\n", buffer);
//       return marks;
//     }

//     private String getVoteMark(int n) {
//       final int bundle = n / 5;
//       final int remain = n % 5;

//       final List<String> buffer = new LinkedList<>();
//       for (int i = 0; i < bundle; i++) buffer.add(Bundle_Vote);
//       if (remain > 0) buffer.add("|".repeat(remain));

//       final String mark = String.join(" ", buffer);
//       return mark;
//     }
//   }
}