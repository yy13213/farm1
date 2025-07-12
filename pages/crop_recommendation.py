import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from components.layout import create_page_header, create_recommendation_card, create_sensor_status_badge, create_compact_metric
from utils.constants import PLANTING_SEASONS, RISK_PREFERENCES, TARGET_USES, SENSOR_CONFIG

def show():
    """显示作物推荐页面"""
    create_page_header("🌾 智能作物推荐", "AI驱动的精准作物推荐与种植方案")
    
    # 主要布局：左右分栏
    left_col, right_col = st.columns([1, 2])
    
    with left_col:
        show_configuration_panel()
    
    with right_col:
        show_recommendation_results()


def show_configuration_panel():
    """左侧配置面板"""
    st.markdown("### ⚙️ 推荐配置")
    
    # 基本推荐设置
    with st.container():
        st.markdown("#### 📋 基本设置")
        
        # 地块选择
        plot_options = [
            "示范地块A (50亩) - 优质土壤",
            "试验地块B (30亩) - 中等土壤", 
            "生产地块C (80亩) - 盐碱土壤",
            "新开发地块D (45亩) - 改良土壤"
        ]
        selected_plot = st.selectbox("🌾 选择地块", plot_options)
        
        # 种植参数
        season = st.selectbox("🗓️ 种植季节", PLANTING_SEASONS)
        target_use = st.selectbox("🎯 种植目标", TARGET_USES)
        risk_preference = st.selectbox("📊 风险偏好", RISK_PREFERENCES)
        
        # 投资预算
        budget = st.slider("💰 投资预算(元/亩)", min_value=500, max_value=5000, value=1500, step=100)
        
        # 期望产量
        expected_yield = st.selectbox("📈 期望产量水平", ["高产优先", "稳产优先", "成本优先"])
    
    # 传感器配置
    st.markdown("#### 📡 传感器配置")
    
    with st.container():
        # 传感器基本设置
        sensor_id = st.text_input("传感器ID", value="S001-A1", placeholder="例：S001-A1")
        sensor_type = st.selectbox("设备类型", SENSOR_CONFIG["supported_types"])
        
        # 数据获取方式
        data_mode = st.radio("数据获取方式", ["📡 自动获取", "✏️ 手动输入"], horizontal=True)
        
        if "自动获取" in data_mode:
            # 自动获取模式
            st.success("🔄 自动从传感器网络获取实时数据")
            
            # 传感器状态
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(create_compact_metric("在线状态", "正常", "#28a745"), unsafe_allow_html=True)
            with col2:
                st.markdown(create_compact_metric("更新时间", "30秒前", "#17a2b8"), unsafe_allow_html=True)
            
            # 实时数据同步
            if st.button("🔄 立即同步数据", use_container_width=True):
                with st.spinner("正在同步传感器数据..."):
                    st.session_state.sensor_synced = True
                st.success("✅ 数据同步完成")
                st.rerun()
            
            # 显示当前传感器读数
            show_sensor_readings()
        
        else:
            # 手动输入模式
            st.info("📝 手动输入环境参数")
            show_manual_input()
    
    # 推荐执行按钮
    st.markdown("#### 🚀 生成推荐")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🔍 验证数据", use_container_width=True):
            validate_configuration()
    
    with col2:
        if st.button("🌱 智能推荐", use_container_width=True, type="primary"):
            generate_recommendations()


def show_sensor_readings():
    """显示传感器实时读数"""
    st.markdown("**📊 实时环境数据**")
    
    # 模拟传感器数据
    sensor_data = {
        "温度": {"value": 18.5, "unit": "°C", "status": "正常"},
        "湿度": {"value": 65.2, "unit": "%", "status": "正常"},
        "pH值": {"value": 6.8, "unit": "", "status": "偏碱"},
        "盐碱度": {"value": 0.35, "unit": "‰", "status": "轻微"},
        "氮含量": {"value": 45.2, "unit": "mg/kg", "status": "中等"},
        "磷含量": {"value": 28.1, "unit": "mg/kg", "status": "充足"},
        "钾含量": {"value": 156.8, "unit": "mg/kg", "status": "丰富"},
        "有机质": {"value": 2.8, "unit": "%", "status": "良好"}
    }
    
    # 显示传感器数据
    for param, data in sensor_data.items():
        status_color = "#28a745" if data["status"] == "正常" else "#ffc107" if "轻微" in data["status"] or "中等" in data["status"] else "#17a2b8"
        
        st.markdown(f"""
        <div style="border: 1px solid {status_color}; border-radius: 5px; padding: 6px; margin: 3px 0; font-size: 0.85em;">
            <div style="display: flex; justify-content: space-between;">
                <span style="font-weight: bold;">{param}</span>
                <span style="color: {status_color};">{data['status']}</span>
            </div>
            <div style="color: #333; font-size: 1.1em; font-weight: bold;">
                {data['value']}{data['unit']}
            </div>
        </div>
        """, unsafe_allow_html=True)


