# 🏭 工业设备智能运维 MCP Server

基于 [Model Context Protocol](https://modelcontextprotocol.io/) 构建的工业设备运维管理系统，提供标准化的 MCP 工具接口，为 LLM 应用提供实时设备监控、智能故障诊断和预防性维护管理能力。

## 🌟 核心特性

- ⚡ **实时设备监控** - 即时获取设备运行状态和关键性能指标
- 🔍 **智能故障诊断** - 基于故障代码提供诊断结果和解决方案
- 📅 **维护计划管理** - 自动化的维护提醒和历史记录追踪
- 📊 **多维度数据分析** - 支持温度、振动、功率等多种监测参数
- 🔌 **即插即用** - 标准 MCP 协议，无缝集成 Claude、其他 LLM 和 AI 应用

## 🚀 快速开始

### 环境要求
- Python 3.8+
- pip 包管理器

### 安装依赖
```bash
pip install mcp
```

### 启动服务
```bash
# 默认运行在端口 8000
python main.py

# 或指定自定义端口
PORT=9000 python main.py
```

**服务地址**：`http://127.0.0.1:8000/mcp`（默认）

**配置说明**：
- 通过环境变量 `PORT` 配置服务端口（默认为 8000）

## 🔧 MCP 工具接口

| 工具名称 | 功能描述 | 输入参数 | 输出示例 |
|---------|---------|---------|--------|
| `get_device_status` | 获取设备实时运行状态 | `device_id: str` | `{status, last_checked}` |
| `get_operating_metrics` | 查询设备性能指标 | `device_id: str`<br>`metric: str` | `{value, trend, unit}` |
| `diagnose_fault` | 设备故障智能诊断 | `device_id: str`<br>`fault_code: str` | `{diagnosis, solution}` |
| `maintenance_schedule` | 查询下次维护计划 | `device_id: str` | `{schedule_date, responsible}` |
| `maintenance_history` | 获取维护历史记录 | `device_id: str` | `[{date, maintenance_type}]` |

## 💡 使用场景示例

### 1. 设备状态查询
```json
// 请求
{
  "tool": "get_device_status",
  "params": {"device_id": "D-1001"}
}

// 响应
{
  "device_id": "D-1001",
  "status": "正常",
  "last_checked": "2025-07-15 08:00"
}
```

### 2. 性能指标查询
```json
// 请求
{
  "tool": "get_operating_metrics",
  "params": {"device_id": "D-1001", "metric": "temperature"}
}

// 响应
{
  "device_id": "D-1001",
  "metric": "temperature",
  "value": 75,
  "unit": "°C",
  "trend": "稳定"
}
```

### 3. 故障诊断与解决方案
```json
// 请求
{
  "tool": "diagnose_fault",
  "params": {"device_id": "D-1001", "fault_code": "E101"}
}

// 响应
{
  "fault_code": "E101",
  "diagnosis": "冷却系统可能堵塞",
  "solution": "检查冷却液流量，清洁冷却器"
}
```

## 📐 技术架构

- **框架**：FastMCP 1.20.0 - 轻量级 MCP 实现
- **协议**：Model Context Protocol (MCP) - 标准化的 AI 应用接口
- **数据格式**：JSON - 结构化数据交互
- **传输方式**：Streamable HTTP - 支持流式响应
- **部署模式**：即插即用的 Python 服务

### 支持的性能指标

| 指标类型 | 单位 | 描述 |
|---------|------|------|
| `temperature` | °C | 设备运行温度 |
| `vibration` | mm/s | 机械振动幅度 |
| `power` | W | 实时功率消耗 |

### 常见故障代码参考

| 代码 | 名称 | 影响等级 |
|------|------|--------|
| `E101` | 冷却系统故障 | 🔴 高 |
| `E202` | 振动异常 | 🟡 中 |
| `E303` | 电源电压异常 | 🟡 中 |

## 🚧 发展规划

- [x] 基础 MCP 工具实现
- [x] 环境变量配置支持
- [ ] 实时数据库集成
- [ ] 警告阈值自定义配置
- [ ] 历史数据分析和趋势预测
- [ ] 多租户支持

## 📋 产品状态

当前为 **演示版本**，使用模拟数据和预设规则。生产环境需要集成：
- 实时物联网数据源（如 MQTT、OPC-UA）
- 设备管理系统数据库
- 监控平台 API
- 数据可视化仪表板

## 📖 更多资源

- [MCP Protocol 官方文档](https://modelcontextprotocol.io/)
- [Python MCP SDK](https://github.com/modelcontextprotocol/python-sdk)
- [FastMCP 文档](https://github.com/jlowin/fastmcp)
