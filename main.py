# https://github.com/modelcontextprotocol/python-sdk
# pip install mcp

from typing import Literal

from mcp.server import MCPServer
from mcp.types import ToolAnnotations

import datetime

# 创建 MCP 服务器实例
mcp = MCPServer(
    name="industrial-mcp",
    version="1.0.0",
    description="工业设备智能运维 MCP Server，提供设备状态、运行指标、故障诊断与维护管理工具",
    instructions="本服务面向工业设备运维场景，所有工具均为只读查询，不改变设备状态。",
)


@mcp.tool(
    description=(
        "查询指定设备的运行状态和基本信息。"
        "适用于「设备在线状态盘点」「快速确认某台设备是否正常」等情境；"
        "若需查看温度/振动/功率等具体运行指标，请改用 get_operating_metrics。"
        "输入 device_id（设备唯一识别码，格式如 D-1001）。"
        "回传设备状态与最后检查时间，唯读操作，不改变任何状态。"
    ),
    annotations=ToolAnnotations(
        read_only_hint=True,
        destructive_hint=False,
        idempotent_hint=True,
        open_world_hint=False,
    ),
)
def get_device_status(
    device_id: str = "D-1001",
) -> dict:
    # 示例数据，实际可接入工业物联网平台API
    return {
        "device_id": device_id,
        "status": "正常",
        "last_checked": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }


@mcp.tool(
    description=(
        "查询指定设备的一项运行指标（温度/振动/功率）。"
        "适用于「读取单一指标当前值」的情境；"
        "若需整体设备状态，请改用 get_device_status。"
        "输入 device_id（格式如 D-1001）与 metric（temperature/vibration/power）。"
        "回传该指标的当前值与趋势，唯读操作。"
    ),
    annotations=ToolAnnotations(
        read_only_hint=True,
        destructive_hint=False,
        idempotent_hint=True,
        open_world_hint=False,
    ),
)
def get_operating_metrics(
    device_id: str = "D-1001",
    metric: Literal["temperature", "vibration", "power"] = "temperature",
) -> dict:
    """获取设备的具体运行指标"""

    metrics = {"temperature": 75, "vibration": 0.02, "power": 1200}
    return {
        "device_id": device_id,
        "metric": metric,
        "value": metrics[metric],
        "trend": "稳定",
    }


@mcp.tool(
    description=(
        "依据故障代码诊断设备故障并给出解决方案建议。"
        "适用于「设备已报出故障代码、需快速定位原因与处置建议」的情境；"
        "输入 device_id（格式如 D-1001）与 fault_code（如 E101/E202/E303）。"
        "回传对应故障的诊断说明，唯读操作，不执行任何修复动作。"
    ),
    annotations=ToolAnnotations(
        read_only_hint=True,
        destructive_hint=False,
        idempotent_hint=True,
        open_world_hint=False,
    ),
)
def diagnose_fault(
    fault_code: Literal["E101", "E202", "E303"],
    device_id: str = "D-1001",
) -> dict:
    suggestions = {
        "E101": "检查冷却系统是否堵塞",
        "E202": "振动过大，建议检修轴承",
        "E303": "电源电压异常，建议检查电源线",
    }
    return {
        "device_id": device_id,
        "fault_code": fault_code,
        "diagnosis": suggestions[fault_code],
    }


@mcp.tool(
    description=(
        "查询指定设备的下次维护计划。"
        "适用于「确认维护排期、维护负责人与备注事项」的情境；"
        "若要查过往维护记录，请改用 maintenance_history。"
        "输入 device_id（格式如 D-1001）。"
        "回传下次维护日期、负责人与备注，唯读操作。"
    ),
    annotations=ToolAnnotations(
        read_only_hint=True,
        destructive_hint=False,
        idempotent_hint=True,
        open_world_hint=False,
    ),
)
def maintenance_schedule(
    device_id: str = "D-1001",
) -> dict:
    return {
        "device_id": device_id,
        "next_maintenance": "2025-08-01",
        "responsible": "张工",
        "notes": "注意润滑油更换",
    }


@mcp.tool(
    description=(
        "查询指定设备的历史维护记录。"
        "适用于「回顾设备过往被维护过哪些项目、由谁执行」的情境；"
        "若要查未来维护排期，请改用 maintenance_schedule。"
        "输入 device_id（格式如 D-1001）。"
        "回传按时间倒序的维护记录列表，唯读操作。"
    ),
    annotations=ToolAnnotations(
        read_only_hint=True,
        destructive_hint=False,
        idempotent_hint=True,
        open_world_hint=False,
    ),
)
def maintenance_history(
    device_id: str = "D-1001",
) -> dict:
    # 模拟的历史数据（实际应从数据库查询）
    history = [
        {"date": "2025-06-01", "engineer": "张工", "content": "更换润滑油"},
        {"date": "2025-05-15", "engineer": "李工", "content": "调整传动轴并清理灰尘"},
    ]
    return {"device_id": device_id, "records": history}


if __name__ == "__main__":
    mcp.run(transport="streamable-http", host="0.0.0.0", port=8000)
