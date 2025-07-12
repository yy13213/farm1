import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from components.layout import create_page_header, create_sensor_status_badge, create_info_panel, create_compact_metric

def show():
    """显示智能微区精细种植管理页面"""
    create_page_header("🌾 智能微区管理", "无人机遥感+微传感器驱动的精细种植管理")
    
    # 创新功能导航
    st.markdown("## 🚀 核心创新功能")
    nav_col1, nav_col2, nav_col3, nav_col4 = st.columns(4)
    
    with nav_col1:
        if st.button("🛩️ 无人机遥感", use_container_width=True, key="drone_sensing"):
            st.session_state.active_mode = "drone"
    
    with nav_col2:
        if st.button("📡 微传感器网", use_container_width=True, key="micro_sensors"):
            st.session_state.active_mode = "sensors"
    
    with nav_col3:
        if st.button("🌱 同田异种", use_container_width=True, key="multi_crop"):
            st.session_state.active_mode = "multi_crop"
    
    with nav_col4:
        if st.button("🎯 精准管理", use_container_width=True, key="precision_mgmt"):
            st.session_state.active_mode = "precision"
    
    # 获取当前模式
    active_mode = st.session_state.get('active_mode', 'multi_crop')
    
    # 地块选择区域
    st.markdown("---")
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # 地块列表 - 增强版
        st.markdown("### 📍 智能地块")
        
        # 模拟增强的地块数据
        plots_data = [
            {
                "id": "P001", "name": "示范地块A", "area": 50, "zones": 8, "status": "同田异种",
                "drone_coverage": 100, "sensor_density": 16, "crop_diversity": 3, "ai_score": 95
            },
            {
                "id": "P002", "name": "试验地块B", "area": 30, "zones": 6, "status": "精准管理",
                "drone_coverage": 95, "sensor_density": 12, "crop_diversity": 2, "ai_score": 88
            },
            {
                "id": "P003", "name": "生产地块C", "area": 80, "zones": 12, "status": "同田异种",
                "drone_coverage": 90, "sensor_density": 24, "crop_diversity": 4, "ai_score": 92
            }
        ]
        
        # 地块选择
        selected_plot = st.selectbox(
            "选择智能地块",
            options=plots_data,
            format_func=lambda x: f"{x['name']} - {x['area']}亩 (AI评分:{x['ai_score']})",
            key="plot_selector"
        )
        
        # 显示增强地块卡片
        for plot in plots_data:
            status_colors = {
                "同田异种": "#28a745", 
                "精准管理": "#17a2b8", 
                "传统管理": "#6c757d"
            }
            status_color = status_colors.get(plot["status"], "#6c757d")
            
            with st.container():
                st.markdown(f"""
                <div style="border: 2px solid {status_color}; border-radius: 10px; 
                           padding: 12px; margin: 8px 0; background: white; font-size: 0.85em;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                        <span style="font-weight: bold; color: #333;">🌾 {plot['name']}</span>
                        <span style="background: {status_color}; color: white; padding: 2px 6px; 
                                     border-radius: 12px; font-size: 0.7em;">{plot['status']}</span>
                    </div>
                    <div style="color: #666; font-size: 0.75em; line-height: 1.4;">
                        📐 面积: {plot['area']}亩 | 🔬 微区: {plot['zones']}个<br>
                        🛩️ 遥感覆盖: {plot['drone_coverage']}% | 📡 传感器: {plot['sensor_density']}个<br>
                        🌱 作物种类: {plot['crop_diversity']}种 | 🤖 AI评分: <strong>{plot['ai_score']}</strong>
                    </div>
                </div>
                """, unsafe_allow_html=True)
    
    with col2:
        if selected_plot:
            # 根据不同模式显示内容
            if active_mode == "drone":
                show_drone_sensing(selected_plot)
            elif active_mode == "sensors":
                show_micro_sensors(selected_plot)
            elif active_mode == "multi_crop":
                show_multi_crop_management(selected_plot)
            else:  # precision
                show_precision_management(selected_plot)


