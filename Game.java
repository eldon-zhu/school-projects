import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;


public class Game extends Thread {
    private final Board board;
    private final Player player;
    private final GameRecorder gameRecorder;
    private final HighScoreManager highScoreManager;
    private final List<Card> cards;

    private final int totalPairs;
    private int numPairsFound;
    private int numMoves;
    private int rows;
    private int cols;
    private int secs;


    public Game(int rows, int cols, int secs, int totalPairs, Player player, GameRecorder gameRecorder, HighScoreManager highScoreManager) {

        this.totalPairs = totalPairs;
        this.player = player;
        this.gameRecorder = gameRecorder;
        this.highScoreManager = highScoreManager;
        this.numPairsFound = 0;
        this.numMoves = 0;
        this.cards = new ArrayList<>();
        this.rows = rows;
        this.cols = cols;
        this.board = new Board(rows, cols);
        this.secs = secs;
    }

    public static void clearScreen() {
        System.out.println("\033[H\033[2J");
        System.out.flush();
    }
    public void play() {
        while (numPairsFound < totalPairs) {
            board.print();
            Move selection = new Move(player.getMove(board));
            Card card1 = board.getCard(selection.getRow1(),selection.getCol1());
            Card card2 = board.getCard(selection.getRow2(),selection.getCol2());
            clearScreen();
            card1.show();
            card2.show();
            board.print();
            numMoves++;
            if (card1.equals(card2)) {
                System.out.println("Nice!");
                numPairsFound++;
                clearScreen();

            } else {
                System.out.println("Not quite it, tiles will flip back!");
                for (int sec = 0; sec < secs; sec++) {
                    int timeRemaining = secs - sec;
                    System.out.println( timeRemaining + " second(s) remaining!");
                    try {
                        Thread.sleep(1000);
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }
                card1.hide();
                card2.hide();
                clearScreen();
            }
            gameRecorder.recordMove(selection);
        }
        System.out.println("Congratulations, you won in " + numMoves + " moves!");
        highScoreManager.updateHighScore(player.getName(), (rows*cols), numMoves);
        highScoreManager.displayHighScores(rows*cols);
    }

    public Board getBoard() {
        return board;
    }
    public Player getPlayer() {
        return player;
    }
    public GameRecorder getGameRecorder() {
        return gameRecorder;
    }
    public HighScoreManager getHighScoreManager() {
        return highScoreManager;
    }
    public int getTotalPairs() {
        return totalPairs;
    }
    public int getNumPairsFound() {
        return numPairsFound;
    }
    public int getNumMoves() {
        return numMoves;
    }
    public int getRows() {
        return rows;
    }
    public int getCols() {
        return cols;
    }
    public int getSecs() {
        return secs;
    }
    public List<Card> getCards() {
        return cards;
    }


}
