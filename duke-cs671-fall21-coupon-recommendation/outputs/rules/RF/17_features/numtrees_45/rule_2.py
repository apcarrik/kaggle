def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Coffeehouse", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[13]>1.0:
		# {"feature": "Occupation", "instances": 12, "metric_value": 0.4138, "depth": 2}
		if obj[10]<=11:
			return 'True'
		elif obj[10]>11:
			return 'False'
		else: return 'False'
	elif obj[13]<=1.0:
		# {"feature": "Coupon", "instances": 11, "metric_value": 0.684, "depth": 2}
		if obj[3]>2:
			return 'False'
		elif obj[3]<=2:
			# {"feature": "Time", "instances": 4, "metric_value": 1.0, "depth": 3}
			if obj[2]<=2:
				return 'True'
			elif obj[2]>2:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
