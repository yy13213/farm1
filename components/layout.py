import streamlit as st
from utils.constants import COLORS, APP_CONFIG

def apply_custom_css():
    """应用自定义CSS样式 - 优化为50%网页比例"""
    css = f"""
    <style>
    /* 主体样式 - 紧凑布局 */
    .main {{
        background-color: {COLORS['background']};
        padding: 10px;
    }}
    
    /* 标题样式 - 缩小尺寸 */
    .main-title {{
        color: {COLORS['primary']};
        text-align: center;
        padding: 10px 0;
        border-bottom: 2px solid {COLORS['primary']};
        margin-bottom: 15px;
        font-size: 1.8em;
    }}
    
    /* 卡片样式 - 紧凑设计 */
    .metric-card {{
        background: white;
        padding: 12px;
        border-radius: 8px;
        border-left: 3px solid {COLORS['primary']};
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        margin: 5px 0;
        min-height: 80px;
    }}
    
    .metric-value {{
        font-size: 1.8em;
        font-weight: bold;
        color: {COLORS['primary']};
        line-height: 1.2;
    }}
    
    .metric-label {{
        color: {COLORS['text']};
        font-size: 0.9em;
        margin-top: 3px;
    }}
    
    /* 功能按钮样式 - 小尺寸 */
    .feature-button {{
        background: linear-gradient(135deg, {COLORS['primary']} 0%, {COLORS['secondary']} 100%);
        color: white;
        padding: 12px;
        border-radius: 10px;
        text-align: center;
        cursor: pointer;
        transition: all 0.3s ease;
        border: none;
        width: 100%;
        margin: 5px 0;
        min-height: 100px;
    }}
    
    .feature-button:hover {{
        transform: translateY(-1px);
        box-shadow: 0 4px 15px rgba(144, 238, 144, 0.3);
    }}
    
    /* 推荐卡片样式 - 紧凑 */
    .recommendation-card {{
        background: white;
        border-radius: 10px;
        padding: 12px;
        margin: 8px 0;
        border: 1px solid {COLORS['border']};
        transition: all 0.3s ease;
        min-height: 120px;
    }}
    
    .recommendation-card:hover {{
        border-color: {COLORS['primary']};
        box-shadow: 0 3px 10px rgba(144, 238, 144, 0.2);
    }}
    
    .crop-name {{
        color: {COLORS['primary']};
        font-size: 1.1em;
        font-weight: bold;
        margin-bottom: 8px;
    }}
    
    .score-stars {{
        color: {COLORS['accent']};
        font-size: 1em;
    }}
    
    /* 传感器状态样式 */
    .sensor-online {{
        color: {COLORS['success']};
        font-weight: bold;
        font-size: 0.9em;
    }}
    
    .sensor-offline {{
        color: {COLORS['danger']};
        font-weight: bold;
        font-size: 0.9em;
    }}
    
    /* 侧边栏样式 - 紧凑 */
    .sidebar .sidebar-content {{
        background: linear-gradient(180deg, {COLORS['primary']} 0%, {COLORS['secondary']} 100%);
        padding: 10px;
    }}
    
    /* 表单样式 - 小尺寸 */
    .stSelectbox > div > div {{
        border-color: {COLORS['primary']};
        min-height: 35px;
    }}
    
    .stNumberInput > div > div > input {{
        border-color: {COLORS['primary']};
        padding: 8px;
    }}
    
    /* 成功提示样式 - 紧凑 */
    .success-message {{
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        color: #155724;
        padding: 10px;
        border-radius: 6px;
        margin: 8px 0;
        font-size: 0.9em;
    }}
    
    /* 警告提示样式 - 紧凑 */
    .warning-message {{
        background-color: #fff3cd;
        border: 1px solid #ffeaa7;
        color: #856404;
        padding: 10px;
        border-radius: 6px;
        margin: 8px 0;
        font-size: 0.9em;
    }}
    
    /* 信息面板样式 - 紧凑 */
    .info-panel {{
        background: white;
        border-radius: 8px;
        padding: 12px;
        border-left: 3px solid {COLORS['accent']};
        margin: 10px 0;
        font-size: 0.9em;
    }}
    
    /* 数据表格样式 - 紧凑 */
    .dataframe {{
        border: 1px solid {COLORS['border']};
        border-radius: 6px;
        font-size: 0.85em;
    }}
    
    /* 进度条样式 */
    .stProgress > div > div > div {{
        background-color: {COLORS['primary']};
        height: 8px;
    }}
    
    /* 响应式设计 - 50%网页比例优化 */
    @media (max-width: 1200px) {{
        .main-title {{
            font-size: 1.5em;
            padding: 8px 0;
        }}
        
        .metric-card {{
            padding: 10px;
            min-height: 70px;
        }}
        
        .metric-value {{
            font-size: 1.5em;
        }}
        
        .feature-button {{
            padding: 10px;
            min-height: 85px;
        }}
        
        .recommendation-card {{
            padding: 10px;
            min-height: 100px;
        }}
    }}
    
    /* 紧凑模式按钮样式 */
    .compact-button {{
        background: {COLORS['primary']};
        color: white;
        padding: 6px 12px;
        border-radius: 6px;
        border: none;
        font-size: 0.85em;
        margin: 2px;
        cursor: pointer;
    }}
    
    /* 小图表容器 */
    .chart-container {{
        height: 250px;
        margin: 8px 0;
    }}
    
    /* 紧凑表格 */
    .compact-table {{
        font-size: 0.8em;
    }}
    
    .compact-table th, .compact-table td {{
        padding: 4px 8px;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

def create_page_header(title, subtitle=None):
    """创建页面标题头部 - 紧凑版"""
    st.markdown(f'<h1 class="main-title">{title}</h1>', unsafe_allow_html=True)
    if subtitle:
        st.markdown(f'<p style="text-align: center; color: {COLORS["text"]}; font-size: 1em; margin-top: -10px;">{subtitle}</p>', unsafe_allow_html=True)

def create_metric_card(label, value, unit="", delta=None):
    """创建指标卡片 - 紧凑版"""
    delta_html = ""
    if delta:
        delta_color = COLORS['success'] if delta > 0 else COLORS['danger']
        delta_symbol = "↑" if delta > 0 else "↓"
        delta_html = f'<div style="color: {delta_color}; font-size: 0.8em;">{delta_symbol} {abs(delta)}</div>'
    
    card_html = f"""
    <div class="metric-card">
        <div class="metric-value">{value}{unit}</div>
        <div class="metric-label">{label}</div>
        {delta_html}
    </div>
    """
    return card_html

def create_feature_button(title, description, icon="🌱"):
    """创建功能按钮 - 紧凑版"""
    button_html = f"""
    <div class="feature-button">
        <div style="font-size: 1.5em; margin-bottom: 5px;">{icon}</div>
        <div style="font-size: 1em; font-weight: bold;">{title}</div>
        <div style="font-size: 0.8em; margin-top: 3px; opacity: 0.8;">{description}</div>
    </div>
    """
    return button_html

def create_recommendation_card(crop_name, suitability, profit, risk, variety=""):
    """创建推荐卡片 - 紧凑版"""
    # 星级评分
    stars_suitability = "★" * int(suitability/20) + "☆" * (5 - int(suitability/20))
    
    # 风险颜色
    risk_color = COLORS['success'] if risk < 30 else COLORS['warning'] if risk < 70 else COLORS['danger']
    risk_text = "低" if risk < 30 else "中" if risk < 70 else "高"
    
    # 收益颜色
    profit_color = COLORS['success'] if profit > 70 else COLORS['warning'] if profit > 40 else COLORS['danger']
    profit_text = "高" if profit > 70 else "中" if profit > 40 else "低"
    
    card_html = f"""
    <div class="recommendation-card">
        <div class="crop-name">{crop_name}</div>
        {f'<div style="color: {COLORS["text"]}; font-size: 0.8em; margin-bottom: 8px;">品种: {variety}</div>' if variety else ''}
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <div>
                <div style="margin: 3px 0; font-size: 0.85em;">
                    <span style="color: {COLORS['text']};">适应性: </span>
                    <span class="score-stars">{stars_suitability}</span>
                </div>
                <div style="margin: 3px 0; font-size: 0.85em;">
                    <span style="color: {COLORS['text']};">收益: </span>
                    <span style="color: {profit_color}; font-weight: bold;">{profit_text}</span>
                </div>
                <div style="margin: 3px 0; font-size: 0.85em;">
                    <span style="color: {COLORS['text']};">风险: </span>
                    <span style="color: {risk_color}; font-weight: bold;">{risk_text}</span>
                </div>
            </div>
        </div>
    </div>
    """
    return card_html

def create_sensor_status_badge(status):
    """创建传感器状态徽章"""
    if status == "在线":
        return f'<span class="sensor-online">● {status}</span>'
    else:
        return f'<span class="sensor-offline">● {status}</span>'

def create_info_panel(title, content, icon="ℹ️"):
    """创建信息面板 - 紧凑版"""
    panel_html = f"""
    <div class="info-panel">
        <div style="font-size: 1em; font-weight: bold; margin-bottom: 8px;">
            {icon} {title}
        </div>
        <div style="color: {COLORS['text']}; font-size: 0.9em;">
            {content}
        </div>
    </div>
    """
    return panel_html

def create_compact_metric(label, value, color=None):
    """创建紧凑指标显示"""
    if color is None:
        color = COLORS['primary']
    
    return f"""
    <div style="background: white; padding: 8px; border-radius: 6px; margin: 3px 0; 
                border-left: 3px solid {color}; display: flex; justify-content: space-between;">
        <span style="font-size: 0.85em; color: {COLORS['text']};">{label}</span>
        <span style="font-size: 0.9em; font-weight: bold; color: {color};">{value}</span>
    </div>
    """ 