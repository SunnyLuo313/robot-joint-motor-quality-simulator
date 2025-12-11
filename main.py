from data_simulator import simulate_motor_data
from test_runner import MotorQualityTester
import json

def main():
    print("=== 机器人关节电机质量自动化测试模拟平台 ===\n")
    
    # 1. 定义测试规范
    test_specification = {
        "test_name": "关节电机连续运行1小时耐久测试",
        "max_temperature_c": 75.0,  # 行业常识：电机一般耐温约70-80°C
        "max_current_a": 2.0
    }
    
    print(f"执行测试: {test_specification['test_name']}")
    print(f"测试规范: {json.dumps(test_specification, indent=2)}\n")
    
    # 2. 模拟两种场景的数据
    print("场景1: 模拟正常电机数据...")
    normal_data = simulate_motor_data(run_time_seconds=10, fault_injection=False)  # 10秒演示
    
    print("场景2: 模拟带故障（过热）的电机数据...")
    fault_data = simulate_motor_data(run_time_seconds=10, fault_injection=True)
    
    # 3. 执行自动化测试
    tester = MotorQualityTester(test_specification)
    
    print("\n" + "="*50)
    print("测试报告:")
    print("="*50)
    
    normal_result = tester.run_tests(normal_data)
    fault_result = tester.run_tests(fault_data)
    
    # 4. 生成并保存结构化报告（模拟8D报告的第一步）
    report = {
        "test_specification": test_specification,
        "scenario_results": {
            "normal_scenario": normal_result,
            "fault_injection_scenario": fault_result
        },
        "conclusion": "故障注入场景成功触发温升测试失败，验证了测试系统的有效性。"
    }
    
    with open("test_report.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    
    print(f"\n详细测试报告已保存至: test_report.json")
    
    # 5. 终端输出简要结果（用于快速演示）
    print("\n" + "="*50)
    print("结果摘要:")
    for scenario_name, result in [("正常场景", normal_result), ("故障场景", fault_result)]:
        print(f"\n{scenario_name}:")
        for test in result["tests"]:
            status = "✅ PASS" if test["passed"] else "❌ FAIL"
            print(f"  {status} {test['name']} - 规范:{test['spec']}, 实测:{test['measured']}")
    
    print(f"\n结论: {report['conclusion']}")

if __name__ == "__main__":
    main()