# TwitterAutomation
this is a bot that loops through each follower of a specific twitter account and check their recent 5 tweets. if their tweet founds to be offensive or negative the bot will automatically block them. and continues to check other followers.

## Requirements
First you need to import required libraries as follows

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
```

then you need to download chrome web driver in order to automate Twitter.com and then add its path into your code like this.

```python
driver = webdriver.Chrome('C:/Users/userx/chromewebdriver/chromedriver.exe')
driver.get('https://twitter.com/')
```

you can find what it looks like in when it finally runs on youtube.
https://www.youtube.com/watch?v=YzN4GfoOjLU
