#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by tz301 on 2020/5/9
"""排序算法."""
import logging

from base.utils import LOGGER_FORMAT

__LEN = 0
#
#
# def shell_sort(in_list: List) -> List:
#   """希尔排序."""
#   out_list = in_list.copy()
#   num = len(in_list)
#
#   gap = 1
#   while gap < num / 3:  # 动态定义增量序列.
#     gap = gap * 3 + 1
#
#   while gap > 0:
#     for i in range(gap, num):
#       current = out_list[i]
#       j = i - gap
#       while j >= 0 and current < out_list[j]:
#         out_list[j + gap] = out_list[j]
#         j -= gap
#
#       out_list[j + gap] = current
#
#     gap = floor(gap / 2)
#   return out_list
#
#
# def __merge(left, right):
#   """合并两个有序序列."""
#   left_index = 0
#   right_index = 0
#   out_list = list()
#   while left_index < len(left) and right_index < len(right):
#     if left[left_index] < right[right_index]:
#       out_list.append(left[left_index])
#       left_index += 1
#     else:
#       out_list.append(right[right_index])
#       right_index += 1
#
#   if left_index == len(left):
#     out_list.extend(right[right_index:])
#
#   if right_index == len(right):
#     out_list.extend(left[left_index:])
#   return out_list
#
#
# def merge_sort(in_list: List) -> List:
#   """归并排序."""
#   num = len(in_list)
#   if num < 2:
#     return in_list
#   else:
#     middle_index = floor(num / 2)
#     left = in_list[:middle_index]
#     right = in_list[middle_index:]
#     return __merge(merge_sort(left), merge_sort(right))
#
#
# def bucket_sort(in_list: List) -> List:
#   """桶排序."""
#   min_value = min(in_list)
#   max_value = max(in_list)
#
#   bucket_size = 5
#   bucket_count = int(floor(max_value - min_value) / bucket_size + 1)
#   buckets = [[] for _ in range(bucket_count)]
#
#   for value in in_list:
#     buckets[int(floor(value - min_value) / bucket_size)].append(value)
#
#   out_list = list()
#   for bucket in buckets:
#     out_list.extend(insertion_sorting(bucket))
#   return out_list
#
#
# def radix_sort(in_list: List) -> List:
#   """基数排序."""
#   max_digit = len(str(max(in_list)))
#
#   out_list = in_list.copy()
#   mod = 10
#   dev = 1
#   counter = [[] for _ in range(10)]
#   for i in range(max_digit):
#     for value in out_list:
#       bucket = int((value % mod) / dev)
#       counter[bucket].append(value)
#
#     out_list.clear()
#     for counter_one in counter:
#       if counter_one:
#         out_list.extend(counter_one)
#         counter_one.clear()
#
#     mod *= 10
#     dev *= 10
#   return out_list


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


def __partition(nums, pivot, right):
  """快速排序分区."""
  index = pivot + 1
  for i in range(index, right + 1):
    if nums[i] < nums[pivot]:
      nums[i], nums[index] = nums[index], nums[i]
      index += 1
  nums[pivot], nums[index - 1] = nums[index - 1], nums[pivot]
  return index - 1


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


def __cmd():
  """测试排序算法."""
  in_list = [5, 4, 2, 3, 29, 8, 1, 7, 13]
  func_list = [
      ("冒泡", __bubble_sorting),
      ("选择", __selection_sorting),
      ("插入", __insertion_sorting),
      # ("希尔", __shell_sort),
      # ("归并", __merge_sort),
      ("快速", __quick_sort),
      ("堆", __heap_sort),
      ("计数", __counting_sort),
      # ("桶", __bucket_sort),
      # ("基数", __radix_sort)
  ]

  ret = [1, 2, 3, 4, 5, 7, 8, 13, 29]
  for name, sorting_func in func_list:
    out_list = in_list.copy()
    sorting_func(out_list)
    assert out_list == ret, f"{name}排序错误: {out_list} != {ret}."


if __name__ == '__main__':
  logging.basicConfig(format=LOGGER_FORMAT, level=logging.INFO)
  __cmd()
