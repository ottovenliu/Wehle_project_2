def calculate(min, max):
    # 請用你的程式補完這個函式的區塊
    if(float(min) > float(max)):
        (min, max) = (max, min)
    Answer_1 = (max-min+1)*(min+max)*0.5
    print(Answer_1)
    return Answer_1


calculate(1, 3)  # 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8)  # 你的程式要能夠計算 4+5+6+7+8，最後印出 30


def avg(data):
    # 請用你的程式補完這個函式的區塊
    total_2 = 0
    for i in range(int(data["count"])):
        total_2 += data["employees"][i]["salary"]
    Answer_2 = total_2/int(data["count"])
    print(Answer_2)
    return Answer_2


avg({
    "count": 3,
    "employees": [
        {
            "name": "John",
            "salary": 30000
        },
        {
            "name": "Bob",
            "salary": 60000
        },
        {
            "name": "Jenny",
            "salary": 50000
        }
    ]
})  # 呼叫 avg 函式


def maxProduct(nums):
    # 請用你的程式補完這個函式的區塊
    area_3 = []
    for i in nums:
        for j in nums:
            k = i*j
            if(i*j != i*i):
                area_3.append(k)

    Answer_3 = 0
    for l in range(len(area_3)):
        if(Answer_3 < area_3[l]):
            Answer_3 = area_3[l]
    print(Answer_3)
    return Answer_3


maxProduct([5, 20, 2, 6])  # 得到 120 因為 20 和 6 相乘得到最大值
maxProduct([10, -20, 0, 3])  # 得到 30 因為 10 和 3 相乘得到最大值


def twoSum(nums, target):
    # your code here
    area_4 = []
    for i in nums:
        for j in nums:
            if(i+j == target):
                a = (i, j)
                area_4.append(a)
    b = nums.index(area_4[0][0])
    c = nums.index(area_4[0][1])
    Answer_4 = [b, c]
    return Answer_4


result = twoSum([2, 11, 7, 15], 9)
print(result)  # show [0, 2] because nums[0]+nums[2] is 9
