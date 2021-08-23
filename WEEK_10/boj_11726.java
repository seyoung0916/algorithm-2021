import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class boj_11726 {
    static int n;
    static int[] cnt = new int[1001];

    private static void solve(int n) {
        for (int i = 3; i <= n; i++) {
            cnt[i] = (cnt[i - 1] + cnt[i - 2]) % 10007;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());

        cnt[1] = 1;
        cnt[2] = 2;
        if (n >= 3) {
            solve(n);
        }
        System.out.println(cnt[n]);
    }
}
