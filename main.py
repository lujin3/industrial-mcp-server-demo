# https://github.com/modelcontextprotocol/python-sdk

# pip install mcp

from mcp.server.fastmcp import FastMCP
import datetime
from pydantic import Field
from pathlib import Path

# 创建 MCP 服务器实例
mcp = FastMCP(name="indiecloud-mcp", host="0.0.0.0", port=8000, version="1.0.0")


@mcp.tool(description="获取设备状态和基本信息")
def get_device_status(device_id: str = Field(description="设备ID，如 D-1001")) -> dict:
    # 示例数据，实际可接入工业物联网平台API
    return {
        "device_id": device_id,
        "status": "正常",
        "last_checked": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }


@mcp.tool(description="获取设备运行指标数据")
def get_operating_metrics(
    device_id: str = Field(description="设备ID"),
    metric: str = Field(
        description="指标类型: temperature(温度), vibration(振动), power(功率)"
    ),
) -> dict:
    """获取设备的具体运行指标"""

    metrics = {"temperature": 75, "vibration": 0.02, "power": 1200}
    return {
        "device_id": device_id,
        "metric": metric,
        "value": metrics.get(metric, None),
        "trend": "稳定",
    }


@mcp.tool(description="诊断设备故障并提供解决方案")
def diagnose_fault(
    device_id: str = Field(description="设备ID"),
    fault_code: str = Field(description="故障代码，如 E101, E202, E303"),
) -> dict:
    suggestions = {
        "E101": "检查冷却系统是否堵塞",
        "E202": "振动过大，建议检修轴承",
        "E303": "电源电压异常，建议检查电源线",
    }
    return {
        "device_id": device_id,
        "fault_code": fault_code,
        "diagnosis": suggestions.get(fault_code, "未知故障，请联系工程师"),
    }


@mcp.tool(description="查询设备维护计划")
def maintenance_schedule(
    device_id: str = Field(description="设备ID"),
) -> dict:
    return {
        "device_id": device_id,
        "next_maintenance": "2025-08-01",
        "responsible": "张工",
        "notes": "注意润滑油更换",
    }


@mcp.tool(description="查询设备历史维护记录")
def maintenance_history(
    device_id: str = Field(description="设备ID"),
) -> dict:
    # 模拟的历史数据（实际应从数据库查询）
    history = [
        {"date": "2025-06-01", "engineer": "张工", "content": "更换润滑油"},
        {"date": "2025-05-15", "engineer": "李工", "content": "调整传动轴并清理灰尘"},
    ]
    return {"device_id": device_id, "records": history}


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
