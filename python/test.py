from SMS import SMS

sms = SMS(
	username='test_account@email.com',
	password='my_password',
	originator='MyName',
	hostname='solutions4mobiles.com',
	phone='901231231212',
	msgtext='Hello!')

print sms.send()
