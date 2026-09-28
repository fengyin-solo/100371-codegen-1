<template>
  <div class="app-shell">
    <aside class="app-side">
      <h1 class="app-title">森林防火瞭望扑救平台</h1>
      <nav class="nav-list">
        <RouterLink v-for="item in navItems" :key="item.path" :to="item.path" class="nav-item">
          {{ item.label }}
        </RouterLink>
      </nav>
    </aside>
    <main class="app-main">
      <header class="app-head">
        <span class="head-desc">面向林区瞭望塔值守、火情报告核实、扑救队伍调度、火场气象观测与火烧迹地清理的一体化防火指挥后台。</span>
        <span class="head-user">当前值班：{{ store.operator }} · {{ store.shiftLabel }}</span>
      </header>
      <RouterView />
    </main>
  </div>
</template>

<script setup lang="ts">
import { useSessionStore } from '@/stores/session'

const store = useSessionStore()

const navItems = [{ label: "运营概览", path: "/" }, { label: "瞭望塔", path: "/tower" }, { label: "林区网格", path: "/grid" }, { label: "火情报告", path: "/hotspot" }, { label: "扑救队伍", path: "/brigade" }, { label: "扑火物资", path: "/supply" }, { label: "直升机吊桶", path: "/heli" }, { label: "隔离带", path: "/fireline" }, { label: "火场气象", path: "/fireweather" }, { label: "无人机巡查", path: "/drone" }, { label: "防火通道", path: "/road" }, { label: "入山检查站", path: "/checkpoint" }, { label: "防火宣传", path: "/publicity" }, { label: "火烧迹地", path: "/burntarea" }, { label: "扑救复盘", path: "/review" }, { label: "防火期管理", path: "/fireperiod" }, { label: "应急演练", path: "/drill" }, { label: "防火值班", path: "/duty" }, { label: "火险预警", path: "/danger" }]
</script>
