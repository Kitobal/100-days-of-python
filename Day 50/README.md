# Day 50: Automatic Tinder Swiper
Could not test this, is basicaly the code from the course, it works in theory, but the Xpaths of tinder change with every request so it does not.<br>
The only new thing that this class taught was the code for changing focus to popup windows in selenium<br>
```
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
```
