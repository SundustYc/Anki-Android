import uiautomator2 as u2

d = u2.connect('7d5caacf') # connect to device
d.xpath('//*[@resource-id="com.ichi2.anki.debug:id/files"]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]').click()
d(resourceId="com.ichi2.anki.debug:id/snackbar_action").click()
d.click(0.064, 0.719)
d(resourceId="com.ichi2.anki.debug:id/id_note_editText", description="背面").click()
d.click(0.064, 0.719)
d(resourceId="com.ichi2.anki.debug:id/action_save").click()
d(description="转到上一层级").click()
d.xpath('//*[@resource-id="com.ichi2.anki.debug:id/files"]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]').click()
d(description="更多选项").click()
d.xpath('//android.widget.ListView/android.widget.LinearLayout[6]').click()
d(resourceId="android:id/button1").click()