# Stock Analysis

### Get the code running

```
pip install -r requirements.txt
streamlit run application.py
```

### Fre APIs to get data

- [Alpha Vantage](https://www.alphavantage.co/documentation/)
- [Coin API](https://www.coinapi.io/Pricing)
- [finnhub.io](https://finnhub.io/pricing)
- [Binanace](https://github.com/binance/binance-spot-api-docs)
- [Nomics](https://nomics.com/docs/)
- [WazirX](https://github.com/WazirX/wazirx-api)
- [Market Stack](https://marketstack.com/)

### Youtube links

- [lots of trading app videos](https://www.youtube.com/c/parttimelarry/playlists)

### Resources

-[Financial Charts](https://plotly.com/python/financial-charts/)

- [Streamlit with plotly](https://medium.com/swlh/building-interactive-dashboard-with-plotly-and-streamlit-2c390bcfd41a)

### Nice charts to implement later

- [Radar Chart](https://towardsdatascience.com/how-to-make-stunning-radar-charts-with-python-implemented-in-matplotlib-and-plotly-91e21801d8ca)

## Stuck?

### Creating a virtual environment

- Check python version and then if pip is installed properly

  ```bash
  python --version
  pip -h
  ```

- Install Virtualenv using `pip install virtualenv` and create an environment
  ```
  virtualenv env
  #or if this doesn't work
  [path to python installation folder]/python.exe -m venv env
  ```
  - Activate **env**
  ```
  #on Windows
  .\env\Scripts\activate
  #on Linux
  source env/bin/activate
  ```

### Heroku

```
heroku login
heroku create knownowanalysis
git push heroku master

```
