#include <iostream>
#include <vector>
using namespace std;

vector<int> productExceptSelf(vector<int>& nums) {
    int n = nums.size();
    vector<int> answer(n);

    for (int i = 0; i < n; i++) {
        int product = 1;

        for (int j = 0; j < n; j++) {
            if (i != j) {
                product *= nums[j];
            }
        }

        answer[i] = product;
    }

    return answer;
}

int main() {
    int n;

    cout << "Enter the size of the array: ";
    cin >> n;

    vector<int> nums(n);

    cout << "Enter " << n << " elements: ";
    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }

    vector<int> result = productExceptSelf(nums);

    cout << "\nProduct of array except self is:\n";
    for (int i = 0; i < n; i++) {
        cout << result[i] << " ";
    }

    return 0;
}