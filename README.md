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
- Python 3.10+
- pip 包管理器

### 安装依赖
```bash
pip install -r requirements.txt
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

### 工具标注（ToolAnnotations）

所有工具统一标注以下属性，便于 LLM 准确判断调用安全性：

| 标注 | 值 | 含义 |
|------|------|------|
| `read_only_hint` | `true` | 仅读取，不改变状态 |
| `destructive_hint` | `false` | 非破坏性操作 |
| `idempotent_hint` | `true` | 幂等，重复调用结果一致 |
| `open_world_hint` | `false` | 不与外部世界交互 |

## 💡 使用场景示例

### 1. 设备状态查询
> 用户：查询设备 D-1001 的状态
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
> 用户：D-1001 当前温度是多少？
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
> 用户：设备 D-1001 报故障码 E101 怎么解决？
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

### 4. 维护计划查询
> 用户：D-1001 下次什么时候维护？
```json
// 请求
{
  "tool": "maintenance_schedule",
  "params": {"device_id": "D-1001"}
}

// 响应
{
  "device_id": "D-1001",
  "next_maintenance": "2025-08-01",
  "responsible": "张工",
  "notes": "注意润滑油更换"
}
```

## 📐 技术架构

本项目基于 [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) 的 `MCPServer` 实现，通过 `streamable-http` 传输协议对外提供标准化的 MCP 接口，可无缝集成到支持 MCP 的 LLM 应用中。

服务器实例声明了 `description` 与 `instructions`，便于客户端在握手阶段获取服务能力概览与使用约束。

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
