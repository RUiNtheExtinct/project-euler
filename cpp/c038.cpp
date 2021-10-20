#include <bits/stdc++.h>
#include <bits/extc++.h>

using namespace std;
using namespace __gnu_pbds;

#define all(x) (x).begin(), (x).end()
#define fro(i, a, n, s) for (int i = (a); i < (n); i += (s))
#define fr(i, a, n) for (int i = (a); i < (n); i += (1))
#define frbo(i, a, n, s) for (int i = (a); i >= (n); i -= (s))
#define frb(i, a, n) for (int i = (a); i >= (n); i -= (1))
#define sz(x) (int)(x).size()
#define trav(a, x) for (auto &a : x)
#define csbits(x) __builtin_popcountll(x)
#define mk(arr, n, type) type *arr = new type[n]

#define str string
#define li long int
#define uli unsigned long int
#define ll long long
#define ull unsigned long long
#define ld long double
#define pll pair<ll, ll>
#define vl vector<ll>
#define v vector
#define vpl vector<pll>
#define msll multiset<ll>
#define mpll map<ll, ll>
#define umap unordered_map
#define pqll priority_queue<ll>

#define ff first
#define ss second
#define mp make_pair
#define pb push_back
#define ppb pop_back
#define pf push_front
#define ppf pop_front
#define eb emplace_back
#define lb lower_bound

#define ed '\n'
#define sp " \n"[i == n - 1]
#define null NULL
#define nulp nullptr

mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());
typedef tree<ll, null_type, less<ll>, rb_tree_tag, tree_order_statistics_node_update> pbds;

template <typename T>
T const pi = std::acos(-T(1));
#define MAX 100005
#define MOD 1000000007 // 998244353
#define INF 1e18 + 1
ll d8[8][2] = {{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}};
ll d4[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};

//#define ONLINE_JUDGE 1
/*
    g++ c1.cpp -o c1.exe
    g++ -o c1 c1.cpp&c1.exe
*/

bool is_pandigital(str s, ll k)
{
    if (s.length() < k)
        return false;
    sort(all(s));
    if (k == 8)
        return s == "12345678";
    return s == "123456789";
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin.exceptions(cin.failbit);

    ll n, r;
    cin >> n >> r;
    set<ll> s;
    vl bounds = {0, 0, 3, 2, 1, 0, 0, 0, 0, 0};
    fr(i, 2, r + 1)
    {
        fr(j, (ll)pow(10, bounds[i]) == 1 ? 2 : (ll)pow(10, bounds[i]), min(n, (ll)pow(10, bounds[i] + 1)))
        {
            str a = "";
            fr(l, 1, i + 1)
            {
                str a = "";
                fr(k, 1, l + 1) a += to_string(k * j);
                if (is_pandigital(a, r))
                    s.insert(j);
            }
        }
    }
    trav(a, s) cout << a << ed;

    return 0;
}