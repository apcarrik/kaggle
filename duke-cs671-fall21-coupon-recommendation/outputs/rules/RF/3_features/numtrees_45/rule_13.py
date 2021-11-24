def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[2]<=12:
		# {"feature": "Education", "instances": 21, "metric_value": 0.9984, "depth": 2}
		if obj[1]<=3:
			# {"feature": "Coupon", "instances": 19, "metric_value": 0.9819, "depth": 3}
			if obj[0]>0:
				return 'True'
			elif obj[0]<=0:
				return 'False'
			else: return 'False'
		elif obj[1]>3:
			return 'False'
		else: return 'False'
	elif obj[2]>12:
		return 'True'
	else: return 'True'
