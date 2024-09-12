from flask import Flask, render_template_string
import yfinance as yf
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def msos_data():
    end_date = datetime.now().strftime('%Y-%m-%d')
    msos_stock = yf.download('MSOS', start='2024-01-01', end=end_date)
    
    data = {
        "latest_close": f"${msos_stock['Close'][-1]:.2f}",
        "highest_price": f"${msos_stock['High'].max():.2f}",
        "lowest_price": f"${msos_stock['Low'].min():.2f}",
        "avg_volume": f"{msos_stock['Volume'].mean():.0f}",
        "last_updated": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    
    html = """
    <h1>MSOS Stock Data</h1>
    <p>Latest closing price: {{ data.latest_close }}</p>
    <p>Highest price since 1/1/2024: {{ data.highest_price }}</p>
    <p>Lowest price since 1/1/2024: {{ data.lowest_price }}</p>
    <p>Average daily trading volume: {{ data.avg_volume }}</p>
    <p>Last updated: {{ data.last_updated }}</p>
    """
    
    return render_template_string(html, data=data)

if __name__ == '__main__':
    app.run(debug=True)