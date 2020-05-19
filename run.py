from R_W_excel import read_data
from R_W_excel import write_data
from http_request import http_request

#读取注册的数据
# 获取注册的测试用例数据
register_test_cases = read_data("test_case.xlsx", 'register')
print("注册的用例数据：{}".format(register_test_cases))
print()

#测试环境的ip地址为：
IP="http://120.78.128.25:8766"

#http请求头信息
headers = {"X-Lemonban-Media-Type": "lemonban.v2", "Content-Type": "application/json;charset=UTF-8"}

#开始测试注册的用例
file_name='test_case.xlsx'
register_sheet='register'
for test_case in register_test_cases:
    test_result={}
    print("**------------目前正在测试{}模块的第{}条用例，用例标题为：{}------------**".format(test_case[1],test_case[0],test_case[2]))
    result=http_request(test_case[3],IP+test_case[4],eval(test_case[5]),headers)
    print("测试结果是：{}".format(result))
    test_result['code']=result['code']
    test_result['msg'] = result['msg']
    #判断结果是否通过
    if test_result==eval(test_case[6]):
        print("期望与实际结果一致，测试通过！")
        write_data(file_name,register_sheet,test_case[0]+ 1, 8,str(test_result))
        write_data(file_name, register_sheet, test_case[0] + 1, 9,'测试通过')
    else:
        print("期望与实际结果不一致，测试不通过！")
        write_data(file_name, register_sheet, test_case[0] + 1, 8, str(test_result))
        write_data(file_name, register_sheet, test_case[0] + 1, 9, '测试不通过')
    print("")
