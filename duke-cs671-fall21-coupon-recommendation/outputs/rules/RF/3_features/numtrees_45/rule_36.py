def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.8281, "depth": 1}
	if obj[2]<=5:
		# {"feature": "Coupon", "instances": 12, "metric_value": 0.4138, "depth": 2}
		if obj[0]>0:
			return 'True'
		elif obj[0]<=0:
			# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[1]>0:
				return 'True'
			elif obj[1]<=0:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[2]>5:
		# {"feature": "Coupon", "instances": 11, "metric_value": 0.994, "depth": 2}
		if obj[0]<=3:
			# {"feature": "Education", "instances": 10, "metric_value": 0.971, "depth": 3}
			if obj[1]<=2:
				return 'False'
			elif obj[1]>2:
				return 'True'
			else: return 'True'
		elif obj[0]>3:
			return 'False'
		else: return 'False'
	else: return 'True'
