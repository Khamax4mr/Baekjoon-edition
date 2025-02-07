import java.util.LinkedList;
import java.util.List;


public class Main {
  public static void main(String[] args) {
    final Solver solver = new Solver(args);
    System.out.println(solver.getAnswer());
  }

  private static class Solver {
    public Solver(String[] args) {}

    public String getAnswer() {
      return getMessage();
    }

    private String getMessage() {
      final String message = "엄마 아빠 사랑해요!";
      return message;
    }
  }
}