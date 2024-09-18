#include <iostream>
#include <vector>
#include <string>
using namespace std;

struct book
{
    string isbn;
    string name;
    int year;
};

void merge(vector<book> &arr, const int left,const int mid, const int right)
{
            const int n1 = mid - left + 1;
            const int n2 = mid - left + 1;
    vector<book> left_arr(n1), right_arr(n2);
    for (int i = 0; i < n1; i++)
        left_arr[i] = arr[left + i];
    for (int j = 0; j< n2; j++)
        right_arr[j] = arr[mid + 1 + j];
    int i = 0, j = 0, k = left;
    while (i < n1 && j < n2)
    {
        if (left_arr[i].year < right_arr[i].year || (left_arr[i].year == right_arr[i].year && left_arr[i].name <= right_arr[i].name))
        {
            arr[k++] = left_arr[i++];
        }
        else
        {
            arr[k] = right_arr[j++];
        }
        k++;
    }
    while(i < n1)
        arr[k++] = left_arr[i++];
    while(j < n2)
        arr[k++] = right_arr[j++];
}
void MergeSort(vector<book> &arr, const int left, const int right)
{
    if (left >= right)
        return;
    const int mid = left + (right - left) / 2;
    MergeSort(arr, left, mid);
    MergeSort(arr, mid + 1, right);
    
    merge(arr, left, mid, right);
}

int main()
{
    int n;
    string s;
    getline(cin, s);
    n = stoi(s);
    vector<book> library;
    book bk;
    for (int i=0; i < n; i++)
    {
        getline(cin, s);
        cout<<s<<'\n';
        bk.isbn = s.substr(0, 10);
        bk.name = "";
        bk.year = 0;
        short flag = 0;
        string year = "";
        for (auto c : s.substr(12, s.size()))
        {
            if (c != '"' && flag != 2)
            {
                bk.name += c;
            }
            else if (c == '"')
            {
                bk.name += c;
                flag++;
            }
            else if (c != '\n' && c != ' ')
            {
                year += c;
            }
        }
        cout<<"Year is: "<<year<<'\n';
        bk.year = stoi(year);
        library.push_back(bk);
        
    }
    cout<<"value is: "<<library.size();
    MergeSort(library, 0, n - 1);
    for (int i=0; i < n; i++)
    {
        book bk = library[i];
        cout << bk.isbn << " " << bk.name << " " << bk.year << "\n";
        
    }

    return 0;
}
