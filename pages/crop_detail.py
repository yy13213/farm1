import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
from components.layout import create_page_header, create_info_panel, create_compact_metric
from utils.constants import CROP_CATEGORIES, PLOT_CONDITIONS

def show():
    """显示作物详情分析页面"""
    create_page_header("🌾 作物详情", "作物品种分析与种植指导")
    
    # 作物选择区域 - 紧凑版
    st.markdown("## 🔍 选择作物")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        category = st.selectbox("作物类别", list(CROP_CATEGORIES.keys()))
    
    with col2:
        if category:
            varieties = CROP_CATEGORIES[category]
            variety = st.selectbox("品种选择", varieties)
    
    with col3:
        plot_condition = st.selectbox("地块条件", PLOT_CONDITIONS)
    
    if category and variety:
        # 作物基本信息 - 紧凑显示
        st.markdown(f"## 📋 {variety} 基本信息")
        
        # 基本指标 - 紧凑版
        col1, col2, col3, col4 = st.columns(4)
        
        # 模拟作物数据
        crop_data = {
            "玉米": {"cycle": "120天", "yield": "600kg/亩", "revenue": "1500元/亩", "cost": "800元/亩"},
            "大豆": {"cycle": "110天", "yield": "250kg/亩", "revenue": "1200元/亩", "cost": "650元/亩"},
            "向日葵": {"cycle": "100天", "yield": "300kg/亩", "revenue": "1050元/亩", "cost": "550元/亩"},
            "小麦": {"cycle": "180天", "yield": "450kg/亩", "revenue": "1300元/亩", "cost": "700元/亩"}
        }
        
        current_crop = variety.split()[0] if variety else "玉米"
        data = crop_data.get(current_crop, crop_data["玉米"])
        
        with col1:
            st.markdown(create_compact_metric("生长周期", data["cycle"]), unsafe_allow_html=True)
        
        with col2:
            st.markdown(create_compact_metric("预期产量", data["yield"]), unsafe_allow_html=True)
        
        with col3:
            st.markdown(create_compact_metric("预期收益", data["revenue"]), unsafe_allow_html=True)
        
        with col4:
            st.markdown(create_compact_metric("种植成本", data["cost"]), unsafe_allow_html=True)
        
        # 匹配度显示
        match_score = np.random.randint(75, 95)
        st.markdown(f"""
        <div style="background: linear-gradient(90deg, #90EE90, #32CD32); 
                    border-radius: 8px; padding: 10px; text-align: center; margin: 10px 0;">
            <div style="color: white; font-size: 1.1em; font-weight: bold;">
                🎯 地块匹配度: {match_score}%
            </div>
            <div style="color: white; font-size: 0.9em; margin-top: 3px;">
                {'非常适合' if match_score >= 90 else '比较适合' if match_score >= 80 else '一般适合'}当前地块条件
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # 主要内容区域 - 紧凑布局
        col1, col2 = st.columns([1, 1])
        
        with col1:
            # 环境适应性分析 - 紧凑版
            st.markdown("### 🌱 环境适应性")
            
            # 当前条件vs最佳条件雷达图 - 紧凑版
            categories = ['温度', 'pH', '水分', '养分', '盐碱度']
            current_values = [85, 90, 80, 88, 92]
            optimal_values = [95, 95, 95, 95, 95]
            
            fig = go.Figure()
            
            fig.add_trace(go.Scatterpolar(
                r=current_values,
                theta=categories,
                fill='toself',
                name='当前条件',
                line_color='blue',
                fillcolor='rgba(0,0,255,0.1)'
            ))
            
            fig.add_trace(go.Scatterpolar(
                r=optimal_values,
                theta=categories,
                fill='toself',
                name='最佳条件',
                line_color='green',
                fillcolor='rgba(0,255,0,0.1)'
            ))
            
            fig.update_layout(
                polar=dict(
                    radialaxis=dict(
                        visible=True,
                        range=[0, 100]
                    )),
                showlegend=True,
                font=dict(family="SimHei", size=10),
                height=250,
                margin=dict(l=0, r=0, t=20, b=0)
            )
            
            st.plotly_chart(fig, use_container_width=True)
            
            # 收益预测 - 紧凑版
            st.markdown("### 💰 收益分析")
            
            # 收益构成饼图 - 紧凑版
            revenue_data = pd.DataFrame({
                '项目': ['销售收入', '政府补贴', '其他收入'],
                '金额': [1200, 200, 100],
                '比例': [80, 13, 7]
            })
            
            fig_pie = px.pie(
                revenue_data, 
                values='金额', 
                names='项目',
                height=200
            )
            
            fig_pie.update_layout(
                font=dict(family="SimHei", size=10),
                showlegend=True,
                margin=dict(l=0, r=0, t=20, b=0)
            )
            
            st.plotly_chart(fig_pie, use_container_width=True)
        
        with col2:
            # 成本构成分析 - 紧凑版
            st.markdown("### 💸 成本构成")
            
            cost_data = pd.DataFrame({
                '项目': ['种子', '肥料', '农药', '人工', '其他'],
                '金额': [200, 180, 150, 200, 70],
                '比例': [25, 22.5, 18.8, 25, 8.7]
            })
            
            fig_cost = px.bar(
                cost_data, 
                x='项目', 
                y='金额',
                color='项目',
                height=200
            )
            
            fig_cost.update_layout(
                font=dict(family="SimHei", size=10),
                showlegend=False,
                margin=dict(l=0, r=0, t=20, b=0)
            )
            
            st.plotly_chart(fig_cost, use_container_width=True)
            
            # 市场分析 - 紧凑版
            st.markdown("### 📈 市场分析")
            
            # 价格趋势 - 紧凑版
            months = ['1月', '2月', '3月', '4月', '5月', '6月']
            prices = [4.8, 5.2, 4.9, 5.1, 5.5, 5.3]
            
            fig_price = go.Figure()
            fig_price.add_trace(go.Scatter(
                x=months,
                y=prices,
                mode='lines+markers',
                name='价格趋势',
                line=dict(color='orange', width=2),
                marker=dict(size=4)
            ))
            
            fig_price.update_layout(
                xaxis=dict(title=''),
                yaxis=dict(title='价格(元/kg)'),
                font=dict(family="SimHei", size=10),
                height=180,
                showlegend=False,
                margin=dict(l=0, r=0, t=20, b=0)
            )
            
            st.plotly_chart(fig_price, use_container_width=True)
        
        # 技术指导 - 紧凑版
        st.markdown("### 📖 技术指导")
        
        tab1, tab2, tab3, tab4 = st.tabs(["种植技术", "田间管理", "病虫害防治", "收获加工"])
        
        with tab1:
            st.markdown("#### 🌱 种植技术要点")
            planting_tips = [
                "🌱 **播种时间**: 3月下旬至4月上旬，土温稳定在10°C以上",
                "🌱 **播种深度**: 3-5cm，覆土厚度2-3cm",
                "🌱 **株行距**: 行距60cm，株距25-30cm",
                "🌱 **种植密度**: 每亩3500-4000株",
                "🌱 **选地要求**: 排水良好，pH值6.0-7.5"
            ]
            
            for tip in planting_tips:
                st.markdown(f"<div style='font-size: 0.9em; margin: 5px 0;'>{tip}</div>", unsafe_allow_html=True)
        
        with tab2:
            st.markdown("#### 🌾 田间管理")
            management_tips = [
                "💧 **灌溉管理**: 拔节期、抽穗期、灌浆期适时浇水",
                "🌿 **施肥管理**: 基肥+追肥结合，注意氮磷钾配比",
                "🔪 **中耕除草**: 出苗后及时中耕，保持土壤疏松",
                "✂️ **整枝打杈**: 及时摘除无效分蘖和病弱枝",
                "🌡️ **温度调控**: 适宜生长温度18-25°C"
            ]
            
            for tip in management_tips:
                st.markdown(f"<div style='font-size: 0.9em; margin: 5px 0;'>{tip}</div>", unsafe_allow_html=True)
        
        with tab3:
            st.markdown("#### 🐛 病虫害防治")
            
            col_a, col_b = st.columns(2)
            
            with col_a:
                st.markdown("**主要病害:**")
                diseases = [
                    "🦠 大斑病 - 喷施三唑酮",
                    "🦠 小斑病 - 使用代森锰锌",
                    "🦠 纹枯病 - 井冈霉素防治",
                    "🦠 锈病 - 三唑类杀菌剂"
                ]
                for disease in diseases:
                    st.markdown(f"<div style='font-size: 0.85em; margin: 3px 0;'>{disease}</div>", unsafe_allow_html=True)
            
            with col_b:
                st.markdown("**主要虫害:**")
                pests = [
                    "🐛 玉米螟 - 苏云金杆菌",
                    "🐛 蚜虫 - 吡虫啉防治",
                    "🐛 地老虎 - 辛硫磷颗粒",
                    "🐛 红蜘蛛 - 阿维菌素"
                ]
                for pest in pests:
                    st.markdown(f"<div style='font-size: 0.85em; margin: 3px 0;'>{pest}</div>", unsafe_allow_html=True)
        
        with tab4:
            st.markdown("#### 🌾 收获加工")
            harvest_tips = [
                "📅 **收获时机**: 籽粒含水量25-30%时适时收获",
                "🚜 **收获方式**: 机械收获为主，人工收获为辅",
                "☀️ **晾晒干燥**: 收获后及时晾晒，水分降至14%以下",
                "📦 **储存管理**: 通风干燥处储存，防虫防霉",
                "🏭 **加工利用**: 可用于饲料、食品、工业原料"
            ]
            
            for tip in harvest_tips:
                st.markdown(f"<div style='font-size: 0.9em; margin: 5px 0;'>{tip}</div>", unsafe_allow_html=True)
        
        # 风险评估 - 紧凑版
        st.markdown("### ⚠️ 风险评估")
        
        risk_data = pd.DataFrame([
            {"风险因素": "天气风险", "风险等级": "中", "影响程度": "较大", "防范措施": "天气预报监测，适时调整"},
            {"风险因素": "病虫害", "风险等级": "低", "影响程度": "一般", "防范措施": "定期检查，预防为主"},
            {"风险因素": "市场风险", "风险等级": "中", "影响程度": "较大", "防范措施": "合同种植，期货套保"},
            {"风险因素": "技术风险", "风险等级": "低", "影响程度": "较小", "防范措施": "技术培训，专家指导"},
            {"风险因素": "资金风险", "风险等级": "低", "影响程度": "一般", "防范措施": "合理预算，分期投入"}
        ])
        
        st.dataframe(risk_data, use_container_width=True, height=180)
        
        # 底部操作按钮 - 紧凑版
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            if st.button("📊 生成报告", use_container_width=True):
                st.info("正在生成详细分析报告...")
        
        with col2:
            if st.button("💾 保存方案", use_container_width=True):
                st.success("种植方案已保存")
        
        with col3:
            if st.button("📞 专家咨询", use_container_width=True):
                st.info("正在联系农技专家...")
        
        with col4:
            if st.button("🔄 重新分析", use_container_width=True):
                st.rerun() 