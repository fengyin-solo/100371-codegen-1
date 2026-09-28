"""业务模块路由汇总。

这里统一按别名导入再暴露 ROUTERS：模块名有可能和内置名撞车（某个业务模块就叫 dict、list
这种名字时），按名字直接 import 会把内置类型覆盖掉，函数注解在运行时求值就会报
'module' object is not subscriptable。
"""
from __future__ import annotations

from app.routers import tower as router_tower
from app.routers import grid as router_grid
from app.routers import hotspot as router_hotspot
from app.routers import brigade as router_brigade
from app.routers import supply as router_supply
from app.routers import heli as router_heli
from app.routers import fireline as router_fireline
from app.routers import fireweather as router_fireweather
from app.routers import drone as router_drone
from app.routers import road as router_road
from app.routers import checkpoint as router_checkpoint
from app.routers import publicity as router_publicity
from app.routers import burntarea as router_burntarea
from app.routers import review as router_review
from app.routers import fireperiod as router_fireperiod
from app.routers import drill as router_drill
from app.routers import duty as router_duty
from app.routers import danger as router_danger

ROUTERS = [router_tower, router_grid, router_hotspot, router_brigade, router_supply, router_heli, router_fireline, router_fireweather, router_drone, router_road, router_checkpoint, router_publicity, router_burntarea, router_review, router_fireperiod, router_drill, router_duty, router_danger]
