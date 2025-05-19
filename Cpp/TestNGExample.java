import org.testng.Assert;
import org.testng.annotations.Test;

public class TestNGExample {

    @Test
    public void testAddition() {
        int a = 5;
        int b = 3;
        int result = a + b;
        // Verify that 5 + 3 equals 8
        Assert.assertEquals(result, 8, "Addition result is incorrect");
    }

    @Test
    public void testStringEquality() {
        String str1 = "TestNG";
        String str2 = "TestNG";
        // Verify that the two strings are equal
        Assert.assertEquals(str1, str2, "Strings are not equal");
    }

    @Test
    public void testFailure() {
        int x = 5;
        int y = 2;
        int result = x * y;
        // This will fail because 5 * 2 is 10, not 15
        Assert.assertEquals(result, 15, "Multiplication result is incorrect");
    }
}