def show_drone_sensing(plot_data):
    """无人机遥感监测模块"""
    st.markdown(f"### 🛩️ {plot_data['name']} - 无人机遥感")
    
    # 遥感数据采集状态
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(create_compact_metric("覆盖率", f"{plot_data['drone_coverage']}%", "#28a745"), unsafe_allow_html=True)
    with col2:
        st.markdown(create_compact_metric("最新飞行", "2小时前", "#17a2b8"), unsafe_allow_html=True)
    with col3:
        st.markdown(create_compact_metric("数据质量", "优秀", "#28a745"), unsafe_allow_html=True)
    
    # 遥感图像分析
    st.markdown("#### 📸 多光谱遥感分析")
    
    tab1, tab2, tab3 = st.tabs(["植被指数", "土壤分析", "病虫害识别"])
    
    with tab1:
        # NDVI植被指数热力图
        st.markdown("**NDVI植被指数分布**")
        
        # 生成模拟NDVI数据
        np.random.seed(42)
        x = np.linspace(0, 100, 20)
        y = np.linspace(0, 80, 16)
        X, Y = np.meshgrid(x, y)
        ndvi_data = 0.3 + 0.5 * np.exp(-((X-50)**2 + (Y-40)**2) / 800) + np.random.normal(0, 0.1, X.shape)
        
        fig_ndvi = go.Figure(data=go.Heatmap(
            z=ndvi_data,
            x=x,
            y=y,
            colorscale='RdYlGn',
            colorbar=dict(title="NDVI值")
        ))
        
        fig_ndvi.update_layout(
            title="植被覆盖度热力图",
            xaxis_title="东西方向(米)",
            yaxis_title="南北方向(米)",
            font=dict(family="SimHei", size=10),
            height=300,
            margin=dict(l=0, r=0, t=30, b=0)
        )
        
        st.plotly_chart(fig_ndvi, use_container_width=True)
        
        # NDVI分析结果
        col_a, col_b = st.columns(2)
        with col_a:
            st.info("🌱 **高NDVI区域** (>0.7)\n适合高产作物种植")
        with col_b:
            st.warning("🟡 **中NDVI区域** (0.4-0.7)\n需要精准施肥管理")
    
    with tab2:
        # 土壤成分分析
        st.markdown("**高光谱土壤成分检测**")
        
        # 土壤成分分布
        soil_zones = pd.DataFrame({
            '微区': [f'Z{i:02d}' for i in range(1, 9)],
            '有机质(%)': np.random.uniform(1.5, 4.2, 8),
            '全氮(g/kg)': np.random.uniform(0.8, 2.1, 8),
            '有效磷(mg/kg)': np.random.uniform(15, 45, 8),
            '速效钾(mg/kg)': np.random.uniform(80, 180, 8),
            '含水率(%)': np.random.uniform(15, 35, 8)
        })
        
        # 土壤养分雷达图
        fig_soil = go.Figure()
        
        for i, zone in enumerate(['Z01', 'Z04', 'Z08']):  # 选择3个代表性微区
            zone_data = soil_zones[soil_zones['微区'] == zone].iloc[0]
            
            fig_soil.add_trace(go.Scatterpolar(
                r=[
                    zone_data['有机质(%)'] * 25,  # 标准化到0-100
                    zone_data['全氮(g/kg)'] * 50,
                    zone_data['有效磷(mg/kg)'] * 2,
                    zone_data['速效钾(mg/kg)'] * 0.6,
                    zone_data['含水率(%)'] * 3
                ],
                theta=['有机质', '全氮', '有效磷', '速效钾', '含水率'],
                fill='toself',
                name=zone,
                line=dict(width=2)
            ))
        
        fig_soil.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
            showlegend=True,
            font=dict(family="SimHei", size=10),
            height=300,
            margin=dict(l=0, r=0, t=20, b=0)
        )
        
        st.plotly_chart(fig_soil, use_container_width=True)
    
    with tab3:
        # AI病虫害识别
        st.markdown("**AI病虫害智能识别**")
        
        col_a, col_b = st.columns(2)
        
        with col_a:
            # 病虫害检测结果
            pest_data = [
                {"区域": "Z02", "类型": "玉米螟", "严重程度": "轻微", "置信度": 92, "建议": "生物防治"},
                {"区域": "Z05", "类型": "蚜虫", "严重程度": "中等", "置信度": 88, "建议": "化学防治"},
                {"区域": "Z07", "类型": "叶斑病", "严重程度": "轻微", "置信度": 95, "建议": "预防为主"}
            ]
            
            for pest in pest_data:
                severity_colors = {"轻微": "green", "中等": "orange", "严重": "red"}
                color = severity_colors[pest["严重程度"]]
                
                st.markdown(f"""
                <div style="border: 1px solid {color}; border-radius: 6px; padding: 8px; margin: 5px 0;">
                    <div style="font-weight: bold; color: {color};">🐛 {pest['类型']} - {pest['区域']}</div>
                    <div style="font-size: 0.8em; color: #666;">
                        严重程度: {pest['严重程度']} | 置信度: {pest['置信度']}%<br>
                        建议: {pest['建议']}
                    </div>
                </div>
                """, unsafe_allow_html=True)
        
        with col_b:
            # 健康度分布饼图
            health_data = {"健康": 70, "轻微异常": 20, "需要关注": 8, "严重问题": 2}
            
            fig_health = px.pie(
                values=list(health_data.values()),
                names=list(health_data.keys()),
                title="地块健康度分布",
                color_discrete_map={
                    "健康": "#28a745",
                    "轻微异常": "#ffc107", 
                    "需要关注": "#fd7e14",
                    "严重问题": "#dc3545"
                }
            )
            
            fig_health.update_layout(
                font=dict(family="SimHei", size=10),
                height=250,
                margin=dict(l=0, r=0, t=30, b=0)
            )
            
            st.plotly_chart(fig_health, use_container_width=True)


