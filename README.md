# 🎯 Demo 场景名称：工业设备智能运维 MCP Server

## 场景背景
现代工厂依赖大量工业设备，实时监控和维护对保证生产效率至关重要。利用 MCP 协议，构建一套可被 LLM 调用的设备运维工具，帮助实现：
- 设备状态查询
- 运行指标获取
- 故障诊断建议
- 维护计划提醒
- 设备历史维护记录

## 功能设计
1. 设备状态查询（工具名：get_device_status）
    - 输入参数：设备 ID
    - 返回设备当前运行状态（正常、异常、维护中）及基本信息

2. 运行指标获取（工具名：get_operating_metrics）
    - 输入参数：设备 ID，指标类型（温度、振动、功率等）
    - 返回设备该指标的最新数值及趋势分析简报

3. 故障诊断建议（工具名：diagnose_fault）
    - 输入参数：设备 ID，故障代码或描述
    - 返回对应的诊断结果和解决建议

4. 维护计划提醒（工具名：maintenance_schedule）
    - 输入参数：设备 ID
    - 返回下次维护时间、负责人和注意事项

5. 设备历史维护记录 (工具名: maintenance_history)
    - 输入参数: 设备 ID
    - 返回设备的历史维护记录

## 用户交互示例
| 用户提问              | 调用工具                    | 返回示例                                                                                          |
| ----------------- | ----------------------- | --------------------------------------------------------------------------------------------- |
| 查询设备编号为D-1001的状态？ | `get_device_status`     | {"device\_id":"D-1001","status":"正常","last\_checked":"2025-07-15 08:00"}                      |
| 获取设备D-1001的温度是多少？ | `get_operating_metrics` | {"device\_id":"D-1001","metric":"temperature","value":75,"trend":"稳定"}                        |
| 故障码E101的解决方案？     | `diagnose_fault`        | {"device\_id":"D-1001","fault\_code":"E101","diagnosis":"检查冷却系统是否堵塞"}                         |
| 设备D-1001下次维护时间？   | `maintenance_schedule`  | {"device\_id":"D-1001","next\_maintenance":"2025-08-01","responsible":"张工","notes":"注意润滑油更换"} |
| 设备D-1001维护记录？   | `maintenance_history`  | [ {"date": "2025-06-01", "engineer": "张工", "content": "更换润滑油"},{"date": "2025-05-15", "engineer": "李工", "content": "调整传动轴并清理灰尘"}]|



## 使用
 ```python
    python main.py
 ```
 连接地址: `http://127.0.0.1:8000/mcp`