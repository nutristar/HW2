""". Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке. Для выполнения задания обязательно использовать генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]."""
nums1= [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

nums2=[x for x in nums1 if nums1.count(x)==1]

print(nums2)  #[23, 1, 3, 10, 4, 11]