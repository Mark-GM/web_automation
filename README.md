### Experimental: Use at your own risk!
<br>


```shell
# install firefox webdriver
wget https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux64.tar.gz
tar -xvzf geckodriver-v0.30.0-linux64.tar.gz
chmod a+x geckodriver
sudo mv geckodriver /usr/local/bin/

# prepare selenium environment
python3 -m venv selenium_env
. selenium_env/bin/activate
pip install -U pip wheel
pip install -U python-dotenv selenium
```