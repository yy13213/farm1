import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from components.layout import create_page_header, create_metric_card

def show():
    """显示数据分析页面"""
    create_page_header("📊 数据分析", "历史数据分析与趋势预测")
    
    # 分析类型选择
    analysis_type = st.selectbox(
        "选择分析类型",
        ["综合分析", "推荐效果分析", "作物产量分析", "环境数据分析", "收益分析", "风险分析"]
    )
    
    if analysis_type == "综合分析":
        show_comprehensive_analysis()
    elif analysis_type == "推荐效果分析":
        show_recommendation_analysis()
    elif analysis_type == "作物产量分析":
        show_yield_analysis()
    elif analysis_type == "环境数据分析":
        show_environmental_analysis()
    elif analysis_type == "收益分析":
        show_profit_analysis()
    else:
        show_risk_analysis()

def show_comprehensive_analysis():
    """综合分析"""
    st.markdown("## 📈 综合数据分析")
    
    # 关键指标卡片
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(create_metric_card("推荐成功率", "91.5", "%", delta=2.3), unsafe_allow_html=True)
    
    with col2:
        st.markdown(create_metric_card("平均收益", "1348", "元/亩", delta=125), unsafe_allow_html=True)
    
    with col3:
        st.markdown(create_metric_card("用户满意度", "94.2", "%", delta=1.8), unsafe_allow_html=True)
    
    with col4:
        st.markdown(create_metric_card("数据完整度", "96.7", "%", delta=0.5), unsafe_allow_html=True)
    
    # 时间段选择
    st.markdown("---")
    col1, col2 = st.columns(2)
    
    with col1:
        start_date = st.date_input("开始日期", value=datetime.now() - timedelta(days=365))
    
    with col2:
        end_date = st.date_input("结束日期", value=datetime.now())
    
    # 综合趋势图
    st.markdown("### 📊 关键指标趋势")
    
    # 生成模拟数据
    dates = pd.date_range(start=start_date, end=end_date, freq='M')
    success_rate = np.random.normal(91, 3, len(dates))
    user_satisfaction = np.random.normal(94, 2, len(dates))
    avg_profit = np.random.normal(1350, 100, len(dates))
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=dates,
        y=success_rate,
        mode='lines+markers',
        name='推荐成功率(%)',
        line=dict(color='green', width=3),
        yaxis='y1'
    ))
    
    fig.add_trace(go.Scatter(
        x=dates,
        y=user_satisfaction,
        mode='lines+markers',
        name='用户满意度(%)',
        line=dict(color='blue', width=3),
        yaxis='y1'
    ))
    
    fig.add_trace(go.Scatter(
        x=dates,
        y=avg_profit,
        mode='lines+markers',
        name='平均收益(元/亩)',
        line=dict(color='orange', width=3),
        yaxis='y2'
    ))
    
    fig.update_layout(
        title='关键指标趋势分析',
        xaxis=dict(title='时间'),
        yaxis=dict(title='成功率/满意度(%)', side='left'),
        yaxis2=dict(title='收益(元/亩)', side='right', overlaying='y'),
        font=dict(family="SimHei", size=12),
        height=500,
        hovermode='x unified'
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # 地块对比分析
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🏞️ 地块表现对比")
        
        plot_performance = pd.DataFrame({
            '地块': ['地块A', '地块B', '地块C', '地块D', '地块E'],
            '推荐次数': [25, 18, 32, 15, 28],
            '成功率': [95, 88, 92, 85, 90],
            '平均收益': [1450, 1280, 1380, 1150, 1320]
        })
        
        fig_bar = px.bar(
            plot_performance,
            x='地块',
            y='推荐次数',
            color='成功率',
            title='各地块推荐表现',
            color_continuous_scale='Greens'
        )
        
        fig_bar.update_layout(
            font=dict(family="SimHei", size=12),
            height=400
        )
        
        st.plotly_chart(fig_bar, use_container_width=True)
    
    with col2:
        st.markdown("### 🌾 作物推荐分布")
        
        crop_distribution = {
            '玉米': 35,
            '大豆': 25,
            '向日葵': 20,
            '小麦': 15,
            '其他': 5
        }
        
        fig_pie = px.pie(
            values=list(crop_distribution.values()),
            names=list(crop_distribution.keys()),
            title='作物推荐分布',
            color_discrete_sequence=['#90EE90', '#98FB98', '#00CED1', '#87CEEB', '#DDA0DD']
        )
        
        fig_pie.update_layout(
            font=dict(family="SimHei", size=12),
            height=400
        )
        
        st.plotly_chart(fig_pie, use_container_width=True)

def show_recommendation_analysis():
    """推荐效果分析"""
    st.markdown("## 🎯 推荐效果分析")
    
    # 推荐算法性能对比
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🔬 算法性能对比")
        
        algorithm_performance = pd.DataFrame({
            '算法版本': ['v1.0', 'v1.1', 'v1.2', 'v2.0', 'v2.1'],
            '准确率': [85, 88, 90, 92, 94],
            '召回率': [82, 85, 88, 90, 93],
            'F1得分': [83.5, 86.5, 89, 91, 93.5]
        })
        
        fig_line = go.Figure()
        
        for metric in ['准确率', '召回率', 'F1得分']:
            fig_line.add_trace(go.Scatter(
                x=algorithm_performance['算法版本'],
                y=algorithm_performance[metric],
                mode='lines+markers',
                name=metric,
                line=dict(width=3),
                marker=dict(size=8)
            ))
        
        fig_line.update_layout(
            title='算法性能演进',
            xaxis_title='算法版本',
            yaxis_title='性能指标(%)',
            font=dict(family="SimHei", size=12),
            height=400
        )
        
        st.plotly_chart(fig_line, use_container_width=True)
    
    with col2:
        st.markdown("### 📊 推荐结果准确性")
        
        accuracy_data = {
            '非常准确': 45,
            '比较准确': 35,
            '一般准确': 15,
            '不太准确': 4,
            '完全不准确': 1
        }
        
        fig_donut = px.pie(
            values=list(accuracy_data.values()),
            names=list(accuracy_data.keys()),
            title='用户对推荐结果准确性评价',
            hole=0.4,
            color_discrete_sequence=['#228B22', '#90EE90', '#98FB98', '#FFA500', '#FF6347']
        )
        
        fig_donut.update_layout(
            font=dict(family="SimHei", size=12),
            height=400
        )
        
        st.plotly_chart(fig_donut, use_container_width=True)
    
    # 推荐因子重要性分析
    st.markdown("### 🔍 推荐因子重要性分析")
    
    factor_importance = pd.DataFrame({
        '因子': ['土壤pH值', '盐碱度', '温度', '湿度', '氮含量', '磷含量', '钾含量', '历史产量', '市场价格'],
        '重要性': [0.18, 0.16, 0.14, 0.12, 0.11, 0.09, 0.08, 0.07, 0.05],
        '影响程度': ['极高', '高', '高', '中高', '中高', '中', '中', '中低', '中低']
    })
    
    fig_bar = px.bar(
        factor_importance,
        x='重要性',
        y='因子',
        orientation='h',
        color='重要性',
        title='推荐因子重要性排序',
        color_continuous_scale='Greens'
    )
    
    fig_bar.update_layout(
        font=dict(family="SimHei", size=12),
        height=500
    )
    
    st.plotly_chart(fig_bar, use_container_width=True)
    
    # 详细数据表
    st.markdown("### 📋 推荐效果详细数据")
    
    recommendation_details = pd.DataFrame({
        '时间': ['2024-01', '2024-02', '2024-03', '2024-04', '2024-05'],
        '推荐次数': [45, 52, 38, 65, 58],
        '成功推荐': [42, 48, 35, 60, 54],
        '成功率(%)': [93.3, 92.3, 92.1, 92.3, 93.1],
        '用户反馈平均分': [4.2, 4.3, 4.1, 4.4, 4.5],
        '实际采用率(%)': [78, 82, 75, 85, 88]
    })
    
    st.dataframe(recommendation_details, use_container_width=True)

def show_yield_analysis():
    """作物产量分析"""
    st.markdown("## 🌾 作物产量分析")
    
    # 产量趋势分析
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📈 历年产量趋势")
        
        years = list(range(2019, 2024))
        corn_yield = [580, 595, 610, 625, 635]
        soybean_yield = [240, 245, 250, 255, 260]
        sunflower_yield = [290, 295, 300, 305, 310]
        
        fig_yield = go.Figure()
        
        fig_yield.add_trace(go.Scatter(
            x=years,
            y=corn_yield,
            mode='lines+markers',
            name='玉米',
            line=dict(color='gold', width=3)
        ))
        
        fig_yield.add_trace(go.Scatter(
            x=years,
            y=soybean_yield,
            mode='lines+markers',
            name='大豆',
            line=dict(color='green', width=3)
        ))
        
        fig_yield.add_trace(go.Scatter(
            x=years,
            y=sunflower_yield,
            mode='lines+markers',
            name='向日葵',
            line=dict(color='orange', width=3)
        ))
        
        fig_yield.update_layout(
            title='主要作物产量趋势(kg/亩)',
            xaxis_title='年份',
            yaxis_title='产量(kg/亩)',
            font=dict(family="SimHei", size=12),
            height=400
        )
        
        st.plotly_chart(fig_yield, use_container_width=True)
    
    with col2:
        st.markdown("### 🎯 产量目标达成率")
        
        target_achievement = pd.DataFrame({
            '作物': ['玉米', '大豆', '向日葵', '小麦', '棉花'],
            '目标产量': [600, 250, 300, 450, 150],
            '实际产量': [635, 260, 310, 440, 145],
            '达成率': [105.8, 104.0, 103.3, 97.8, 96.7]
        })
        
        fig_target = px.bar(
            target_achievement,
            x='作物',
            y='达成率',
            title='产量目标达成情况(%)',
            color='达成率',
            color_continuous_scale='RdYlGn',
            color_continuous_midpoint=100
        )
        
        fig_target.add_hline(y=100, line_dash="dash", line_color="red", 
                            annotation_text="目标线")
        
        fig_target.update_layout(
            font=dict(family="SimHei", size=12),
            height=400
        )
        
        st.plotly_chart(fig_target, use_container_width=True)
    
    # 产量影响因子分析
    st.markdown("### 🔬 产量影响因子分析")
    
    # 相关性热力图
    factors = ['温度', 'pH值', '盐碱度', '氮含量', '磷含量', '钾含量', '降水量']
    correlation_matrix = np.random.uniform(0.3, 0.9, (len(factors), len(factors)))
    np.fill_diagonal(correlation_matrix, 1.0)
    correlation_matrix = (correlation_matrix + correlation_matrix.T) / 2  # 确保对称
    
    fig_heatmap = px.imshow(
        correlation_matrix,
        x=factors,
        y=factors,
        color_continuous_scale='RdYlGn',
        title='环境因子与产量相关性分析'
    )
    
    fig_heatmap.update_layout(
        font=dict(family="SimHei", size=12),
        height=500
    )
    
    st.plotly_chart(fig_heatmap, use_container_width=True)

def show_environmental_analysis():
    """环境数据分析"""
    st.markdown("## 🌡️ 环境数据分析")
    
    # 环境监测指标选择
    selected_metrics = st.multiselect(
        "选择监测指标",
        ["温度", "湿度", "pH值", "盐碱度", "氮含量", "磷含量", "钾含量"],
        default=["温度", "湿度", "pH值"]
    )
    
    if selected_metrics:
        # 生成环境数据时间序列
        dates = pd.date_range(start=datetime.now() - timedelta(days=30), end=datetime.now(), freq='D')
        
        fig_env = go.Figure()
        
        for metric in selected_metrics:
            if metric == "温度":
                data = np.random.normal(18, 3, len(dates))
                unit = "°C"
                color = 'red'
            elif metric == "湿度":
                data = np.random.normal(65, 8, len(dates))
                unit = "%"
                color = 'blue'
            elif metric == "pH值":
                data = np.random.normal(6.8, 0.3, len(dates))
                unit = ""
                color = 'green'
            elif metric == "盐碱度":
                data = np.random.normal(0.3, 0.1, len(dates))
                unit = "‰"
                color = 'orange'
            else:
                data = np.random.normal(50, 10, len(dates))
                unit = "mg/kg"
                color = 'purple'
            
            fig_env.add_trace(go.Scatter(
                x=dates,
                y=data,
                mode='lines+markers',
                name=f'{metric}({unit})',
                line=dict(color=color, width=2),
                marker=dict(size=4)
            ))
        
        fig_env.update_layout(
            title='环境监测数据趋势',
            xaxis_title='时间',
            yaxis_title='监测值',
            font=dict(family="SimHei", size=12),
            height=500
        )
        
        st.plotly_chart(fig_env, use_container_width=True)
    
    # 环境数据统计分析
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📊 数据质量统计")
        
        quality_stats = pd.DataFrame({
            '指标': ['数据完整率', '异常值比例', '传感器在线率', '数据时效性'],
            '当前值': [96.5, 2.1, 94.2, 98.8],
            '目标值': [95.0, 3.0, 90.0, 95.0],
            '状态': ['优秀', '良好', '优秀', '优秀']
        })
        
        st.dataframe(quality_stats, use_container_width=True)
    
    with col2:
        st.markdown("### 🚨 异常数据统计")
        
        anomaly_stats = {
            '温度异常': 3,
            'pH值异常': 2,
            '湿度异常': 1,
            '传感器故障': 2
        }
        
        fig_anomaly = px.bar(
            x=list(anomaly_stats.keys()),
            y=list(anomaly_stats.values()),
            title='近30天异常事件统计',
            color=list(anomaly_stats.values()),
            color_continuous_scale='Reds'
        )
        
        fig_anomaly.update_layout(
            font=dict(family="SimHei", size=12),
            height=300
        )
        
        st.plotly_chart(fig_anomaly, use_container_width=True)

def show_profit_analysis():
    """收益分析"""
    st.markdown("## 💰 收益分析")
    
    # 收益概览
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("总收益", "168.5万元", delta="12.3万元")
    
    with col2:
        st.metric("平均收益", "1348元/亩", delta="125元/亩")
    
    with col3:
        st.metric("利润率", "68.2%", delta="3.5%")
    
    # 收益构成分析
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 💹 收益构成分析")
        
        revenue_breakdown = {
            '主产品销售': 75,
            '副产品利用': 15,
            '政府补贴': 8,
            '其他收入': 2
        }
        
        fig_revenue = px.pie(
            values=list(revenue_breakdown.values()),
            names=list(revenue_breakdown.keys()),
            title='收益构成比例(%)',
            color_discrete_sequence=['#90EE90', '#98FB98', '#00CED1', '#87CEEB']
        )
        
        fig_revenue.update_layout(
            font=dict(family="SimHei", size=12),
            height=400
        )
        
        st.plotly_chart(fig_revenue, use_container_width=True)
    
    with col2:
        st.markdown("### 📊 成本效益分析")
        
        cost_benefit = pd.DataFrame({
            '项目': ['种子', '肥料', '农药', '机械', '人工'],
            '成本(元/亩)': [150, 300, 100, 200, 50],
            '产出贡献(%)': [20, 35, 15, 20, 10]
        })
        
        fig_cost = px.scatter(
            cost_benefit,
            x='成本(元/亩)',
            y='产出贡献(%)',
            size='成本(元/亩)',
            color='项目',
            title='成本投入与产出贡献关系'
        )
        
        fig_cost.update_layout(
            font=dict(family="SimHei", size=12),
            height=400
        )
        
        st.plotly_chart(fig_cost, use_container_width=True)

def show_risk_analysis():
    """风险分析"""
    st.markdown("## ⚠️ 风险分析")
    
    # 风险评估雷达图
    risk_categories = ['自然灾害', '病虫害', '市场波动', '技术风险', '政策风险', '资金风险']
    risk_scores = [25, 15, 30, 10, 12, 18]
    
    fig_risk = go.Figure()
    
    fig_risk.add_trace(go.Scatterpolar(
        r=risk_scores,
        theta=risk_categories,
        fill='toself',
        name='当前风险水平',
        line_color='red',
        fillcolor='rgba(255,0,0,0.1)'
    ))
    
    fig_risk.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 50]
            )),
        showlegend=True,
        title="风险评估雷达图",
        font=dict(family="SimHei", size=12),
        height=500
    )
    
    st.plotly_chart(fig_risk, use_container_width=True)
    
    # 风险事件历史统计
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📈 风险事件趋势")
        
        months = ['1月', '2月', '3月', '4月', '5月', '6月']
        risk_events = [2, 1, 3, 4, 2, 1]
        
        fig_trend = px.line(
            x=months,
            y=risk_events,
            title='月度风险事件统计',
            markers=True
        )
        
        fig_trend.update_layout(
            font=dict(family="SimHei", size=12),
            height=300
        )
        
        st.plotly_chart(fig_trend, use_container_width=True)
    
    with col2:
        st.markdown("### 🛡️ 风险缓解措施效果")
        
        mitigation_effectiveness = {
            '保险覆盖': 85,
            '技术培训': 78,
            '预警系统': 82,
            '应急预案': 75
        }
        
        fig_mitigation = px.bar(
            x=list(mitigation_effectiveness.keys()),
            y=list(mitigation_effectiveness.values()),
            title='风险缓解措施有效性(%)',
            color=list(mitigation_effectiveness.values()),
            color_continuous_scale='Greens'
        )
        
        fig_mitigation.update_layout(
            font=dict(family="SimHei", size=12),
            height=300
        )
        
        st.plotly_chart(fig_mitigation, use_container_width=True) 