def show_manual_input():
    """显示手动输入界面"""
    # 基础环境参数
    temperature = st.number_input("🌡️ 温度 (°C)", min_value=-20.0, max_value=50.0, value=18.5, step=0.1)
    humidity = st.number_input("💧 湿度 (%)", min_value=0.0, max_value=100.0, value=65.2, step=0.1)
    ph_value = st.number_input("⚗️ pH值", min_value=3.0, max_value=12.0, value=6.8, step=0.1)
    salinity = st.number_input("🧂 盐碱度 (‰)", min_value=0.0, max_value=2.0, value=0.35, step=0.01)
    
    # 土壤养分参数
    st.markdown("**土壤养分**")
    nitrogen = st.number_input("🟢 氮含量 (mg/kg)", min_value=0.0, max_value=300.0, value=45.2, step=1.0)
    phosphorus = st.number_input("🔵 磷含量 (mg/kg)", min_value=0.0, max_value=100.0, value=28.1, step=1.0)
    potassium = st.number_input("🟡 钾含量 (mg/kg)", min_value=0.0, max_value=300.0, value=156.8, step=1.0)
    organic_matter = st.number_input("🟤 有机质 (%)", min_value=0.0, max_value=10.0, value=2.8, step=0.1)


def validate_configuration():
    """验证配置数据"""
    with st.spinner("正在验证配置数据..."):
        # 模拟验证过程
        import time
        time.sleep(1)
    
    st.success("✅ 配置数据验证通过")
    st.session_state.config_validated = True


def generate_recommendations():
    """生成作物推荐"""
    with st.spinner("AI正在分析环境数据，生成智能推荐..."):
        # 模拟AI分析过程
        import time
        time.sleep(2)
    
    st.success("🌱 智能推荐已生成")
    st.session_state.recommendations_ready = True
    st.rerun()


def show_recommendation_results():
    """右侧推荐结果面板"""
    if not st.session_state.get('recommendations_ready', False):
        # 显示等待状态
        st.markdown("### 🤖 AI智能推荐系统")
        st.info("👈 请先在左侧完成推荐配置，然后点击\"智能推荐\"按钮")
        
        # 显示推荐系统介绍
        st.markdown("""
        #### 🌟 推荐系统特色
        
        **🧠 AI智能分析**
        - 多维度环境数据融合分析
        - 深度学习作物适应性评估
        - 历史数据与实时监测结合
        
        **🎯 精准推荐**
        - 作物品种精确匹配
        - 个性化种植方案
        - 风险评估与收益预测
        
        **🌱 同田异种管理**
        - 微区差异化种植
        - 多作物轮作优化
        - 生态协调发展
        """)
        return
    
    # 显示推荐结果
    st.markdown("### 🌱 智能推荐结果")
    
    # 顶部推荐作物卡片
    show_top_recommendations()
    
    # 详细推荐信息
    st.markdown("### 📋 详细推荐方案")
    
    # 推荐作物选择
    selected_crop_tab = st.selectbox(
        "选择查看详细方案", 
        ["🌽 玉米 - 郑单958", "🌿 大豆 - 东农42", "🌻 向日葵 - 三瑞3号"],
        key="crop_detail_selector"
    )
    
    # 根据选择显示详细方案
    crop_name = selected_crop_tab.split(" - ")[0].replace("🌽 ", "").replace("🌿 ", "").replace("🌻 ", "")
    show_detailed_crop_plan(crop_name)