def show_micro_sensors(plot_data):
    """微传感器网络监测"""
    st.markdown(f"### 📡 {plot_data['name']} - 微传感器网络")
    
    # 传感器网络状态
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(create_compact_metric("传感器总数", f"{plot_data['sensor_density']}个", "#17a2b8"), unsafe_allow_html=True)
    with col2:
        online_sensors = int(plot_data['sensor_density'] * 0.95)
        st.markdown(create_compact_metric("在线数量", f"{online_sensors}个", "#28a745"), unsafe_allow_html=True)
    with col3:
        st.markdown(create_compact_metric("数据密度", "2米/个", "#6f42c1"), unsafe_allow_html=True)
    with col4:
        st.markdown(create_compact_metric("更新频率", "5分钟", "#fd7e14"), unsafe_allow_html=True)
    
    # 实时传感器数据
    st.markdown("#### 📊 实时环境监测")
    
    # 生成传感器网格数据
    sensor_grid = []
    for i in range(plot_data['zones']):
        for j in range(2):  # 每个微区2个传感器
            sensor_grid.append({
                'sensor_id': f"S{i+1:02d}-{j+1}",
                'zone': f"Z{i+1:02d}",
                'lat': 39.9042 + (i % 4) * 0.0005 + j * 0.0002,
                'lon': 116.4074 + (i // 4) * 0.0005 + j * 0.0002,
                'temperature': round(np.random.normal(20, 2), 1),
                'humidity': round(np.random.normal(65, 5), 1),
                'ph': round(np.random.uniform(6.2, 7.8), 1),
                'salinity': round(np.random.uniform(0.1, 0.6), 2),
                'ec': round(np.random.uniform(0.5, 2.0), 2),
                'status': np.random.choice(['正常', '正常', '正常', '警告'], p=[0.85, 0.1, 0.04, 0.01])
            })
    
    sensor_df = pd.DataFrame(sensor_grid)
    
    # 传感器分布地图
    col_a, col_b = st.columns([3, 2])
    
    with col_a:
        st.markdown("**传感器网络分布**")
        
        # 根据状态设置颜色
        color_map = {'正常': 'green', '警告': 'orange', '异常': 'red'}
        sensor_df['color'] = sensor_df['status'].map(color_map)
        
        fig_sensors = px.scatter_mapbox(
            sensor_df,
            lat='lat',
            lon='lon',
            color='status',
            size='temperature',
            hover_name='sensor_id',
            hover_data=['zone', 'temperature', 'humidity', 'ph'],
            mapbox_style='open-street-map',
            zoom=16,
            height=350,
            color_discrete_map=color_map
        )
        
        fig_sensors.update_layout(
            font=dict(family="SimHei", size=10),
            margin=dict(l=0, r=0, t=20, b=0)
        )
        
        st.plotly_chart(fig_sensors, use_container_width=True)
    
    with col_b:
        st.markdown("**环境参数统计**")
        
        # 环境参数统计
        param_stats = {
            '温度': {'avg': sensor_df['temperature'].mean(), 'std': sensor_df['temperature'].std(), 'unit': '°C'},
            '湿度': {'avg': sensor_df['humidity'].mean(), 'std': sensor_df['humidity'].std(), 'unit': '%'},
            'pH值': {'avg': sensor_df['ph'].mean(), 'std': sensor_df['ph'].std(), 'unit': ''},
            '盐碱度': {'avg': sensor_df['salinity'].mean(), 'std': sensor_df['salinity'].std(), 'unit': '‰'},
            '电导率': {'avg': sensor_df['ec'].mean(), 'std': sensor_df['ec'].std(), 'unit': 'mS/cm'}
        }
        
        for param, stats in param_stats.items():
            avg_val = f"{stats['avg']:.1f}{stats['unit']}"
            std_val = f"±{stats['std']:.1f}"
            st.markdown(f"""
            <div style="background: white; border: 1px solid #ddd; border-radius: 5px; 
                        padding: 8px; margin: 5px 0; font-size: 0.85em;">
                <div style="font-weight: bold; color: #333;">{param}</div>
                <div style="color: #666;">均值: {avg_val} {std_val}</div>
            </div>
            """, unsafe_allow_html=True)
        
        # 异常传感器告警
        st.markdown("**异常告警**")
        abnormal_sensors = sensor_df[sensor_df['status'] != '正常']
        
        if len(abnormal_sensors) > 0:
            for _, sensor in abnormal_sensors.iterrows():
                st.warning(f"⚠️ {sensor['sensor_id']}: {sensor['status']}")
        else:
            st.success("✅ 所有传感器运行正常")
    
    # 数据趋势分析
    st.markdown("#### 📈 历史趋势分析")
    
    # 生成24小时趋势数据
    hours = pd.date_range(start=datetime.now() - timedelta(hours=23), end=datetime.now(), freq='H')
    trend_data = pd.DataFrame({
        'time': hours,
        'avg_temp': np.random.normal(20, 2, len(hours)) + 3 * np.sin(np.arange(len(hours)) * 2 * np.pi / 24),
        'avg_humidity': np.random.normal(65, 3, len(hours)) - 2 * np.sin(np.arange(len(hours)) * 2 * np.pi / 24),
        'avg_ph': np.random.normal(6.8, 0.1, len(hours)),
        'avg_salinity': np.random.normal(0.35, 0.05, len(hours))
    })
    
    # 多参数趋势图
    fig_trend = go.Figure()
    
    fig_trend.add_trace(go.Scatter(
        x=trend_data['time'],
        y=trend_data['avg_temp'],
        mode='lines',
        name='温度(°C)',
        line=dict(color='red', width=2),
        yaxis='y1'
    ))
    
    fig_trend.add_trace(go.Scatter(
        x=trend_data['time'],
        y=trend_data['avg_humidity'],
        mode='lines',
        name='湿度(%)',
        line=dict(color='blue', width=2),
        yaxis='y2'
    ))
    
    fig_trend.update_layout(
        title='24小时环境参数趋势',
        xaxis=dict(title='时间'),
        yaxis=dict(title='温度(°C)', side='left'),
        yaxis2=dict(title='湿度(%)', side='right', overlaying='y'),
        font=dict(family="SimHei", size=10),
        height=300,
        margin=dict(l=0, r=0, t=30, b=0)
    )
    
    st.plotly_chart(fig_trend, use_container_width=True)


def show_multi_crop_management(plot_data):
    """同田异种管理"""
    st.markdown(f"### 🌱 {plot_data['name']} - 同田异种精准管理")
    
    # 微区作物分配状态
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(create_compact_metric("作物种类", f"{plot_data['crop_diversity']}种", "#28a745"), unsafe_allow_html=True)
    with col2:
        st.markdown(create_compact_metric("种植模式", "差异化", "#17a2b8"), unsafe_allow_html=True)
    with col3:
        diversity_index = round(plot_data['crop_diversity'] / plot_data['zones'], 2)
        st.markdown(create_compact_metric("多样性指数", f"{diversity_index}", "#6f42c1"), unsafe_allow_html=True)
    with col4:
        st.markdown(create_compact_metric("预期增产", "+15%", "#fd7e14"), unsafe_allow_html=True)
    
    # 微区作物分配图
    st.markdown("#### 🗺️ 微区作物智能分配")
    
    # 生成微区作物分配数据
    np.random.seed(42)
    crop_allocation = []
    crop_types = ['玉米', '大豆', '向日葵', '小麦']
    crop_colors = {'玉米': '#FFD700', '大豆': '#90EE90', '向日葵': '#FFA500', '小麦': '#F4A460'}
    
    for i in range(plot_data['zones']):
        # 基于土壤条件智能分配作物
        soil_score = np.random.uniform(0.6, 1.0)
        if soil_score > 0.9:
            crop = '玉米'  # 最适合高产作物
        elif soil_score > 0.8:
            crop = '大豆'
        elif soil_score > 0.7:
            crop = '向日葵'
        else:
            crop = '小麦'
        
        crop_allocation.append({
            'zone_id': f"Z{i+1:02d}",
            'crop': crop,
            'variety': f"{crop}_优选品种{np.random.randint(1,4)}",
            'lat': 39.9042 + (i % 4) * 0.0008,
            'lon': 116.4074 + (i // 4) * 0.0008,
            'soil_score': round(soil_score, 2),
            'expected_yield': round(np.random.uniform(400, 800), 0),
            'planting_date': f"3月{15 + i % 15}日",
            'growth_stage': np.random.choice(['播种期', '出苗期', '拔节期', '开花期'])
        })
    
    allocation_df = pd.DataFrame(crop_allocation)
    
    col_a, col_b = st.columns([3, 2])
    
    with col_a:
        # 微区作物分布地图
        fig_allocation = px.scatter_mapbox(
            allocation_df,
            lat='lat',
            lon='lon',
            color='crop',
            size='expected_yield',
            hover_name='zone_id',
            hover_data=['crop', 'variety', 'soil_score', 'expected_yield'],
            mapbox_style='open-street-map',
            zoom=15,
            height=400,
            color_discrete_map=crop_colors,
            title="微区作物智能分配图"
        )
        
        fig_allocation.update_layout(
            font=dict(family="SimHei", size=10),
            margin=dict(l=0, r=0, t=30, b=0)
        )
        
        st.plotly_chart(fig_allocation, use_container_width=True)
    
    with col_b:
        # 作物分配统计
        st.markdown("**作物分配统计**")
        
        crop_stats = allocation_df['crop'].value_counts()
        
        fig_pie = px.pie(
            values=crop_stats.values,
            names=crop_stats.index,
            title="作物面积分配",
            color_discrete_map=crop_colors
        )
        
        fig_pie.update_layout(
            font=dict(family="SimHei", size=10),
            height=200,
            margin=dict(l=0, r=0, t=30, b=0)
        )
        
        st.plotly_chart(fig_pie, use_container_width=True)
        
        # 预期收益对比
        st.markdown("**预期收益分析**")
        
        for crop in crop_types:
            crop_data = allocation_df[allocation_df['crop'] == crop]
            if len(crop_data) > 0:
                avg_yield = crop_data['expected_yield'].mean()
                zone_count = len(crop_data)
                st.markdown(f"""
                <div style="border-left: 3px solid {crop_colors[crop]}; padding: 5px 10px; margin: 3px 0;">
                    <div style="font-weight: bold; font-size: 0.9em;">{crop}</div>
                    <div style="font-size: 0.75em; color: #666;">
                        微区数: {zone_count} | 平均产量: {avg_yield:.0f}kg/亩
                    </div>
                </div>
                """, unsafe_allow_html=True)
    
    # 微区管理详情表
    st.markdown("#### 📋 微区管理详情")
    
    # 增强的微区管理表格
    management_df = allocation_df.copy()
    management_df['管理建议'] = management_df.apply(lambda row: get_management_advice(row), axis=1)
    management_df['投入成本'] = np.random.uniform(600, 1000, len(management_df)).round(0)
    management_df['预期收益'] = (management_df['expected_yield'] * np.random.uniform(2.5, 4.0)).round(0)
    
    display_columns = ['zone_id', 'crop', 'variety', 'growth_stage', 'soil_score', 
                      'expected_yield', '投入成本', '预期收益', '管理建议']
    
    # 重命名列
    display_df = management_df[display_columns].copy()
    display_df.columns = ['微区', '作物', '品种', '生长期', '土壤评分', '预期产量', '投入成本', '预期收益', '管理建议']
    
    st.dataframe(display_df, use_container_width=True, height=200)
    
    # 智能优化建议
    st.markdown("#### 🤖 AI优化建议")
    
    col_1, col_2 = st.columns(2)
    
    with col_1:
        st.success("""
        **🎯 优化策略**
        - Z02、Z06微区土壤条件优秀，建议种植高产玉米
        - Z03、Z07微区适合豆科作物，可提升土壤肥力
        - 建议轮作方案：玉米-大豆-向日葵循环
        """)
        
        st.info("""
        **📊 数据驱动洞察**
        - 当前配置预期增产15%
        - 多样性种植降低风险30%
        - 建议投入传感器密度+20%
        """)
    
    with col_2:
        st.warning("""
        **⚠️ 注意事项**
        - Z05微区盐碱度偏高，需加强改良
        - 相邻作物需考虑病虫害传播
        - 建议设置隔离带防止杂交
        """)
        
        st.markdown("""
        **🔄 动态调整**
        - 根据生长监测数据实时调整
        - 市场价格变化时优化种植结构
        - 气候异常时启动应急预案
        """)


def show_precision_management(plot_data):
    """精准管理模块"""
    st.markdown(f"### 🎯 {plot_data['name']} - 精准管理系统")
    
    # 精准管理指标
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(create_compact_metric("精准度", "98.5%", "#28a745"), unsafe_allow_html=True)
    with col2:
        st.markdown(create_compact_metric("资源利用率", "95.2%", "#17a2b8"), unsafe_allow_html=True)
    with col3:
        st.markdown(create_compact_metric("成本节约", "22%", "#fd7e14"), unsafe_allow_html=True)
    with col4:
        st.markdown(create_compact_metric("环境友好", "A级", "#28a745"), unsafe_allow_html=True)
    
    # 精准作业控制
    st.markdown("#### 🚜 精准作业控制")
    
    tab1, tab2, tab3, tab4 = st.tabs(["变量施肥", "精准灌溉", "智能植保", "收获优化"])
    
    with tab1:
        show_variable_fertilization(plot_data)
    
    with tab2:
        show_precision_irrigation(plot_data)
    
    with tab3:
        show_smart_protection(plot_data)
    
    with tab4:
        show_harvest_optimization(plot_data)


def show_variable_fertilization(plot_data):
    """变量施肥"""
    st.markdown("**🧪 变量施肥处方图**")
    
    # 生成施肥处方数据
    np.random.seed(42)
    fertilizer_map = []
    
    for i in range(plot_data['zones']):
        # 基于土壤检测数据生成施肥处方
        soil_n = np.random.uniform(0.8, 2.1)  # 氮含量
        soil_p = np.random.uniform(15, 45)    # 磷含量
        soil_k = np.random.uniform(80, 180)   # 钾含量
        
        # 计算施肥量（简化算法）
        n_need = max(0, 120 - soil_n * 60)
        p_need = max(0, 80 - soil_p * 2)
        k_need = max(0, 100 - soil_k * 0.6)
        
        fertilizer_map.append({
            'zone': f"Z{i+1:02d}",
            'lat': 39.9042 + (i % 4) * 0.0008,
            'lon': 116.4074 + (i // 4) * 0.0008,
            'nitrogen_kg': round(n_need, 1),
            'phosphorus_kg': round(p_need, 1),
            'potassium_kg': round(k_need, 1),
            'total_cost': round((n_need * 6 + p_need * 8 + k_need * 4), 0)
        })
    
    fertilizer_df = pd.DataFrame(fertilizer_map)
    
    col_a, col_b = st.columns([2, 1])
    
    with col_a:
        # 施肥量分布地图
        fig_fert = px.scatter_mapbox(
            fertilizer_df,
            lat='lat',
            lon='lon',
            size='total_cost',
            color='nitrogen_kg',
            hover_name='zone',
            hover_data=['nitrogen_kg', 'phosphorus_kg', 'potassium_kg', 'total_cost'],
            mapbox_style='open-street-map',
            zoom=15,
            height=300,
            color_continuous_scale='RdYlGn_r',
            title="氮肥需求分布"
        )
        
        fig_fert.update_layout(
            font=dict(family="SimHei", size=10),
            margin=dict(l=0, r=0, t=30, b=0)
        )
        
        st.plotly_chart(fig_fert, use_container_width=True)
    
    with col_b:
        # 施肥统计
        total_n = fertilizer_df['nitrogen_kg'].sum()
        total_p = fertilizer_df['phosphorus_kg'].sum()
        total_k = fertilizer_df['potassium_kg'].sum()
        total_cost = fertilizer_df['total_cost'].sum()
        
        st.markdown(f"""
        **施肥总用量**
        - 氮肥: {total_n:.1f} kg
        - 磷肥: {total_p:.1f} kg  
        - 钾肥: {total_k:.1f} kg
        - 总成本: {total_cost:.0f} 元
        
        **节约效果**
        - 比传统施肥节约: 18%
        - 减少环境污染: 25%
        - 提高利用效率: 22%
        """)


def show_precision_irrigation(plot_data):
    """精准灌溉"""
    st.markdown("**💧 精准灌溉控制**")
    
    # 生成灌溉需求数据
    irrigation_zones = []
    for i in range(plot_data['zones']):
        soil_moisture = np.random.uniform(15, 35)
        target_moisture = 25  # 目标含水量
        
        if soil_moisture < 20:
            irrigation_need = "高"
            water_amount = 30
        elif soil_moisture < 25:
            irrigation_need = "中"
            water_amount = 20
        else:
            irrigation_need = "低"
            water_amount = 10
        
        irrigation_zones.append({
            'zone': f"Z{i+1:02d}",
            'current_moisture': round(soil_moisture, 1),
            'target_moisture': target_moisture,
            'irrigation_need': irrigation_need,
            'water_amount': water_amount,
            'next_irrigation': f"{np.random.randint(1,4)}天后"
        })
    
    irrigation_df = pd.DataFrame(irrigation_zones)
    
    # 灌溉需求表格
    st.dataframe(irrigation_df, use_container_width=True, height=200)
    
    # 灌溉控制按钮
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🚿 启动智能灌溉", use_container_width=True):
            st.success("智能灌溉系统已启动")
    with col2:
        if st.button("⏸️ 暂停灌溉", use_container_width=True):
            st.info("灌溉系统已暂停")
    with col3:
        if st.button("📊 生成灌溉报告", use_container_width=True):
            st.info("正在生成灌溉效果报告...")


def show_smart_protection(plot_data):
    """智能植保"""
    st.markdown("**🛡️ 智能植保方案**")
    
    # 植保监测数据
    protection_data = [
        {"微区": "Z02", "风险": "玉米螟", "预测概率": "15%", "建议措施": "生物防治", "成本": "50元/亩"},
        {"微区": "Z05", "风险": "蚜虫", "预测概率": "25%", "建议措施": "天敌释放", "成本": "30元/亩"},
        {"微区": "Z07", "风险": "叶斑病", "预测概率": "8%", "建议措施": "预防喷药", "成本": "25元/亩"}
    ]
    
    for data in protection_data:
        risk_level = "高" if float(data["预测概率"].rstrip('%')) > 20 else "中" if float(data["预测概率"].rstrip('%')) > 10 else "低"
        color = "#dc3545" if risk_level == "高" else "#ffc107" if risk_level == "中" else "#28a745"
        
        st.markdown(f"""
        <div style="border: 1px solid {color}; border-radius: 8px; padding: 10px; margin: 5px 0;">
            <div style="font-weight: bold; color: {color};">🛡️ {data['微区']} - {data['风险']}</div>
            <div style="font-size: 0.85em; color: #666;">
                预测概率: {data['预测概率']} | 风险等级: {risk_level}<br>
                建议措施: {data['建议措施']} | 预计成本: {data['成本']}
            </div>
        </div>
        """, unsafe_allow_html=True)


def show_harvest_optimization(plot_data):
    """收获优化"""
    st.markdown("**🌾 智能收获优化**")
    
    # 收获成熟度监测
    harvest_data = []
    for i in range(plot_data['zones']):
        maturity = np.random.uniform(70, 95)
        
        if maturity >= 90:
            harvest_status = "可收获"
            harvest_date = "3天内"
        elif maturity >= 85:
            harvest_status = "接近成熟"
            harvest_date = "5-7天"
        else:
            harvest_status = "未成熟"
            harvest_date = "10天以上"
        
        harvest_data.append({
            'zone': f"Z{i+1:02d}",
            'maturity': f"{maturity:.1f}%",
            'status': harvest_status,
            'estimated_date': harvest_date,
            'expected_yield': f"{np.random.uniform(500, 800):.0f}kg/亩"
        })
    
    harvest_df = pd.DataFrame(harvest_data)
    
    # 收获规划表
    st.dataframe(harvest_df, use_container_width=True)
    
    # 收获优化建议
    st.info("""
    **🚜 收获路径优化建议:**
    1. 优先收获Z01、Z03、Z06（成熟度>90%）
    2. 建议收获路径：Z01→Z03→Z06→Z02→Z05
    3. 预计总收获时间：3天，节约燃料15%
    """)


def get_management_advice(row):
    """根据微区数据生成管理建议"""
    crop = row['crop']
    soil_score = row['soil_score']
    stage = row['growth_stage']
    
    if soil_score > 0.9:
        return f"优质土壤，{stage}加强水肥管理"
    elif soil_score > 0.8:
        return f"土壤良好，{stage}常规管理"
    else:
        return f"土壤需改良，{stage}增施有机肥" 