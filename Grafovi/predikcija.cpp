#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> pi;
typedef pair<ll, ll> pl;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<double> vd;
typedef vector<bool> vb;
typedef vector<char> vc;
typedef vector<string> vs;
typedef vector<pi> vp;
typedef vector<pl> vpl;

vi e[50000], p[50000];
bool b[50000][50000];

int main()
{
	ios_base::sync_with_stdio(false); 
	cin.tie(nullptr); 
	cout.tie(nullptr); 
	cerr.tie(nullptr);	

	int n, m;
	cin >> n >> m;

	vector<set<int>> sve;
	for (int i = 0; i < m * 7 / 10; ++i){
		int u, v;
		cin >> u >> v;
		b[u][v] = 1;
		e[u].push_back(v);
		e[v].push_back(u);
		sve[u].insert(v);
		sve[v].insert(u);
	}

	map<pair<int, int>, int> mapa;
	for (int i = 1; i <= n - 1; ++i){
		for (int j = i + 1; j <= n; ++j){
			for (auto& x : e[j]){
				sve[i].insert(x);
				b[j][x] = 1;
			}
			mapa[{i, j}] = sve.size();
		}
	}

	map<pair<int, int>, int> mapp;
	for (int i = 1; i<= n - 1; ++i){
		for (int j = i + 1; j <= n; ++j){
			set<int> tmp;
			if (b[i][j])
				continue;
			for (auto& x : e[i]){
				for (auto& y : e[j]){
					if (x == y)
						tmp.insert(x);
				}
			}
			mapp[{i, j}] = tmp.size();
		}
	}

	map<pi, double> sol;
	for (int i = 1; i <= n - 1; ++i){
		for (int j = i + 1; j <= n; ++j){
			if (b[i][j])
				continue;
			sol[{i, j}] = -1 * (mapp[{i, j}] * 1.0 / mapa[{i, j}]);
		}
	}

	vi res(n);
	for (auto& i : sol){
		int mini = min(i.first.first, i.first.second), maxi = max(i.first.first, i.first.second);
		res[mini] = maxi;
	}

	sort(res.begin(), res.end());

	m = m - (7 * m / 10);
	vi test(n);
	for (int i = 0; i < m; ++i){
		int u, v;
		cin >> u >> v;

		test[min(u, v)] = max(u, v);
	}

	sort(test.begin(), test.end());

	int cnt = 0;
	for (int i = 1; i <= n; ++i){
		if (test[i] == res[i])
			++cnt;
	}

	cout << "Uspelo je " << (cnt * 1.0 / m) * 100.0 << " procenata\n";
}