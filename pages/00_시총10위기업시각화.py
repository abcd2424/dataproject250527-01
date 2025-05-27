import yfinance as yf
import plotly.graph_objects as go
from datetime import datetime, timedelta

# 시가총액 기준 상위 10개 기업의 티커
tickers = ["MSFT", "AAPL", "NVDA", "2222.SR", "GOOGL", "AMZN", "BRK-B", "META", "TSM", "LLY"]

# 날짜 범위 설정 (최근 6개월)
end_date = datetime.today()
start_date = end_date - timedelta(days=180)

# 데이터 수집 및 시각화
fig = go.Figure()

for ticker in tickers:
    try:
        data = yf.download(ticker, start=start_date, end=end_date)
        fig.add_trace(go.Scatter(x=data.index, y=data['Close'], mode='lines', name=ticker))
    except Exception as e:
        print(f"{ticker} 데이터 로딩 중 오류 발생: {e}")

# 그래프 설정
fig.update_layout(
    title="글로벌 시가총액 상위 10개 기업 주가 추이 (최근 6개월)",
    xaxis_title="날짜",
    yaxis_title="주가 (USD)",
    template="plotly_dark",
    hovermode="x unified"
)

fig.show()
