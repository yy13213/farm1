import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from datetime import datetime, timedelta
from components.layout import create_page_header, create_metric_card, create_feature_button, create_info_panel, create_compact_metric

def show():
    """显示首页/仪表板"""
    create_page_header("🌱 智播农链", "AI驱动农业全流程数智升级")
    
    # 系统概览卡片区域 - 紧凑布局
    st.markdown("## 📊 系统概览")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(create_metric_card("管理地块", "12", "个", delta=2), unsafe_allow_html=True)
    
    with col2:
        st.markdown(create_metric_card("推荐作物", "28", "种", delta=3), unsafe_allow_html=True)
    
    with col3:
        st.markdown(create_metric_card("微区数量", "48", "个", delta=5), unsafe_allow_html=True)
    
    with col4:
        st.markdown(create_metric_card("活跃用户", "156", "人", delta=12), unsafe_allow_html=True)
    
    # 快速功能入口 - 更紧凑
    st.markdown("## 🚀 快速操作")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("📍 地块管理", use_container_width=True, key="nav_plot"):
            st.session_state.selected_page = "地块管理"
            st.rerun()
    
    with col2:
        if st.button("🌾 智能推荐", use_container_width=True, key="nav_recommend"):
            st.session_state.selected_page = "作物推荐"
            st.rerun()
    
    with col3:
        if st.button("📊 数据分析", use_container_width=True, key="nav_analysis"):
            st.session_state.selected_page = "数据分析"
            st.rerun()
    
    # 主要内容区域 - 紧凑布局
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # 最新推荐结果 - 紧凑表格
        st.markdown("### 📈 最新推荐")
        
        # 创建示例推荐数据
        recommendations_data = {
            "地块": ["地块A", "地块B", "地块C", "地块D"],
            "推荐作物": ["玉米", "大豆", "向日葵", "小麦"],
            "适应性": [95, 88, 82, 91],
            "收益": ["高", "中高", "中", "高"],
            "时间": ["10:30", "09:45", "09:12", "16:20"]
        }
        
        df_recommendations = pd.DataFrame(recommendations_data)
        st.dataframe(df_recommendations, use_container_width=True, height=150)
        
        # 地块分布图 - 紧凑版
        st.markdown("### 🗺️ 地块分布")
        
        # 模拟地块位置数据
        plot_data = pd.DataFrame({
            '地块': ['A', 'B', 'C', 'D', 'E'],
            '纬度': [39.9042, 39.9052, 39.9032, 39.9062, 39.9022],
            '经度': [116.4074, 116.4084, 116.4064, 116.4094, 116.4054],
            '面积': [50, 30, 80, 45, 60],
            '作物': ['玉米', '大豆', '向日葵', '小麦', '棉花']
        })
        
        # 创建散点图 - 紧凑版
        fig = px.scatter_mapbox(
            plot_data,
            lat='纬度',
            lon='经度',
            size='面积',
            color='作物',
            hover_name='地块',
            hover_data=['面积'],
            mapbox_style='open-street-map',
            zoom=12,
            height=280
        )
        
        fig.update_layout(
            title="地块位置分布",
            font=dict(family="SimHei", size=10),
            margin=dict(l=0, r=0, t=30, b=0)
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # 系统通知 - 紧凑版
        st.markdown("### 📢 通知")
        
        notifications = [
            {
                "type": "success",
                "title": "推荐完成",
                "content": "地块A玉米推荐完成",
                "time": "10分钟前"
            },
            {
                "type": "warning", 
                "title": "传感器异常",
                "content": "S003连接异常",
                "time": "1小时前"
            },
            {
                "type": "info",
                "title": "数据更新",
                "content": "市场价格已更新",
                "time": "2小时前"
            }
        ]
        
        for notif in notifications:
            if notif["type"] == "success":
                st.success(f"✅ **{notif['title']}**\n{notif['content']}")
            elif notif["type"] == "warning":
                st.warning(f"⚠️ **{notif['title']}**\n{notif['content']}")
            else:
                st.info(f"ℹ️ **{notif['title']}**\n{notif['content']}")
        
        # 实时状态 - 紧凑显示
        st.markdown("### 🌤️ 实时状态")
        
        # 使用紧凑指标显示
        st.markdown(create_compact_metric("温度", "18°C"), unsafe_allow_html=True)
        st.markdown(create_compact_metric("湿度", "65%"), unsafe_allow_html=True)
        st.markdown(create_compact_metric("风速", "2.1m/s"), unsafe_allow_html=True)
        
        # 传感器状态
        st.markdown("### 📡 传感器")
        
        col_a, col_b = st.columns(2)
        with col_a:
            st.metric("在线", "15", delta=None)
        with col_b:
            st.metric("离线", "3", delta=None)
    
    # 底部统计图表 - 紧凑版
    st.markdown("## 📊 统计概览")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # 作物推荐统计 - 紧凑图表
        st.markdown("#### 作物推荐统计")
        
        crop_stats = pd.DataFrame({
            '作物': ['玉米', '大豆', '向日葵', '小麦', '棉花'],
            '推荐次数': [25, 18, 15, 22, 12],
            '成功率': [95, 88, 82, 91, 85]
        })
        
        fig = px.bar(
            crop_stats, 
            x='作物', 
            y='推荐次数',
            color='成功率',
            color_continuous_scale='Greens',
            height=220
        )
        
        fig.update_layout(
            font=dict(family="SimHei", size=10),
            margin=dict(l=0, r=0, t=30, b=0),
            showlegend=False
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # 月度趋势 - 紧凑图表
        st.markdown("#### 推荐趋势")
        
        # 生成过去6个月的数据
        months = ['8月', '9月', '10月', '11月', '12月', '1月']
        recommendations = [45, 52, 38, 65, 58, 72]
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=months,
            y=recommendations,
            mode='lines+markers',
            name='推荐数量',
            line=dict(color='lightgreen', width=2),
            marker=dict(size=6)
        ))
        
        fig.update_layout(
            xaxis=dict(title=''),
            yaxis=dict(title='数量'),
            font=dict(family="SimHei", size=10),
            height=220,
            margin=dict(l=0, r=0, t=30, b=0),
            showlegend=False
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # 页面底部信息 - 紧凑版
    st.markdown(
        create_info_panel(
            "系统状态",
            f"运行正常 | 更新: {datetime.now().strftime('%H:%M')} | 在线: 23人",
            "💡"
        ),
        unsafe_allow_html=True
    ) 