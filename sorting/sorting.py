#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by tz301 on 2020/5/9
"""排序算法."""
import logging

from base.utils import LOGGER_FORMAT


def __bubble_sorting(nums):
  """冒泡排序."""
  length = len(nums)
  for i in range(length):
    is_sort = True
    for j in range(1, length - i):
      if nums[j] < nums[j - 1]:
        nums[j], nums[j - 1] = nums[j - 1], nums[j]
        is_sort = False

    if is_sort:
      break


def __selection_sorting(nums):
  """选择排序."""
  length = len(nums)
  for i in range(length):
    min_index = i
    for j in range(i + 1, length):
      if nums[j] < nums[min_index]:
        min_index = j

    if min_index != i:
      nums[i], nums[min_index] = nums[min_index], nums[i]


def __insertion_sorting(nums):
  """插入排序."""
  length = len(nums)
  for i in range(1, length):
    tmp = nums[i]
    j = i
    while j > 0 and tmp < nums[j - 1]:
      nums[j] = nums[j - 1]
      j -= 1
    nums[j] = tmp


def __shell_sort(nums):
  """希尔排序."""
  gap = 1
  num = len(nums)
  while gap < num / 3:  # 动态定义增量序列.
    gap = gap * 3 + 1

  while gap > 0:
    for i in range(gap, num):
      current = nums[i]
      j = i - gap
      while j >= 0 and current < nums[j]:
        nums[j + gap] = nums[j]
        j -= gap
      nums[j + gap] = current
    gap //= 2


def __merge(nums1, nums2):
  """合并两个有序数组."""
  result = list()
  len1, len2 = len(nums1), len(nums2)
  index1, index2 = 0, 0
  while index1 < len1 or index2 < len2:
    if index1 == len1:
      result.append(nums2[index2])
      index2 += 1
    elif index2 == len2:
      result.append(nums1[index1])
      index1 += 1
    elif nums1[index1] < nums2[index2]:
      result.append(nums1[index1])
      index1 += 1
    else:
      result.append(nums2[index2])
      index2 += 1
  return result


def __merge_sort_internal(nums):
  """归并排序."""
  if len(nums) < 2:
    return nums
  else:
    mid = len(nums) // 2
    left, right = nums[:mid], nums[mid:]
    return __merge(__merge_sort_internal(left), __merge_sort_internal(right))


def __merge_sort(nums):
  """归并排序."""
  new_nums = __merge_sort_internal(nums)
  for i in range(len(nums)):
    nums[i] = new_nums[i]


def __partition(nums, left, right):
  """快速排序分区."""
  pivot = left
  for i in range(left, right):
    if nums[i] < nums[right]:
      nums[i], nums[pivot] = nums[pivot], nums[i]
      pivot += 1
  nums[right], nums[pivot] = nums[pivot], nums[right]
  return pivot


def __quick_sort(nums, left=None, right=None):
  """快速排序."""
  left = 0 if left is None else left
  right = len(nums) - 1 if right is None else right

  if left < right:
    index = __partition(nums, left, right)
    __quick_sort(nums, left, index - 1)
    __quick_sort(nums, index + 1, right)


def __heapify(nums, index):
  """堆调整."""
  left = 2 * index + 1
  right = 2 * index + 2
  largest = index

  if left < __LEN and nums[left] > nums[largest]:
    largest = left

  if right < __LEN and nums[right] > nums[largest]:
    largest = right

  if largest != index:
    nums[index], nums[largest] = nums[largest], nums[index]
    __heapify(nums, largest)


__LEN = 0


def __build_top_heap(nums):
  """建立顶堆."""
  global __LEN  # pylint: disable=global-statement

  __LEN = len(nums)
  for i in range(__LEN // 2, -1, -1):
    __heapify(nums, i)


def __heap_sort(nums):
  """堆排序."""
  global __LEN  # pylint: disable=global-statement
  __build_top_heap(nums)

  for i in range(len(nums) - 1, 0, -1):
    nums[0], nums[i] = nums[i], nums[0]
    __LEN -= 1
    __heapify(nums, 0)


def __counting_sort(nums, max_value=100):
  """计数排序."""
  bucket = [0] * (max_value + 1)
  for num in nums:
    bucket[num] += 1

  nums.clear()
  for i, num in enumerate(bucket):
    if num > 0:
      nums.extend([i] * num)


def __bucket_sort(nums):
  min_value, max_value = min(nums), max(nums)

  bucket_size = 5
  bucket_num = (max_value - min_value) // bucket_size + 1
  buckets = [[] for _ in range(bucket_num)]

  for num in nums:
    buckets[(num - min_value) // bucket_size].append(num)

  index = 0
  for bucket in buckets:
    __insertion_sorting(bucket)
    for num in bucket:
      nums[index] = num
      index += 1


def __radix_sort(nums):
  """基数排序."""
  max_digits = len(str(max(nums)))

  mod = 10
  div = 1
  counter = [[] for _ in range(10)]
  for i in range(max_digits):
    for num in nums:
      counter[num % mod // div].append(num)

    nums.clear()
    for counter_one in counter:
      if counter_one:
        nums.extend(counter_one)
        counter_one.clear()

    mod *= 10
    div *= 10


def __cmd():
  """测试排序算法."""
  in_list = [5, 4, 2, 3, 29, 8, 1, 7, 13]
  func_list = [
      ("冒泡", __bubble_sorting),
      ("选择", __selection_sorting),
      ("插入", __insertion_sorting),
      ("希尔", __shell_sort),
      ("归并", __merge_sort),
      ("快速", __quick_sort),
      ("堆", __heap_sort),
      ("计数", __counting_sort),
      ("桶", __bucket_sort),
      ("基数", __radix_sort)
  ]

  ret = [1, 2, 3, 4, 5, 7, 8, 13, 29]
  for name, sorting_func in func_list:
    out_list = in_list.copy()
    sorting_func(out_list)
    assert out_list == ret, f"{name}排序错误: {out_list} != {ret}."


if __name__ == '__main__':
  logging.basicConfig(format=LOGGER_FORMAT, level=logging.INFO)
  __cmd()
