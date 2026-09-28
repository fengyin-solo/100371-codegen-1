"""接口出入参模型：列表分页、动作结果与各模块的明细结构。"""
from __future__ import annotations

from typing import Any, Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class PageResult(BaseModel, Generic[T]):
    items: list[T]
    total: int
    page: int = 1
    size: int = 20


class ActionResult(BaseModel):
    ok: bool
    message: str
    entry: dict[str, Any] | None = None


class EntryPayload(BaseModel):
    """登记或修改一条业务记录时提交的字段集合。"""

    values: dict[str, Any] = Field(default_factory=dict)
    remark: str | None = None



class TowerEntry(BaseModel):
    """瞭望塔明细结构。"""

    field_0: str | None = None  # 塔号
    field_1: str | None = None  # 所在林场
    field_2: str | None = None  # 塔架高度
    field_3: str | None = None  # 视野半径
    field_4: str | None = None  # 值守班组
    field_5: str | None = None  # 瞭望设备
    field_6: str | None = None  # 上次巡查日
    field_7: str | None = None  # 塔台状态

class GridEntry(BaseModel):
    """林区网格明细结构。"""

    field_0: str | None = None  # 网格编号
    field_1: str | None = None  # 所属林场
    field_2: str | None = None  # 网格面积
    field_3: str | None = None  # 主要树种
    field_4: str | None = None  # 可燃物载量
    field_5: str | None = None  # 责任护林员
    field_6: str | None = None  # 火险等级
    field_7: str | None = None  # 网格状态

class HotspotEntry(BaseModel):
    """火情报告单明细结构。"""

    field_0: str | None = None  # 报告编号
    field_1: str | None = None  # 发现方式
    field_2: str | None = None  # 发现时间
    field_3: str | None = None  # 经纬度
    field_4: str | None = None  # 初判火势
    field_5: str | None = None  # 报告人
    field_6: str | None = None  # 所属网格
    field_7: str | None = None  # 报告状态

class BrigadeEntry(BaseModel):
    """扑救队伍明细结构。"""

    field_0: str | None = None  # 队伍编号
    field_1: str | None = None  # 驻地林场
    field_2: str | None = None  # 队伍人数
    field_3: str | None = None  # 装备配置
    field_4: str | None = None  # 值班队长
    field_5: str | None = None  # 联系方式
    field_6: str | None = None  # 集结时限
    field_7: str | None = None  # 队伍状态

class SupplyEntry(BaseModel):
    """扑火物资明细结构。"""

    field_0: str | None = None  # 物资编号
    field_1: str | None = None  # 物资名称
    field_2: str | None = None  # 规格型号
    field_3: str | None = None  # 存放地点
    field_4: str | None = None  # 现有数量
    field_5: str | None = None  # 责任保管员
    field_6: str | None = None  # 上次盘点日
    field_7: str | None = None  # 物资状态

class HeliEntry(BaseModel):
    """吊桶飞行架次明细结构。"""

    field_0: str | None = None  # 架次编号
    field_1: str | None = None  # 机型
    field_2: str | None = None  # 起降场
    field_3: str | None = None  # 吊桶容量
    field_4: str | None = None  # 飞行时长
    field_5: str | None = None  # 机组负责人
    field_6: str | None = None  # 作业日期
    field_7: str | None = None  # 架次状态

class FirelineEntry(BaseModel):
    """隔离带明细结构。"""

    field_0: str | None = None  # 隔离带编号
    field_1: str | None = None  # 所在网格
    field_2: str | None = None  # 开设长度
    field_3: str | None = None  # 开设宽度
    field_4: str | None = None  # 开设方式
    field_5: str | None = None  # 开设班组
    field_6: str | None = None  # 完成日期
    field_7: str | None = None  # 隔离带状态

class FireweatherEntry(BaseModel):
    """火场气象观测明细结构。"""

    field_0: str | None = None  # 观测编号
    field_1: str | None = None  # 观测点位
    field_2: str | None = None  # 风速
    field_3: str | None = None  # 风向
    field_4: str | None = None  # 相对湿度
    field_5: str | None = None  # 气温
    field_6: str | None = None  # 观测时间
    field_7: str | None = None  # 观测状态

