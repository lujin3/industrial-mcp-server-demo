# 🎯 工业设备智能运维 MCP Server

基于 MCP 协议构建的工业设备运维管理系统，为 LLM 提供设备监控、故障诊断和维护管理工具。

## 🚀 快速开始

### 安装依赖
```bash
pip install mcp
```

### 启动服务
```bash
python main.py
```

服务地址：`http://127.0.0.1:8000/mcp`

## 📋 功能特性

- **实时设备监控** - 查询设备运行状态和关键指标
- **智能故障诊断** - 基于故障代码提供解决方案
- **维护计划管理** - 自动提醒和历史记录追踪
- **多指标监测** - 支持温度、振动、功率等多种参数

## 🔧 API 工具

| 工具名称 | 功能描述 | 参数 | 返回值 |
|---------|---------|------|--------|
| `get_device_status` | 获取设备运行状态 | `device_id` | 状态、最后检查时间 |
| `get_operating_metrics` | 查询运行指标 | `device_id`, `metric` | 指标值、趋势分析 |
| `diagnose_fault` | 故障诊断建议 | `device_id`, `fault_code` | 诊断结果、解决方案 |
| `maintenance_schedule` | 维护计划查询 | `device_id` | 下次维护时间、负责人 |
| `maintenance_history` | 历史维护记录 | `device_id` | 维护记录列表 |

## 💬 使用示例

**查询设备状态**
```
用户：查询设备D-1001的状态
返回：{"device_id":"D-1001","status":"正常","last_checked":"2025-07-15 08:00"}
```

**获取运行指标**
```
用户：D-1001的温度是多少？
返回：{"device_id":"D-1001","metric":"temperature","value":75,"trend":"稳定"}
```

**故障诊断**
```
用户：故障码E101怎么解决？
返回：{"fault_code":"E101","diagnosis":"检查冷却系统是否堵塞"}
```

## 🏗️ 架构说明

本项目基于 [MCP SDK](https://github.com/modelcontextprotocol/python-sdk) 框架，提供标准化的 MCP 协议接口，可无缝集成到支持 MCP 的 LLM 应用中。

### 支持的指标类型
- `temperature` - 设备温度 (°C)
- `vibration` - 振动幅度 (mm/s)
- `power` - 功率消耗 (W)

### 常见故障代码
- `E101` - 冷却系统故障
- `E202` - 振动异常
- `E303` - 电源电压异常

## 📝 开发说明

当前为演示版本，使用模拟数据。生产环境可接入：
- 工业物联网平台 API
- 设备管理系统数据库
- 实时监控数据流
