questions = [
    {"word": "abandon", "choices": ["達成する", "捨てる", "改善する", "選ぶ"], "answer": "捨てる"},
    {"word": "achieve", "choices": ["購入する", "避ける", "達成する", "説明する"], "answer": "達成する"},
    {"word": "improve", "choices": ["選ぶ", "借りる", "改善する", "失う"], "answer": "改善する"},
    {"word": "purchase", "choices": ["購入する", "達成する", "拒否する", "説明する"], "answer": "購入する"},
    {"word": "avoid", "choices": ["改善する", "選ぶ", "提供する", "避ける"], "answer": "避ける"},
    {"word": "provide", "choices": ["避ける", "失う", "提供する", "説明する"], "answer": "提供する"},
    {"word": "explain", "choices": ["選ぶ", "説明する", "購入する", "達成する"], "answer": "説明する"},
    {"word": "select", "choices": ["選ぶ", "提供する", "失う", "借りる"], "answer": "選ぶ"},
    {"word": "lose", "choices": ["説明する", "改善する", "失う", "購入する"], "answer": "失う"},
    {"word": "borrow", "choices": ["達成する", "借りる", "避ける", "選ぶ"], "answer": "借りる"},

    {"word": "require", "choices": ["拒否する", "必要とする", "売る", "修理する"], "answer": "必要とする"},
    {"word": "accept", "choices": ["受け入れる", "拒否する", "借りる", "失う"], "answer": "受け入れる"},
    {"word": "refuse", "choices": ["受け入れる", "説明する", "拒否する", "購入する"], "answer": "拒否する"},
    {"word": "increase", "choices": ["減少する", "増加する", "選ぶ", "借りる"], "answer": "増加する"},
    {"word": "decrease", "choices": ["減少する", "増加する", "提供する", "達成する"], "answer": "減少する"},
    {"word": "include", "choices": ["除外する", "修理する", "避ける", "含む"], "answer": "含む"},
    {"word": "receive", "choices": ["受け取る", "送る", "失う", "選ぶ"], "answer": "受け取る"},
    {"word": "deliver", "choices": ["受け取る", "借りる", "説明する", "配達する"], "answer": "配達する"},
    {"word": "attend", "choices": ["欠席する", "購入する", "出席する", "避ける"], "answer": "出席する"},
    {"word": "cancel", "choices": ["予約する", "キャンセルする", "達成する", "提供する"], "answer": "キャンセルする"},

    {"word": "reserve", "choices": ["予約する", "キャンセルする", "修理する", "失う"], "answer": "予約する"},
    {"word": "schedule", "choices": ["拒否する", "借りる", "購入する", "予定を組む"], "answer": "予定を組む"},
    {"word": "available", "choices": ["高価な", "危険な", "利用できる", "遅い"], "answer": "利用できる"},
    {"word": "expensive", "choices": ["安価な", "高価な", "便利な", "空いている"], "answer": "高価な"},
    {"word": "convenient", "choices": ["高価な", "遅い", "便利な", "危険な"], "answer": "便利な"},
    {"word": "necessary", "choices": ["珍しい", "無料の", "古い", "必要な"], "answer": "必要な"},
    {"word": "recent", "choices": ["最近の", "古い", "高価な", "便利な"], "answer": "最近の"},
    {"word": "annual", "choices": ["毎日の", "毎週の", "年1回の", "毎月の"], "answer": "年1回の"},
    {"word": "employee", "choices": ["顧客", "従業員", "経営者", "訪問者"], "answer": "従業員"},
    {"word": "customer", "choices": ["従業員", "会社", "商品", "顧客"], "answer": "顧客"},

    {"word": "manager", "choices": ["顧客", "経営者・管理者", "会社", "従業員"], "answer": "経営者・管理者"},
    {"word": "company", "choices": ["商品", "契約", "会社", "会議"], "answer": "会社"},
    {"word": "product", "choices": ["商品", "顧客", "支店", "従業員"], "answer": "商品"},
    {"word": "service", "choices": ["給料", "契約", "サービス", "予定"], "answer": "サービス"},
    {"word": "contract", "choices": ["請求書", "商品", "会議", "契約"], "answer": "契約"},
    {"word": "meeting", "choices": ["会議", "予約", "契約", "出張"], "answer": "会議"},
    {"word": "appointment", "choices": ["商品", "予約・約束", "会社", "給料"], "answer": "予約・約束"},
    {"word": "department", "choices": ["部門", "顧客", "建物", "商品"], "answer": "部門"},
    {"word": "office", "choices": ["工場", "駅", "事務所", "店舗"], "answer": "事務所"},
    {"word": "branch", "choices": ["本社", "商品", "契約", "支店"], "answer": "支店"},

    {"word": "salary", "choices": ["契約", "給料", "休暇", "費用"], "answer": "給料"},
    {"word": "benefit", "choices": ["損失", "請求書", "福利厚生・利益", "予定"], "answer": "福利厚生・利益"},
    {"word": "vacation", "choices": ["会議", "給料", "出張", "休暇"], "answer": "休暇"},
    {"word": "business", "choices": ["事業・仕事", "商品", "顧客", "建物"], "answer": "事業・仕事"},
    {"word": "career", "choices": ["契約", "職歴・キャリア", "給料", "休暇"], "answer": "職歴・キャリア"},
    {"word": "experience", "choices": ["予定", "商品", "経験", "費用"], "answer": "経験"},
    {"word": "information", "choices": ["契約", "会議", "会社", "情報"], "answer": "情報"},
    {"word": "application", "choices": ["商品", "支店", "申込書・応募", "従業員"], "answer": "申込書・応募"},
    {"word": "document", "choices": ["書類", "商品", "会議", "給料"], "answer": "書類"},
    {"word": "report", "choices": ["契約", "報告書", "予約", "商品"], "answer": "報告書"},

    {"word": "invoice", "choices": ["請求書", "領収書", "契約", "予定"], "answer": "請求書"},
    {"word": "receipt", "choices": ["請求書", "商品", "領収書", "会議"], "answer": "領収書"},
    {"word": "cost", "choices": ["利益", "給料", "費用", "契約"], "answer": "費用"},
    {"word": "profit", "choices": ["費用", "利益", "損失", "給料"], "answer": "利益"},
    {"word": "loss", "choices": ["利益", "費用", "損失", "売上"], "answer": "損失"},
    {"word": "sales", "choices": ["費用", "契約", "給料", "売上・販売"], "answer": "売上・販売"},
    {"word": "price", "choices": ["価格", "利益", "商品", "契約"], "answer": "価格"},
    {"word": "discount", "choices": ["価格", "割引", "利益", "請求書"], "answer": "割引"},
    {"word": "offer", "choices": ["拒否", "購入", "提供・申し出", "修理"], "answer": "提供・申し出"},
    {"word": "order", "choices": ["注文", "配達", "返品", "修理"], "answer": "注文"},

    {"word": "ship", "choices": ["発送する", "受け取る", "予約する", "購入する"], "answer": "発送する"},
    {"word": "return", "choices": ["購入する", "返品する・戻る", "発送する", "修理する"], "answer": "返品する・戻る"},
    {"word": "repair", "choices": ["購入する", "返品する", "修理する", "配達する"], "answer": "修理する"},
    {"word": "replace", "choices": ["交換する", "購入する", "予約する", "説明する"], "answer": "交換する"},
    {"word": "maintain", "choices": ["減らす", "購入する", "拒否する", "維持する"], "answer": "維持する"},
    {"word": "prepare", "choices": ["説明する", "準備する", "購入する", "避ける"], "answer": "準備する"},
    {"word": "complete", "choices": ["完了する", "開始する", "拒否する", "借りる"], "answer": "完了する"},
    {"word": "continue", "choices": ["終了する", "避ける", "続ける", "選ぶ"], "answer": "続ける"},
    {"word": "delay", "choices": ["開始する", "完了する", "予約する", "遅らせる・遅れる"], "answer": "遅らせる・遅れる"},
    {"word": "arrange", "choices": ["拒否する", "手配する・整理する", "購入する", "失う"], "answer": "手配する・整理する"},

    {"word": "confirm", "choices": ["拒否する", "購入する", "確認する", "修理する"], "answer": "確認する"},
    {"word": "contact", "choices": ["避ける", "連絡する", "購入する", "借りる"], "answer": "連絡する"},
    {"word": "discuss", "choices": ["話し合う", "拒否する", "購入する", "配達する"], "answer": "話し合う"},
    {"word": "decide", "choices": ["説明する", "借りる", "修理する", "決める"], "answer": "決める"},
    {"word": "consider", "choices": ["拒否する", "検討する", "購入する", "配達する"], "answer": "検討する"},
    {"word": "suggest", "choices": ["提案する", "拒否する", "失う", "借りる"], "answer": "提案する"},
    {"word": "recommend", "choices": ["避ける", "修理する", "推薦する", "拒否する"], "answer": "推薦する"},
    {"word": "agree", "choices": ["拒否する", "失う", "同意する", "購入する"], "answer": "同意する"},
    {"word": "disagree", "choices": ["同意する", "意見が合わない", "説明する", "選ぶ"], "answer": "意見が合わない"},
    {"word": "allow", "choices": ["拒否する", "避ける", "許可する", "失う"], "answer": "許可する"},

    {"word": "prevent", "choices": ["許可する", "購入する", "説明する", "防ぐ"], "answer": "防ぐ"},
    {"word": "expect", "choices": ["予想する・期待する", "拒否する", "借りる", "修理する"], "answer": "予想する・期待する"},
    {"word": "depend", "choices": ["提供する", "購入する", "依存する", "説明する"], "answer": "依存する"},
    {"word": "reduce", "choices": ["増やす", "減らす", "選ぶ", "借りる"], "answer": "減らす"},
    {"word": "remain", "choices": ["増加する", "購入する", "配達する", "残る"], "answer": "残る"},
    {"word": "local", "choices": ["地元の", "国際的な", "高価な", "危険な"], "answer": "地元の"},
    {"word": "international", "choices": ["地元の", "国際的な", "古い", "便利な"], "answer": "国際的な"},
    {"word": "public", "choices": ["個人的な", "高価な", "公共の", "最近の"], "answer": "公共の"},
    {"word": "private", "choices": ["公共の", "個人的な・私的な", "無料の", "便利な"], "answer": "個人的な・私的な"},
    {"word": "similar", "choices": ["似ている", "異なる", "危険な", "高価な"], "answer": "似ている"},

    {"word": "different", "choices": ["似ている", "異なる", "便利な", "最近の"], "answer": "異なる"},
    {"word": "possible", "choices": ["不可能な", "必要な", "可能な", "危険な"], "answer": "可能な"},
    {"word": "likely", "choices": ["珍しい", "ありそうな", "危険な", "無料の"], "answer": "ありそうな"},
    {"word": "specific", "choices": ["一般的な", "高価な", "古い", "具体的な"], "answer": "具体的な"},
    {"word": "general", "choices": ["一般的な", "具体的な", "危険な", "最近の"], "answer": "一般的な"},
    {"word": "successful", "choices": ["失敗した", "危険な", "遅い", "成功した"], "answer": "成功した"},
    {"word": "popular", "choices": ["人気のある", "珍しい", "高価な", "古い"], "answer": "人気のある"},
    {"word": "professional", "choices": ["個人的な", "無料の", "専門的な・プロの", "危険な"], "answer": "専門的な・プロの"},
    {"word": "temporary", "choices": ["一時的な", "永久的な", "最近の", "便利な"], "answer": "一時的な"},
    {"word": "permanent", "choices": ["一時的な", "永久的な", "高価な", "危険な"], "answer": "永久的な"},

    {"word": "familiar", "choices": ["珍しい", "危険な", "高価な", "よく知っている・馴染みのある"], "answer": "よく知っている・馴染みのある"},
    {"word": "foreign", "choices": ["地元の", "外国の", "公共の", "便利な"], "answer": "外国の"},
    {"word": "efficient", "choices": ["危険な", "高価な", "効率的な", "一時的な"], "answer": "効率的な"},
    {"word": "effective", "choices": ["珍しい", "効果的な", "古い", "無料の"], "answer": "効果的な"},
    {"word": "reliable", "choices": ["信頼できる", "危険な", "一時的な", "高価な"], "answer": "信頼できる"},
    {"word": "accurate", "choices": ["遅い", "正確な", "高価な", "珍しい"], "answer": "正確な"},
    {"word": "appropriate", "choices": ["不適切な", "高価な", "適切な", "危険な"], "answer": "適切な"},
    {"word": "responsible", "choices": ["責任がある", "無料の", "古い", "便利な"], "answer": "責任がある"},
    {"word": "deadline", "choices": ["会議", "締め切り", "契約", "休暇"], "answer": "締め切り"}
]
import random

questions = questions[:100]

# 正解位置を25問ずつ用意
positions = [0] * 25 + [1] * 25 + [2] * 25 + [3] * 25

# 正解位置の順番をランダムにする
random.shuffle(positions)

for question, position in zip(questions, positions):
    correct = question["answer"]

    # 正解以外の3つ
    wrong_choices = [
        choice for choice in question["choices"]
        if choice != correct
    ]

    # 3つの不正解選択肢をランダムに並べる
    random.shuffle(wrong_choices)

    # 指定された位置に正解を入れる
    choices = wrong_choices.copy()
    choices.insert(position, correct)

    question["choices"] = choices
