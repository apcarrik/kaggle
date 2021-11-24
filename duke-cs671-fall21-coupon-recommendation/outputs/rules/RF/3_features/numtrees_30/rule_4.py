def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Occupation", "instances": 34, "metric_value": 0.9082, "depth": 1}
	if obj[2]<=10:
		# {"feature": "Education", "instances": 27, "metric_value": 0.7642, "depth": 2}
		if obj[1]>0:
			# {"feature": "Coupon", "instances": 17, "metric_value": 0.9367, "depth": 3}
			if obj[0]>0:
				return 'True'
			elif obj[0]<=0:
				return 'False'
			else: return 'False'
		elif obj[1]<=0:
			return 'True'
		else: return 'True'
	elif obj[2]>10:
		# {"feature": "Coupon", "instances": 7, "metric_value": 0.8631, "depth": 2}
		if obj[0]>1:
			# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 3}
			if obj[1]<=3:
				return 'True'
			elif obj[1]>3:
				return 'False'
			else: return 'False'
		elif obj[0]<=1:
			return 'False'
		else: return 'False'
	else: return 'False'
