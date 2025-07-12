import streamlit as st
import sys
import os

# 添加当前目录到Python路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# 导入页面模块
from pages import dashboard, plot_management, crop_recommendation, crop_detail, data_analysis
from components.layout import apply_custom_css, create_page_header
from utils.constants import PAGE_CONFIG, APP_CONFIG

def main():
    # 页面配置
    st.set_page_config(
        page_title="智播农链 - 作物推荐系统",
        page_icon="🌱",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # 应用自定义CSS
    apply_custom_css()
    
    # 侧边栏导航
    st.sidebar.markdown("## 🌱 智播农链")
    st.sidebar.markdown("---")
    
    # 导航菜单
    page = st.sidebar.selectbox(
        "选择功能模块",
        ["首页", "地块管理", "作物推荐", "作物详情", "数据分析"]
    )
    
    # 系统信息
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 📊 系统状态")
    st.sidebar.success("✅ 系统运行正常")
    st.sidebar.info(f"📅 {st.session_state.get('current_date', '2024-01-15')}")
    st.sidebar.info(f"🌡️ 当前温度: 18°C")
    
    # 路由到对应页面
    if page == "首页":
        dashboard.show()
    elif page == "地块管理":
        plot_management.show()
    elif page == "作物推荐":
        crop_recommendation.show()
    elif page == "作物详情":
        crop_detail.show()
    elif page == "数据分析":
        data_analysis.show()

if __name__ == "__main__":
    # 初始化session state
    if 'current_date' not in st.session_state:
        st.session_state.current_date = '2024-01-15'
    
    main() 