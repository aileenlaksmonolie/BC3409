#!/usr/bin/env python
# coding: utf-8

# In[48]:


from flask import Flask, request, render_template
import joblib
app = Flask(__name__)


# In[49]:


#decorator -> Run this first before the next function
@app.route('/', methods =["GET","POST"])
def index():
    if request.method == "POST":
        rates = float(request.form.get("rates"))

        model1 = joblib.load("regression")
        prediction1 = model1.predict([[rates]])[0]
        
        model2 = joblib.load("tree")
        prediction2 = model2.predict([[rates]])[0]
        
        return render_template('index.html',result1=prediction1,result2=prediction2)
    else:
        return render_template('index.html',result1="waiting",result2="waiting")


# In[ ]:


if __name__ == '__main__':
    app.run()


# In[ ]:




