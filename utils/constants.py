# 系统配置常量

# 应用配置
APP_CONFIG = {
    "title": "智播农链",
    "subtitle": "AI驱动农业全流程数智升级",
    "version": "1.0.0",
    "theme": "light",
    "primary_color": "#90EE90"
}

# 页面配置
PAGE_CONFIG = {
    "page_title": "智播农链 - 作物推荐系统",
    "page_icon": "🌱",
    "layout": "wide",
    "initial_sidebar_state": "expanded"
}

# 推荐算法权重配置
ALGORITHM_WEIGHTS = {
    "environmental": 0.30,  # 环境适应性
    "profit": 0.25,         # 经济效益
    "risk": 0.20,           # 风险评估
    "technical": 0.15,      # 技术难度
    "market": 0.10          # 市场前景
}

# 样式配置
COLORS = {
    "primary": "#90EE90",     # 浅绿色主色
    "secondary": "#98FB98",   # 次要绿色
    "accent": "#00CED1",      # 强调色
    "background": "#F5F5F5",  # 背景色
    "text": "#333333",        # 文字色
    "border": "#E0E0E0",      # 边框色
    "success": "#28a745",     # 成功色
    "warning": "#ffc107",     # 警告色
    "danger": "#dc3545",      # 危险色
    "info": "#17a2b8"         # 信息色
}

# 推荐系统常量
PLANTING_SEASONS = [
    "春季(3-5月)",
    "夏季(6-8月)", 
    "秋季(9-11月)",
    "冬季(12-2月)"
]

RISK_PREFERENCES = [
    "保守型(低风险)",
    "稳健型(中等风险)",
    "积极型(高风险)"
]

TARGET_USES = [
    "粮食作物",
    "经济作物",
    "饲料作物",
    "观赏作物"
]

# 传感器配置
SENSOR_CONFIG = {
    "supported_types": [
        "多合一传感器",
        "土壤传感器", 
        "气象传感器",
        "pH传感器",
        "盐碱度传感器"
    ],
    "data_ranges": {
        "temperature": {"min": -20, "max": 50, "unit": "°C"},
        "humidity": {"min": 0, "max": 100, "unit": "%"},
        "ph_value": {"min": 3.0, "max": 12.0, "unit": ""},
        "salinity": {"min": 0.0, "max": 2.0, "unit": "‰"},
        "nitrogen": {"min": 0, "max": 300, "unit": "mg/kg"},
        "phosphorus": {"min": 0, "max": 100, "unit": "mg/kg"},
        "potassium": {"min": 0, "max": 300, "unit": "mg/kg"}
    }
}

# 作物数据库
CROPS_DATABASE = {
    "玉米": {
        "varieties": ["郑单958", "先玉335", "京科968"],
        "optimal_conditions": {
            "temperature": {"min": 15, "max": 30},
            "ph": {"min": 6.0, "max": 7.5},
            "salinity": {"max": 0.5}
        }
    },
    "大豆": {
        "varieties": ["东农42", "中黄13", "齐黄34"],
        "optimal_conditions": {
            "temperature": {"min": 12, "max": 28},
            "ph": {"min": 6.2, "max": 7.8},
            "salinity": {"max": 0.4}
        }
    },
    "向日葵": {
        "varieties": ["三瑞3号", "龙葵杂6号", "SH363"],
        "optimal_conditions": {
            "temperature": {"min": 18, "max": 32},
            "ph": {"min": 6.5, "max": 8.0},
            "salinity": {"max": 0.6}
        }
    }
}

# 微区划分参数
ZONE_CONFIG = {
    "default_zone_size": 10,  # 每个微区的面积(亩)
    "max_zones_per_plot": 20, # 每个地块最大微区数
    "min_zones_per_plot": 1   # 每个地块最小微区数
}

# 作物分类数据
CROP_CATEGORIES = {
    "粮食作物": [
        "玉米 郑单958",
        "玉米 先玉335", 
        "玉米 京科968",
        "大豆 东农42",
        "大豆 中黄13",
        "大豆 齐黄34",
        "小麦 济麦22",
        "小麦 烟农19",
        "水稻 龙粳31"
    ],
    "经济作物": [
        "向日葵 三瑞3号",
        "向日葵 龙葵杂6号",
        "棉花 鲁棉研28",
        "花生 花育25",
        "油菜 中双11",
        "芝麻 豫芝11"
    ],
    "蔬菜作物": [
        "番茄 金棚1号",
        "黄瓜 津优35",
        "白菜 北京新3号",
        "萝卜 春白玉",
        "茄子 茄杂2号"
    ],
    "饲料作物": [
        "青贮玉米",
        "苜蓿草",
        "燕麦草",
        "高粱草"
    ]
}

# 地块条件选项
PLOT_CONDITIONS = [
    "平原地区-肥沃土壤",
    "平原地区-一般土壤", 
    "平原地区-盐碱土壤",
    "丘陵地区-梯田",
    "丘陵地区-坡地",
    "山地-缓坡",
    "河谷-冲积土",
    "沿海-盐渍土"
] 