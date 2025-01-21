# 声明：本代码仅供学习和研究目的使用。使用者应遵守以下原则：
# 1. 不得用于任何商业用途。
# 2. 使用时应遵守目标平台的使用条款和robots.txt规则。
# 3. 不得进行大规模爬取或对平台造成运营干扰。
# 4. 应合理控制请求频率，避免给目标平台带来不必要的负担。
# 5. 不得用于任何非法或不当的用途。
#
# 详细许可条款请参阅项目根目录下的LICENSE文件。
# 使用本代码即表示您同意遵守上述原则和LICENSE中的所有条款。

import asyncio
import aiomysql

# 基础配置
PLATFORM = "xhs"

# KEYWORDS = "Tiktok Refugee,Tiktok refugee, tiktok refugee,tt refugee,TT Refugee,TT refugee,TikTok難民,TT難民,tt難民,TT难民,tiktok refugee,tt refugee,TT Refugee,TT refugee,Tiktok Refugee,Tiktok refugee"  # 关键词搜索配置，以英文逗号分隔
KEYWORDS = "tiktok refugee,Tiktok refugee,tt refugee,TT Refugee,TT refugee,TikTok難民,TT難民,tt難民,TT难民,TikTok 难民,tiktok refugee,tt refugee,TT Refugee,TT refugee,Tiktok Refugee,Tiktok refugee"
LOGIN_TYPE = "phone"  # qrcode or phone or cookie
COOKIES = ""
# 具体值参见media_platform.xxx.field下的枚举值，暂时只支持小红书
SORT_TYPE = "general"
# 具体值参见media_platform.xxx.field下的枚举值，暂时只支持抖音
PUBLISH_TIME_TYPE = 0
CRAWLER_TYPE = (
    "search"  # 爬取类型，search(关键词搜索) | detail(帖子详情)| creator(创作者主页数据)
)
# 自定义User Agent（暂时仅对XHS有效）
UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'

# 是否开启 IP 代理
ENABLE_IP_PROXY = False

# 未启用代理时的最大爬取间隔，单位秒（暂时仅对XHS有效）
CRAWLER_MAX_SLEEP_SEC = 2

# 代理IP池数量
IP_PROXY_POOL_COUNT = 2

# 代理IP提供商名称
IP_PROXY_PROVIDER_NAME = "kuaidaili"

# 设置为True不会打开浏览器（无头浏览器）
# 设置False会打开一个浏览器
# 小红书如果一直扫码登录不通过，打开浏览器手动过一下滑动验证码
# 抖音如果一直提示失败，打开浏览器看下是否扫码登录之后出现了手机号验证，如果出现了手动过一下再试。
HEADLESS = False

# 是否保存登录状态
SAVE_LOGIN_STATE = True

# 数据保存类型选项配置,支持三种类型：csv、db、json, 最好保存到DB，有排重的功能。
SAVE_DATA_OPTION = "db"  # csv or db or json

# 用户浏览器缓存的浏览器文件配置
USER_DATA_DIR = "%s_user_data_dir"  # %s will be replaced by platform name

# 爬取开始页数 默认从第一页开始
START_PAGE = 1

# 爬取视频/帖子的数量控制
CRAWLER_MAX_NOTES_COUNT = 200

# 爬取开始的天数，仅支持 bilibili 关键字搜索，YYYY-MM-DD 格式，若为 None 则表示不设置时间范围，按照默认关键字最多返回 1000 条视频的结果处理
START_DAY = '2024-01-01'

# 爬取结束的天数，仅支持 bilibili 关键字搜索，YYYY-MM-DD 格式，若为 None 则表示不设置时间范围，按照默认关键字最多返回 1000 条视频的结果处理
END_DAY = '2024-01-01'

# 是否开启按每一天进行爬取的选项，仅支持 bilibili 关键字搜索
# 若为 False，则忽略 START_DAY 与 END_DAY 设置的值
# 若为 True，则按照 START_DAY 至 END_DAY 按照每一天进行筛选，这样能够突破 1000 条视频的限制，最大程度爬取该关键词下的所有视频
ALL_DAY = True

# 并发爬虫数量控制
MAX_CONCURRENCY_NUM = 2

# 是否开启爬图片模式, 默认不开启爬图片
ENABLE_GET_IMAGES = False

# 是否开启爬评论模式, 默认开启爬评论
ENABLE_GET_COMMENTS = True

# 爬取一级评论的数量控制(单视频/帖子)
CRAWLER_MAX_COMMENTS_COUNT_SINGLENOTES = 1000

# 是否开启爬二级评论模式, 默认不开启爬二级评论
# 老版本项目使用了 db, 则需参考 schema/tables.sql line 287 增加表字段
ENABLE_GET_SUB_COMMENTS = True

# 已废弃⚠️⚠️⚠️指定小红书需要爬虫的笔记ID列表
# 已废弃⚠️⚠️⚠️ 指定笔记ID笔记列表会因为缺少xsec_token和xsec_source参数导致爬取失败
# XHS_SPECIFIED_ID_LIST = [
#     "66fad51c000000001b0224b8",
#     # ........................
# ]

# 指定小红书需要爬虫的笔记URL列表, 目前要携带xsec_token和xsec_source参数
XHS_SPECIFIED_NOTE_URL_LIST = [
    "https://www.xiaohongshu.com/explore/66fad51c000000001b0224b8?xsec_token=AB3rO-QopW5sgrJ41GwN01WCXh6yWPxjSoFI9D5JIMgKw=&xsec_source=pc_search"
    # ........................
]

