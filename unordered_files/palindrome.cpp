#include<bits/stdc++.h>
using namespace std;

string lcs(string &X, string &Y)
{
    int p = X.length();
    int q = Y.length();
    int L[p+1][q+1];
    for (int i=0; i<=p; i++)
    {
        for (int j=0; j<=q; j++)
        {
            if (i == 0 || j == 0)
                L[i][j] = 0;
            else if (X[i-1] == Y[j-1])
                L[i][j] = L[i-1][j-1] + 1;
            else
                L[i][j] = max(L[i-1][j], L[i][j-1]);
        }
    }

    int index = L[p][q];
    string lcs(index+1, '\0');
    int i = p, j = q;
    
    while (i > 0 && j > 0)
    {

        if (X[i-1] == Y[j-1])
        {

            lcs[index-1] = X[i-1];
            i--;
            j--;
            index--;
        }
        else if (L[i-1][j] > L[i][j-1])
            i--;
        else
            j--;
    }
 
    return lcs;
}

void longestPalSubsequence(string &str)
{

    string rev = str;
    reverse(rev.begin(), rev.end());
    string temp = lcs(str, rev);
    cout << temp.length() - 1 << endl << temp <<endl;
}
 

int main()
{
    string str;
    cin >> str;
    //longestPalSubsequence(str);
    ifstream myReadFile;
    myReadFile.open(str);
    char output[100];
    if (myReadFile.is_open()) {
        while (!myReadFile.eof()) {
            myReadFile >> output;
            longestPalSubsequence(output);
        }
    }
myReadFile.close();
    return 0;
}
