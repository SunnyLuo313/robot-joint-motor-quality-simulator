import json

class MotorQualityTester:
    def __init__(self, test_spec):
        self.test_spec = test_spec  # 测试规范，例如最大允许温度
        
    def run_tests(self, data_points):
        """执行自动化测试判定"""
        results = {
            "passed": True,
            "tests": [],
            "summary": {}
        }
        
        max_temp = max([d["temperature_c"] for d in data_points])
        avg_current = sum([d["current_a"] for d in data_points]) / len(data_points)
        
        # 测试用例1：温升测试（模拟硬件测试核心）
        temp_passed = max_temp < self.test_spec["max_temperature_c"]
        results["tests"].append({
            "name": "连续运行温升测试",
            "spec": f"最高温度 < {self.test_spec['max_temperature_c']}°C",
            "measured": f"{max_temp:.2f}°C",
            "passed": temp_passed,
            "result": "PASS" if temp_passed else "FAIL"
        })
        
        # 测试用例2：电流稳定性测试
        current_passed = avg_current < self.test_spec["max_current_a"]
        results["tests"].append({
            "name": "平均电流测试",
            "spec": f"平均电流 < {self.test_spec['max_current_a']}A",
            "measured": f"{avg_current:.3f}A",
            "passed": current_passed,
            "result": "PASS" if current_passed else "FAIL"
        })
        
        results["summary"] = {
            "total_tests": len(results["tests"]),
            "passed_tests": sum([1 for t in results["tests"] if t["passed"]]),
            "failed_tests": sum([1 for t in results["tests"] if not t["passed"]])
        }
        results["passed"] = all([t["passed"] for t in results["tests"]])
        
        return results