# 指定抖音需要爬取的ID列表
DY_SPECIFIED_ID_LIST = [
    "7280854932641664319",
    "7202432992642387233",
    # ........................
]

# 指定快手平台需要爬取的ID列表
KS_SPECIFIED_ID_LIST = ["3xf8enb8dbj6uig", "3x6zz972bchmvqe"]

# 指定B站平台需要爬取的视频bvid列表
BILI_SPECIFIED_ID_LIST = [
    "BV1d54y1g7db",
    "BV1Sz4y1U77N",
    "BV14Q4y1n7jz",
    # ........................
]

# 指定微博平台需要爬取的帖子列表
WEIBO_SPECIFIED_ID_LIST = [
    "4982041758140155",
    # ........................
]

# 指定weibo创作者ID列表
WEIBO_CREATOR_ID_LIST = [
    "5533390220",
    # ........................
]

# 指定贴吧需要爬取的帖子列表
TIEBA_SPECIFIED_ID_LIST = []

# 指定贴吧名称列表，爬取该贴吧下的帖子
TIEBA_NAME_LIST = [
    # "盗墓笔记"
]

# 指定贴吧创作者URL列表
TIEBA_CREATOR_URL_LIST = [
    "https://tieba.baidu.com/home/main/?id=tb.1.7f139e2e.6CyEwxu3VJruH_-QqpCi6g&fr=frs",
    # ........................
]

XHS_CREATOR_ID_LIST = []
# 指定小红书创作者ID列表
# XHS_CREATOR_ID_LIST = [
#     "63e36c9a000000002703502b",
#     # ........................
# ]

# 异步查询函数
async def fetch_data():
    global XHS_CREATOR_ID_LIST
    # 数据库连接配置
    config = {
        'host': "",        # 替换为你的 MySQL 主机地址
        'port': 0,
        'user': "",        # 替换为你的 MySQL 用户名
        'password': "",# 替换为你的 MySQL 密码
        'db': "",       # 替换为你的 MySQL 数据库名
        'charset': 'utf8mb4',             # 确保支持 Unicode 字符
        'autocommit': True
    }


    # SQL 查询
    query = """
    SELECT t1.user_id
FROM
(
    SELECT DISTINCT user_id
    FROM xhs_note_comment
    WHERE ip_location = '美国'
    AND nickname != 'momo'
    AND nickname REGEXP '^[A-Za-z[:punct:] ]+$'  -- Nickname contains only English letters, punctuation, and spaces
    AND nickname NOT REGEXP '[一-龯]'  -- Excludes Chinese characters from nickname (characters from the CJK Unified Ideographs range)
    AND content REGEXP '^[A-Za-z[:punct:] ]+$'  -- Content contains only English letters, punctuation, and spaces
    AND content NOT REGEXP '[一-龯]'  -- Excludes Chinese characters from content
) t1
LEFT JOIN
(
    SELECT DISTINCT user_id
    FROM xhs_creator
) t2
ON t1.user_id = t2.user_id
WHERE t2.user_id IS NULL
order by t1.user_id desc
;
    """

    # 结果存储列表
    result_list = []
    pool = None
    # 异步连接到数据库并执行查询
    try:
        # 创建连接池
        pool = await aiomysql.create_pool(**config)
        async with pool.acquire() as connection:
            async with connection.cursor() as cursor:
                # 执行查询
                await cursor.execute(query)
                results = await cursor.fetchall()

                # 将查询结果存储到列表
                XHS_CREATOR_ID_LIST = [row[0] for row in results]

    except Exception as e:
        print(f"Error: {e}")
    finally:
        if pool:
            # 确保连接池关闭
            pool.close()
            await pool.wait_closed()

    # 返回结果列表
    return result_list

# 主函数
async def fetch_usr():
    # 获取查询结果
    await fetch_data()

# 运行异步主函数
asyncio.run(fetch_usr())

# 指定Dy创作者ID列表(sec_id)
DY_CREATOR_ID_LIST = [
    "MS4wLjABAAAATJPY7LAlaa5X-c8uNdWkvz0jUGgpw4eeXIwu_8BhvqE",
    # ........................
]

# 指定bili创作者ID列表(sec_id)
BILI_CREATOR_ID_LIST = [
    "20813884",
    # ........................
]

# 指定快手创作者ID列表
KS_CREATOR_ID_LIST = [
    "3x4sm73aye7jq7i",
    # ........................
]


# 指定知乎创作者主页url列表
ZHIHU_CREATOR_URL_LIST = [
    "https://www.zhihu.com/people/yd1234567",
    # ........................
]

# 指定知乎需要爬取的帖子ID列表
ZHIHU_SPECIFIED_ID_LIST = [
    "https://www.zhihu.com/question/826896610/answer/4885821440", # 回答
    "https://zhuanlan.zhihu.com/p/673461588", # 文章
    "https://www.zhihu.com/zvideo/1539542068422144000" # 视频
]

# 词云相关
# 是否开启生成评论词云图
ENABLE_GET_WORDCLOUD = False
# 自定义词语及其分组
# 添加规则：xx:yy 其中xx为自定义添加的词组，yy为将xx该词组分到的组名。
CUSTOM_WORDS = {
    "零几": "年份",  # 将“零几”识别为一个整体
    "高频词": "专业术语",  # 示例自定义词
}

# 停用(禁用)词文件路径
STOP_WORDS_FILE = "./docs/hit_stopwords.txt"

# 中文字体文件路径
FONT_PATH = "./docs/STZHONGS.TTF"
