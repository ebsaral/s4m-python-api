<h1>s4m-python-api</h1>
<p>version: 0.8</p>
==============

<h2>solutions4mobiles SMS Python API</h2>

<h3>Requirements:</h3>
<ul>
<li><a href="http://docs.python-requests.org/en/latest/">python requests</a></li>
</ul>

<h3>Usage:</h3>
<ul>
<li>Initialize SMS class with arguments:<br/><code>sms = SMS(hostname='123.123.123.123', username='my_username', password='my_password')</code></li>
<li>or without arguments: <code>sms = SMS()</code>. Then update any of attributes if you want:<br/><code>sms.hostname = '123.123.123.123'</code>, <code>sms.username = 'my_username'</code>, <code>sms.password = 'my_password'</code></li>
<li>Finally, fly your SMS: <code>sms.send()</code></li>
</ul>

<p>This Python class is written by using examples from
http://www.solutions4mobiles.com/en/developer-network/apis.html</p>

<p>Using the API of http://www.solutions4mobiles.com for SMS Messaging</p>
<p>Please contact http://www.solutions4mobiles.com to use their paid services</p>
<hr>
<p><a href="http://www.eminbugrasaral.com/">Emin Buğra Saral</a> - 2014</p>
