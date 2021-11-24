def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.8281, "depth": 1}
	if obj[2]>4:
		# {"feature": "Coupon", "instances": 17, "metric_value": 0.9367, "depth": 2}
		if obj[0]>1:
			# {"feature": "Education", "instances": 12, "metric_value": 0.8113, "depth": 3}
			if obj[1]<=3:
				return 'True'
			elif obj[1]>3:
				return 'True'
			else: return 'True'
		elif obj[0]<=1:
			# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 3}
			if obj[1]<=2:
				return 'True'
			elif obj[1]>2:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[2]<=4:
		return 'True'
	else: return 'True'
