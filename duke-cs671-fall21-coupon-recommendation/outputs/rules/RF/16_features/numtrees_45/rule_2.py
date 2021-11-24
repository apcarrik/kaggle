def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Income", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[10]>0:
		# {"feature": "Time", "instances": 16, "metric_value": 0.896, "depth": 2}
		if obj[2]<=2:
			# {"feature": "Weather", "instances": 11, "metric_value": 0.4395, "depth": 3}
			if obj[1]<=1:
				return 'False'
			elif obj[1]>1:
				return 'True'
			else: return 'True'
		elif obj[2]>2:
			# {"feature": "Bar", "instances": 5, "metric_value": 0.7219, "depth": 3}
			if obj[11]<=2.0:
				return 'True'
			elif obj[11]>2.0:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[10]<=0:
		return 'True'
	else: return 'True'
