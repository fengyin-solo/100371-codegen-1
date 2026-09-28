"""扑救复盘接口：维护扑救复盘单，覆盖召开复盘、形成报告、归档复盘等动作。"""
from __future__ import annotations

from typing import Any

from fastapi import APIRouter, HTTPException, Query

from app.schemas import ActionResult, EntryPayload, PageResult
from app.services.review import ReviewService

router = APIRouter(prefix="/api/review", tags=["扑救复盘"])

service = ReviewService()

LIST_FIELDS = ["复盘编号", "关联火情", "出动人数", "扑救时长", "主要问题", "复盘会议日", "主持单位", "复盘状态"]
STATUSES = ["待复盘", "复盘中", "已形成报告", "已归档"]


@router.get("", response_model=PageResult[dict])
def list_entries(
    keyword: str | None = Query(default=None, description="按复盘编号检索"),
    status: str | None = Query(default=None, description="待复盘、复盘中、已形成报告、已归档"),
    page: int = 1,
    size: int = 20,
) -> PageResult[dict]:
    """按复盘编号与状态过滤扑救复盘列表；没有数据时返回空页，不报错。"""
    if size > 200:
        raise HTTPException(status_code=400, detail="每页最多 200 条，请缩小分页范围")
    items, total = service.list_entries(keyword=keyword, status=status, page=page, size=size)
    return PageResult(items=items, total=total, page=page, size=size)


@router.get("/{entry_id}", response_model=dict)
def get_entry(entry_id: int) -> dict:
    """读取单条扑救复盘单明细；不存在时给出可读的错误说明。"""
    entry = service.get_entry(entry_id)
    if entry is None:
        raise HTTPException(status_code=404, detail=f"扑救复盘单 {entry_id} 不存在或已归档")
    return entry


@router.post("", response_model=ActionResult)
def create_entry(payload: EntryPayload) -> ActionResult:
    """登记一条扑救复盘单，缺字段时说明原因而不是静默丢弃。"""
    entry, missing = service.create_entry(payload.values)
    if missing:
        return ActionResult(ok=False, message=f"缺少必填字段：{'、'.join(missing)}")
    return ActionResult(ok=True, message="扑救复盘单已登记", entry=entry)


@router.post("/{entry_id}/actions", response_model=ActionResult)
def run_action(entry_id: int, payload: EntryPayload) -> ActionResult:
    """对单条扑救复盘单执行召开复盘、形成报告、归档复盘；不允许的动作会被拦下并说明原因。"""
    action = str(payload.values.get("action") or "").strip()
    entry, message = service.run_action(entry_id, action)
    if entry is None:
        return ActionResult(ok=False, message=message)
    return ActionResult(ok=True, message=message, entry=entry)


@router.get("/export")
def export_entries() -> dict[str, Any]:
    """导出扑救复盘清单：返回当前过滤条件下的全量数据。"""
    items, total = service.list_entries(page=1, size=10000)
    return {"module": "review", "total": total, "items": items}