def show_top_recommendations():
    """显示顶部推荐作物卡片"""
    # 推荐作物数据
    recommendations = [
        {
            "name": "玉米", "variety": "郑单958", "emoji": "🌽",
            "suitability": 95, "profit": 88, "risk": 12,
            "yield": "650kg/亩", "revenue": "1600元/亩",
            "image": "https://images.unsplash.com/photo-1551754655-cd27e38d2076?w=200&h=150&fit=crop",
            "description": "高产优质玉米品种，适应性强"
        },
        {
            "name": "大豆", "variety": "东农42", "emoji": "🌿", 
            "suitability": 88, "profit": 78, "risk": 22,
            "yield": "280kg/亩", "revenue": "1250元/亩",
            "image": "https://images.unsplash.com/photo-1605030753481-bb38b08c384a?w=200&h=150&fit=crop",
            "description": "优质高蛋白大豆，市场需求稳定"
        },
        {
            "name": "向日葵", "variety": "三瑞3号", "emoji": "🌻",
            "suitability": 82, "profit": 72, "risk": 28,
            "yield": "320kg/亩", "revenue": "1150元/亩", 
            "image": "https://images.unsplash.com/photo-1508296695146-257a814070b4?w=200&h=150&fit=crop",
            "description": "耐盐碱向日葵品种，油脂含量高"
        }
    ]
    
    # 显示推荐卡片
    col1, col2, col3 = st.columns(3)
    
    for i, crop in enumerate(recommendations):
        with [col1, col2, col3][i]:
            # 获取适应性等级颜色
            if crop["suitability"] >= 90:
                suitability_color = "#28a745"
                suitability_text = "非常适合"
            elif crop["suitability"] >= 80:
                suitability_color = "#17a2b8"
                suitability_text = "比较适合"
            else:
                suitability_color = "#ffc107"
                suitability_text = "一般适合"
            
            st.markdown(f"""
            <div style="border: 2px solid {suitability_color}; border-radius: 15px; 
                        padding: 15px; margin: 8px 0; background: white; text-align: center;">
                <div style="font-size: 3em; margin-bottom: 10px;">{crop['emoji']}</div>
                <div style="font-size: 1.2em; font-weight: bold; color: #333; margin-bottom: 5px;">
                    {crop['name']} - {crop['variety']}
                </div>
                <div style="font-size: 0.85em; color: #666; margin-bottom: 10px;">
                    {crop['description']}
                </div>
                <div style="background: {suitability_color}; color: white; padding: 5px 10px; 
                           border-radius: 20px; font-size: 0.9em; margin: 5px 0;">
                    适应性: {crop['suitability']}% - {suitability_text}
                </div>
                <div style="font-size: 0.8em; color: #333; margin-top: 8px;">
                    📊 预期产量: {crop['yield']}<br>
                    💰 预期收益: {crop['revenue']}<br>
                    ⚠️ 风险指数: {crop['risk']}%
                </div>
            </div>
            """, unsafe_allow_html=True)


