import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class boj_12851 {
    static int N, K;
    static boolean check[] = new boolean[100001];
    static int cnt[] = new int[100001]; // 현재 인덱스까지 올 수 있는 방법의 수
    static int dist[] = new int[100001];

    private static void bfs(int n, int k) {
        Queue<Integer> q = new LinkedList<>();

        q.add(n);
        check[n] = true;
        cnt[n] = 1;

        while (!q.isEmpty()) {
            int now = q.poll();
            int[] next = {now + 1, now - 1, now * 2};
            for (int x : next) {
                if (x >= 0 && x <= 100000) {
                    if (!check[x]) { // 방문 안 한 경우
                        check[x] = true;
                        dist[x] = dist[now] + 1;
                        q.add(x);
                        cnt[x] = cnt[now];
                    } else if (dist[x] == dist[now] + 1) {// 다음 지점이 겹치는 경우 현 지점까지 오는 방법을 다음 지점에 누적
                        cnt[x] += cnt[now];
                    }
                }
            }
        }

        System.out.println(dist[k]);
        System.out.println(cnt[k]);
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        bfs(N, K);
    }

}
