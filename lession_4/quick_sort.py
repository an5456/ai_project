def quick_sort(sort_list, start_index, end_index):
    if start_index < end_index:  # 如果角标左侧小于右侧则开始排序,否则退出
        basic, i, j = sort_list[start_index], start_index, end_index
        while i < j:
            while i < j and basic <= sort_list[j]:  # 基准值比j(右侧)小,那么该值不做任何事情
                j -= 1
            while i < j and basic >= sort_list[i]:
                i += 1
            sort_list[i], sort_list[j] = sort_list[j], sort_list[i]
        sort_list[i], sort_list[start_index] = sort_list[start_index], sort_list[i]
        quick_sort(sort_list, start_index, i - 1)
        quick_sort(sort_list, i + 1, end_index)
l = [10, 6, 9, 18, 20, 5, 7, 15, 14, 18,19]
quick_sort(l,0,len(l)-1)
print(l)