def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Education", "instances": 34, "metric_value": 0.9597, "depth": 1}
	if obj[1]<=3:
		# {"feature": "Occupation", "instances": 29, "metric_value": 0.9923, "depth": 2}
		if obj[2]<=7:
			# {"feature": "Coupon", "instances": 21, "metric_value": 0.9183, "depth": 3}
			if obj[0]>1:
				return 'True'
			elif obj[0]<=1:
				return 'True'
			else: return 'True'
		elif obj[2]>7:
			# {"feature": "Coupon", "instances": 8, "metric_value": 0.8113, "depth": 3}
			if obj[0]>0:
				return 'False'
			elif obj[0]<=0:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[1]>3:
		return 'True'
	else: return 'True'
