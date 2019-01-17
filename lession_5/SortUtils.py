class SortUtils:
    def sort_s(self, lis, way):
        if way == 'bubble':
            self._bubble(lis)
        if way == 'quick':
            self._quick(lis, 0, len(lis)-1)

    def _bubble(self, lis):
        for i in range(len(lis) - 1):
            for j in range(len(lis) - 1 - i):
                if lis[j] > lis[j + 1]:
                    lis[j], lis[j + 1] = lis[j + 1], lis[j]
                print(lis)
        return lis

    def _quick(self, list_str, start_index, end_index):
        if start_index < end_index:  # 角标左侧小于右侧开始排序
            i, basick, j = start_index, list_str[start_index], end_index
            while i <j:# 首先保证左侧的index比右侧的小
                while i < j and basick <= list_str[j]:  # 基准比有侧的下表为(j)值小时,角标做左移
                    j -= 1
                while i < j and basick >= list_str[i]:# 基准比左侧的下表为(i)值大时,角标右移
                    i += 1
                list_str[i], list_str[j]=list_str[j],list_str[i]
                print("i=" + str(i) + "&&&" + "j=" + str(j) + "$$$" + "sort_list=" + str(list_str))
            list_str[start_index],list_str[i]=list_str[i],list_str[start_index]# 当i=j时,将基准值与下标为i或者j的值交换位置
            self._quick(list_str,start_index , i-1)# 取i=j的下标左侧的值在执行
            self._quick(list_str,i+1,end_index)




if __name__ == '__main__':
    s = SortUtils()
    s.sort_s([10, 6, 9, 18, 20, 5, 7, 15, 14, 18, 19], 'quick')
    # s.sort_s([10, 6, 9, 18, 20, 5, 7, 15, 14, 18, 19], 'bubble')

