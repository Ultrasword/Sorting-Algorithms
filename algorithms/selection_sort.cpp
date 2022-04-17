#include <iostream>

void selection_sort(int *nums, int size)
{
    int _min_index = 0, _min = 0;
    int pre = 0;
    for (int i = 0; i < size - 1; i++)
    {
        // find the _min value
        // swap with the current position
        _min = _INTEGRAL_MAX_BITS;
        for (int j = i; j < size; j++)
        {
            if (nums[j] < _min)
            {
                _min = nums[j];
                _min_index = j;
            }
        }
        // std::cout << "Start: " << i << " | End: " << size << " | Min: " << nums[_min_index] << std::endl;

        // swap
        pre = nums[i];
        nums[i] = nums[_min_index];
        nums[_min_index] = pre;
    }
}

int main()
{
    int nums[] = {10, 9, 8, 7, 6, 5, 4, 3, 2, 1};

    selection_sort(nums, sizeof(nums) / sizeof(int));

    for (int i = 0; i < sizeof(nums) / sizeof(int); i++)
        std::cout << nums[i] << " ";
    std::cout << std::endl;
}
