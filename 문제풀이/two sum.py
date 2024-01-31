# testdome two sum 문제
# https://www.testdome.com/questions/python/two-sum/94858

'''
처음에 리스트 순회 방식으로 구현했으나 시간 효율성 때문에 불통과. 찾는 값이 리스트에 있는지 in 으로 찾는 작업(O(n))을 n번 반복해서 O(n^2)이었기 때문.
핵심은 해시 테이블을 이용하는 것이었다. 특정 값을 찾는 작업이 O(1)이므로 n번 반복해도 O(n) !
'''

def find_two_sum(numbers, target_sum):
    """
    :param numbers: (list of ints) The list of numbers.
    :param target_sum: (int) The required target sum.
    :returns: (a tuple of 2 ints) The indices of the two elements whose sum is equal to target_sum
    """
    hash_table = {}
    for i in range(len(numbers)):
      find_num = target_sum - numbers[i]
      if find_num in hash_table: # O(1)
        return (i, hash_table[find_num])
      hash_table[numbers[i]] = i
        
    return None

if __name__ == "__main__":
    print(find_two_sum([3, 1, 5, 7, 5, 9], 10))
    #print(find_two_sum([1,1,1,5,1], 5))