def show_detailed_crop_plan(crop_name):
    """显示详细的作物种植方案"""
    # 根据作物类型设置详细信息
    crop_details = {
        "玉米": {
            "emoji": "🌽",
            "variety": "郑单958",
            "image": "https://images.unsplash.com/photo-1551754655-cd27e38d2076?w=300&h=200&fit=crop",
            "reasons": [
                "🌡️ 当前温湿度条件最适合玉米生长（18.5°C, 65.2%湿度）",
                "🌱 土壤pH值6.8接近玉米最适范围（6.0-7.5）",
                "💧 土壤养分充足，氮磷钾配比合理",
                "📈 市场价格稳定，收益预期良好",
                "🛡️ 抗逆性强，适应本地气候条件"
            ],
            "planting_schedule": [
                {"阶段": "播种期", "时间": "3月15日-25日", "关键操作": "精量播种、覆膜保温"},
                {"阶段": "苗期", "时间": "4月1日-30日", "关键操作": "查苗补苗、中耕除草"},
                {"阶段": "拔节期", "时间": "5月1日-31日", "关键操作": "追肥灌水、病虫防治"},
                {"阶段": "抽雄期", "时间": "6月1日-20日", "关键操作": "水肥管理、去雄授粉"},
                {"阶段": "灌浆期", "时间": "7月1日-31日", "关键操作": "保证水分、防早衰"},
                {"阶段": "成熟期", "时间": "8月15日-30日", "关键操作": "适时收获、降水保存"}
            ]
        },
        "大豆": {
            "emoji": "🌿", 
            "variety": "东农42",
            "image": "https://images.unsplash.com/photo-1605030753481-bb38b08c384a?w=300&h=200&fit=crop",
            "reasons": [
                "🌱 豆科作物可固氮，改善土壤肥力",
                "💰 当前大豆市场需求旺盛，价格稳定上升",
                "🌡️ 适应当前温度条件，生长期较短",
                "🔄 与玉米轮作效果佳，破除连作障碍",
                "💧 耐旱性强，水分需求相对较低"
            ],
            "planting_schedule": [
                {"阶段": "播种期", "时间": "4月20日-30日", "关键操作": "适期播种、接种根瘤菌"},
                {"阶段": "出苗期", "时间": "5月1日-15日", "关键操作": "查苗补种、浅锄保墒"},
                {"阶段": "分枝期", "时间": "5月16日-6月15日", "关键操作": "中耕培土、适量追肥"},
                {"阶段": "开花期", "时间": "6月16日-7月15日", "关键操作": "保证水分、防治害虫"},
                {"阶段": "结荚期", "时间": "7月16日-8月15日", "关键操作": "叶面喷肥、病害防治"},
                {"阶段": "成熟期", "时间": "8月16日-9月10日", "关键操作": "适时收获、晾晒储存"}
            ]
        },
        "向日葵": {
            "emoji": "🌻",
            "variety": "三瑞3号", 
            "image": "https://images.unsplash.com/photo-1508296695146-257a814070b4?w=300&h=200&fit=crop",
            "reasons": [
                "🧂 耐盐碱特性强，适合当前土壤条件（盐碱度0.35‰）",
                "☀️ 喜光作物，当地光照条件充足",
                "🌱 根系发达，改良土壤效果好", 
                "💰 油葵价格稳定，深加工前景广阔",
                "🐝 花期长，有利于养蜂等副业发展"
            ],
            "planting_schedule": [
                {"阶段": "播种期", "时间": "4月25日-5月5日", "关键操作": "深耕整地、精选种子"},
                {"阶段": "苗期", "时间": "5月6日-25日", "关键操作": "间苗定苗、中耕除草"},
                {"阶段": "现蕾期", "时间": "5月26日-6月25日", "关键操作": "追肥灌水、病虫防治"},
                {"阶段": "开花期", "时间": "6月26日-7月25日", "关键操作": "人工辅助授粉、水肥管理"},
                {"阶段": "灌浆期", "时间": "7月26日-8月25日", "关键操作": "保证水分、防鸟害"},
                {"阶段": "成熟期", "时间": "8月26日-9月15日", "关键操作": "适时收获、通风晾晒"}
            ]
        }
    }
    
    if crop_name not in crop_details:
        crop_name = "玉米"  # 默认显示玉米
    
    crop_info = crop_details[crop_name]
    
    # 作物基本信息
    col_img, col_info = st.columns([1, 2])
    
    with col_img:
        st.markdown(f"""
        <div style="text-align: center; padding: 20px;">
            <div style="font-size: 4em; margin-bottom: 10px;">{crop_info['emoji']}</div>
            <div style="font-size: 1.2em; font-weight: bold; color: #333;">
                {crop_name} - {crop_info['variety']}
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col_info:
        st.markdown("#### 🎯 推荐理由")
        for reason in crop_info['reasons']:
            st.markdown(f"- {reason}")
    
    # 种植时间表
    st.markdown("#### 📅 种植时间安排")
    
    schedule_df = pd.DataFrame(crop_info['planting_schedule'])
    
    # 创建时间轴可视化
    fig_timeline = go.Figure()
    
    for i, stage in enumerate(schedule_df.iterrows()):
        stage_data = stage[1]
        fig_timeline.add_trace(go.Scatter(
            x=[i, i+1],
            y=[stage_data['阶段'], stage_data['阶段']],
            mode='lines+markers',
            name=stage_data['阶段'],
            line=dict(width=8),
            marker=dict(size=12)
        ))
    
    fig_timeline.update_layout(
        title=f"{crop_name}种植时间轴",
        xaxis_title="种植进程",
        yaxis_title="生长阶段",
        font=dict(family="SimHei", size=10),
        height=300,
        showlegend=False,
        margin=dict(l=0, r=0, t=30, b=0)
    )
    
    st.plotly_chart(fig_timeline, use_container_width=True)
    
    # 详细时间表
    st.dataframe(schedule_df, use_container_width=True)
    
    # 同田异种方案
    st.markdown("#### 🌱 同田异种管理方案")
    
    multi_crop_col1, multi_crop_col2 = st.columns(2)
    
    with multi_crop_col1:
        st.success(f"""
        **🎯 {crop_name}主导方案**
        - 主作物: {crop_name}（占比60%）
        - 搭配作物: 大豆（占比25%）、向日葵（占比15%）
        - 种植模式: 条带间作
        - 预期效果: 增产15%，降低风险30%
        """)
    
    with multi_crop_col2:
        st.info("""
        **🔄 多轮作保种方案**
        - 第一年: 玉米-大豆轮作
        - 第二年: 向日葵-小麦轮作  
        - 第三年: 绿肥作物休耕
        - 轮作周期: 3年一循环
        """)
    
    # 管理建议
    st.markdown("#### 💡 后续管理建议")
    
    management_tabs = st.tabs(["水肥管理", "病虫防治", "田间管理", "收获储存"])
    
    with management_tabs[0]:
        st.markdown(f"""
        **💧 {crop_name}水肥管理方案**
        
        **灌溉建议:**
        - 播种期: 保持土壤湿润，促进发芽
        - 生长期: 根据土壤墒情，适时补水
        - 关键期: 开花结实期保证充足水分
        
        **施肥建议:**
        - 基肥: 有机肥2000kg/亩 + 复合肥40kg/亩
        - 追肥: 分2-3次追施，以氮肥为主
        - 叶面肥: 生长关键期喷施微量元素
        """)
    
    with management_tabs[1]:
        st.markdown(f"""
        **🛡️ {crop_name}病虫害防治**
        
        **主要病害预防:**
        - 选用抗病品种，合理轮作
        - 种子处理，土壤消毒
        - 及时排水，降低田间湿度
        
        **主要虫害防治:**
        - 物理防治: 性信息素诱捕器
        - 生物防治: 释放天敌昆虫
        - 化学防治: 低毒高效农药
        """)
    
    with management_tabs[2]:
        st.markdown(f"""
        **🚜 {crop_name}田间管理**
        
        **日常管理:**
        - 定期中耕除草，保持田间清洁
        - 及时查苗补苗，确保种植密度
        - 搭建支架，防止倒伏
        
        **监测要点:**
        - 每日观察作物生长状况
        - 定期检查病虫害发生情况
        - 关注天气变化，及时应对
        """)
    
    with management_tabs[3]:
        st.markdown(f"""
        **📦 {crop_name}收获储存**
        
        **收获时机:**
        - 观察作物成熟度指标
        - 选择晴朗天气收获
        - 避免过早或过晚收获
        
        **储存方法:**
        - 充分晾晒，降低水分含量
        - 清理杂质，分级包装
        - 通风干燥，防潮防虫
        """)
    
    # 预期效益分析
    st.markdown("#### 📊 预期效益分析")
    
    benefit_col1, benefit_col2, benefit_col3 = st.columns(3)
    
    with benefit_col1:
        st.markdown(create_compact_metric("预期产量", f"{crop_details[crop_name]['planting_schedule'][0].get('产量', '650kg/亩')}", "#28a745"), unsafe_allow_html=True)
    
    with benefit_col2:
        st.markdown(create_compact_metric("预期收益", "1600元/亩", "#17a2b8"), unsafe_allow_html=True)
    
    with benefit_col3:
        st.markdown(create_compact_metric("投资回报率", "160%", "#fd7e14"), unsafe_allow_html=True) 