import junit.framework.TestCase;
import org.junit.Test;
import static org.junit.Assert.*;

public class BoardTest {

    @Test
    public void testGenerateCards() {
        Board board = new Board(4, 4);
        Card[][] cards = board.generateCards(4, 4);

        assertEquals(cards.length, 4);
        assertEquals(cards[0].length, 4);
        assertEquals(cards[1].length, 4);
        assertEquals(cards[2].length, 4);
        assertEquals(cards[3].length, 4);

        int count = 0;
        for (int i = 0; i < cards.length; i++) {
            for (int j = 0; j < cards[0].length; j++) {
                assertNotNull(cards[i][j]);
                count++;
            }
        }
        assertEquals(count, 16);
    }

    @Test
    public void testGetCard() {
        Board board = new Board(2, 2);
        Card[][] cards = board.generateCards(2, 2);

        assertEquals(board.getCard(0, 0), cards[0][0]);
        assertEquals(board.getCard(1, 1), cards[1][1]);
    }

}

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

public class MoveTest {

    TestCase Assertions;
    @Test
    public void testGetters() {
        Move move = new Move(1, 2, 3, 4);
        Assertions.assertEquals(1, move.getRow1());
        Assertions.assertEquals(2, move.getCol1());
        Assertions.assertEquals(3, move.getRow2());
        Assertions.assertEquals(4, move.getCol2());
    }

    @Test
    public void testCopyConstructor() {
        Move original = new Move(1, 2, 3, 4);
        Move copy = new Move(original);
        Assertions.assertEquals(original.getRow1(), copy.getRow1());
        Assertions.assertEquals(original.getCol1(), copy.getCol1());
        Assertions.assertEquals(original.getRow2(), copy.getRow2());
        Assertions.assertEquals(original.getCol2(), copy.getCol2());
    }

}

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.util.ArrayList;
import java.util.List;

public class GameTest {

    @Test
    public void testGameConstructor() {
        Player player = new Player("Test Player");
        GameRecorder gameRecorder = new GameRecorder();
        HighScoreManager highScoreManager = new HighScoreManager();
        Game game = new Game(4, 4, 10, 8, player, gameRecorder, highScoreManager);
        assertNotNull(game.getBoard());
        assertNotNull(game.getPlayer());
        assertNotNull(game.getGameRecorder());
        assertNotNull(game.getHighScoreManager());
        assertEquals(8, game.getTotalPairs());
        assertEquals(0, game.getNumPairsFound());
        assertEquals(0, game.getNumMoves());
        assertEquals(4, game.getRows());
        assertEquals(4, game.getCols());
        assertEquals(10, game.getSecs());
        assertNotNull(game.getCards());
    }

    @Test
    public void testClearScreen() {
        // Cannot test console output, so only test that the method runs without errors
        Game.clearScreen();
    }

    @Test
    public void testPlay() {
        // Test a game where all pairs are found in the first try
        Player player = new Player("Test Player");
        GameRecorder gameRecorder = new GameRecorder();
        HighScoreManager highScoreManager = new HighScoreManager();
        Game game = new Game(2, 2, 10, 2, player, gameRecorder, highScoreManager);
        game.getBoard().setCard(0, 0, new Card('A'));
        game.getBoard().setCard(0, 1, new Card('A'));
        game.getBoard().setCard(1, 0, new Card('B'));
        game.getBoard().setCard(1, 1, new Card('B'));
        game.play();
        assertEquals(2, game.getNumPairsFound());
        assertEquals(1, game.getNumMoves());

        // Test a game where not all pairs are found in the first try
        player = new Player("Test Player");
        gameRecorder = new GameRecorder();
        highScoreManager = new HighScoreManager();
        game = new Game(2, 2, 10, 2, player, gameRecorder, highScoreManager);
        game.getBoard().setCard(0, 0, new Card('A'));
        game.getBoard().setCard(0, 1, new Card('B'));
        game.getBoard().setCard(1, 0, new Card('C'));
        game.getBoard().setCard(1, 1, new Card('D'));
        game.getPlayer().getScanner().setInput("1 1 2 2".getBytes());
        game.play();
        assertEquals(0, game.getNumPairsFound());
        assertEquals(1, game.getNumMoves());
    }

}
