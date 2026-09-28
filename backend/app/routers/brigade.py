"""扑救队伍接口：维护扑救队伍，覆盖下达集结、确认出动、办理归建等动作。"""
from __future__ import annotations

from typing import Any

from fastapi import APIRouter, HTTPException, Query

from app.schemas import ActionResult, EntryPayload, PageResult
from app.services.brigade import BrigadeService

router = APIRouter(prefix="/api/brigade", tags=["扑救队伍"])

service = BrigadeService()

LIST_FIELDS = ["队伍编号", "驻地林场", "队伍人数", "装备配置", "值班队长", "联系方式", "集结时限", "队伍状态"]
STATUSES = ["待集结", "集结中", "已出动", "已归建"]


@router.get("", response_model=PageResult[dict])
def list_entries(
    keyword: str | None = Query(default=None, description="按队伍编号检索"),
    status: str | None = Query(default=None, description="待集结、集结中、已出动、已归建"),
    page: int = 1,
    size: int = 20,
) -> PageResult[dict]:
    """按队伍编号与状态过滤扑救队伍列表；没有数据时返回空页，不报错。"""
    if size > 200:
        raise HTTPException(status_code=400, detail="每页最多 200 条，请缩小分页范围")
    items, total = service.list_entries(keyword=keyword, status=status, page=page, size=size)
    return PageResult(items=items, total=total, page=page, size=size)


@router.get("/{entry_id}", response_model=dict)
def get_entry(entry_id: int) -> dict:
    """读取单条扑救队伍明细；不存在时给出可读的错误说明。"""
    entry = service.get_entry(entry_id)
    if entry is None:
        raise HTTPException(status_code=404, detail=f"扑救队伍 {entry_id} 不存在或已归档")
    return entry


@router.post("", response_model=ActionResult)
def create_entry(payload: EntryPayload) -> ActionResult:
    """登记一条扑救队伍，缺字段时说明原因而不是静默丢弃。"""
    entry, missing = service.create_entry(payload.values)
    if missing:
        return ActionResult(ok=False, message=f"缺少必填字段：{'、'.join(missing)}")
    return ActionResult(ok=True, message="扑救队伍已登记", entry=entry)


@router.post("/{entry_id}/actions", response_model=ActionResult)
def run_action(entry_id: int, payload: EntryPayload) -> ActionResult:
    """对单条扑救队伍执行下达集结、确认出动、办理归建；不允许的动作会被拦下并说明原因。"""
    action = str(payload.values.get("action") or "").strip()
    entry, message = service.run_action(entry_id, action)
    if entry is None:
        return ActionResult(ok=False, message=message)
    return ActionResult(ok=True, message=message, entry=entry)


@router.get("/export")
def export_entries() -> dict[str, Any]:
    """导出扑救队伍清单：返回当前过滤条件下的全量数据。"""
    items, total = service.list_entries(page=1, size=10000)
    return {"module": "brigade", "total": total, "items": items}