class DroneEntry(BaseModel):
    """无人机巡查架次明细结构。"""

    field_0: str | None = None  # 巡查编号
    field_1: str | None = None  # 机型
    field_2: str | None = None  # 航线编号
    field_3: str | None = None  # 飞行高度
    field_4: str | None = None  # 续航时长
    field_5: str | None = None  # 操作员
    field_6: str | None = None  # 巡查日期
    field_7: str | None = None  # 巡查状态

class RoadEntry(BaseModel):
    """防火通道明细结构。"""

    field_0: str | None = None  # 通道编号
    field_1: str | None = None  # 所在林场
    field_2: str | None = None  # 通道长度
    field_3: str | None = None  # 路面宽度
    field_4: str | None = None  # 通行等级
    field_5: str | None = None  # 养护班组
    field_6: str | None = None  # 上次巡护日
    field_7: str | None = None  # 通道状态

class CheckpointEntry(BaseModel):
    """入山检查站明细结构。"""

    field_0: str | None = None  # 站点编号
    field_1: str | None = None  # 所在林场
    field_2: str | None = None  # 值守人数
    field_3: str | None = None  # 登记方式
    field_4: str | None = None  # 火种收缴数
    field_5: str | None = None  # 值守班长
    field_6: str | None = None  # 检查日期
    field_7: str | None = None  # 站点状态

class PublicityEntry(BaseModel):
    """防火宣传活动明细结构。"""

    field_0: str | None = None  # 宣传编号
    field_1: str | None = None  # 宣传形式
    field_2: str | None = None  # 覆盖村屯
    field_3: str | None = None  # 宣传日期
    field_4: str | None = None  # 发放材料数
    field_5: str | None = None  # 宣传员
    field_6: str | None = None  # 责任林场
    field_7: str | None = None  # 宣传状态

class BurntareaEntry(BaseModel):
    """火烧迹地明细结构。"""

    field_0: str | None = None  # 迹地编号
    field_1: str | None = None  # 所属网格
    field_2: str | None = None  # 过火面积
    field_3: str | None = None  # 林木损失
    field_4: str | None = None  # 清理方式
    field_5: str | None = None  # 清理班组
    field_6: str | None = None  # 清理期限
    field_7: str | None = None  # 迹地状态

class ReviewEntry(BaseModel):
    """扑救复盘单明细结构。"""

    field_0: str | None = None  # 复盘编号
    field_1: str | None = None  # 关联火情
    field_2: str | None = None  # 出动人数
    field_3: str | None = None  # 扑救时长
    field_4: str | None = None  # 主要问题
    field_5: str | None = None  # 复盘会议日
    field_6: str | None = None  # 主持单位
    field_7: str | None = None  # 复盘状态

class FireperiodEntry(BaseModel):
    """防火期明细结构。"""

    field_0: str | None = None  # 期次编号
    field_1: str | None = None  # 防火期名称
    field_2: str | None = None  # 起始日期
    field_3: str | None = None  # 结束日期
    field_4: str | None = None  # 禁火等级
    field_5: str | None = None  # 发布单位
    field_6: str | None = None  # 值守要求
    field_7: str | None = None  # 期次状态

class DrillEntry(BaseModel):
    """应急演练明细结构。"""

    field_0: str | None = None  # 演练编号
    field_1: str | None = None  # 演练科目
    field_2: str | None = None  # 参演队伍
    field_3: str | None = None  # 演练地点
    field_4: str | None = None  # 计划日期
    field_5: str | None = None  # 演练指挥
    field_6: str | None = None  # 评估结论
    field_7: str | None = None  # 演练状态

class DutyEntry(BaseModel):
    """防火值班单明细结构。"""

    field_0: str | None = None  # 值班编号
    field_1: str | None = None  # 值班日期
    field_2: str | None = None  # 值班班组
    field_3: str | None = None  # 带班领导
    field_4: str | None = None  # 值班电话
    field_5: str | None = None  # 交接事项
    field_6: str | None = None  # 交接时间
    field_7: str | None = None  # 值班状态

class DangerEntry(BaseModel):
    """火险预警明细结构。"""

    field_0: str | None = None  # 预警编号
    field_1: str | None = None  # 预警区域
    field_2: str | None = None  # 预警等级
    field_3: str | None = None  # 发布依据
    field_4: str | None = None  # 发布人
    field_5: str | None = None  # 发布时间
    field_6: str | None = None  # 解除时间
    field_7: str | None = None  # 预警状态
