# 森林防火瞭望扑救平台

面向林区瞭望塔值守、火情报告核实、扑救队伍调度、火场气象观测与火烧迹地清理的一体化防火指挥后台。

这是一个前后端分离的管理平台：前端 Vue 3 + Vite + TypeScript，后端 FastAPI（Python）。
两边各自独立启动，前端 dev server 已关掉自动打开页面，启动后按终端打印的地址手工打开。

## 目录结构

```text
.
├── frontend/                 Vue 3 + Vite + TypeScript 前端
│   ├── src/views/            每个业务模块一个页面
│   ├── src/api/              统一请求封装
│   ├── src/stores/           会话与筛选状态
│   └── vite.config.ts        dev server 配置（open: false）
├── backend/                  FastAPI（Python） 后端
│   ├── app/routers/          每个业务模块一组接口
│   ├── app/services/         业务规则与状态流转
│   └── app/store.py          内存数据仓库与示例数据
├── .gitignore
└── docker-compose.yml
```

## 启动

### 后端

```bash
cd backend
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
./run.sh
```

健康检查：`curl http://127.0.0.1:8000/api/health`

### 前端

```bash
cd frontend
npm install
npm run dev
```

前端默认监听 `http://127.0.0.1:5173/`，dev server 不会自动打开浏览器，
需要自己访问。`/api` 由 vite 代理到后端 `http://127.0.0.1:8000`。

## 业务模块

| 模块 | 目录 | 业务对象 | 主要字段 |
| --- | --- | --- | --- |
| 瞭望塔 | `tower` | 瞭望塔 | 塔号、所在林场、塔架高度 |
| 林区网格 | `grid` | 林区网格 | 网格编号、所属林场、网格面积 |
| 火情报告 | `hotspot` | 火情报告单 | 报告编号、发现方式、发现时间 |
| 扑救队伍 | `brigade` | 扑救队伍 | 队伍编号、驻地林场、队伍人数 |
| 扑火物资 | `supply` | 扑火物资 | 物资编号、物资名称、规格型号 |
| 直升机吊桶 | `heli` | 吊桶飞行架次 | 架次编号、机型、起降场 |
| 隔离带 | `fireline` | 隔离带 | 隔离带编号、所在网格、开设长度 |
| 火场气象 | `fireweather` | 火场气象观测 | 观测编号、观测点位、风速 |
| 无人机巡查 | `drone` | 无人机巡查架次 | 巡查编号、机型、航线编号 |
| 防火通道 | `road` | 防火通道 | 通道编号、所在林场、通道长度 |
| 入山检查站 | `checkpoint` | 入山检查站 | 站点编号、所在林场、值守人数 |
| 防火宣传 | `publicity` | 防火宣传活动 | 宣传编号、宣传形式、覆盖村屯 |
| 火烧迹地 | `burntarea` | 火烧迹地 | 迹地编号、所属网格、过火面积 |
| 扑救复盘 | `review` | 扑救复盘单 | 复盘编号、关联火情、出动人数 |
| 防火期管理 | `fireperiod` | 防火期 | 期次编号、防火期名称、起始日期 |
| 应急演练 | `drill` | 应急演练 | 演练编号、演练科目、参演队伍 |
| 防火值班 | `duty` | 防火值班单 | 值班编号、值班日期、值班班组 |
| 火险预警 | `danger` | 火险预警 | 预警编号、预警区域、预警等级 |

## 约定

- 每个模块的前端页面在 `frontend/src/views/<模块>/index.vue`，后端接口在
  `backend/app/routers/<模块>.py`，业务规则在 `backend/app/services/<模块>.py`。
- 列表接口统一返回 `{ items, total, page, size }`，动作接口统一返回 `{ ok, message }`。
- 状态流转只允许在 `app/services` 里改，路由层不做业务判断。
