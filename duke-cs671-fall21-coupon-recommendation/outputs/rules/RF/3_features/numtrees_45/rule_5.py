def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[2]<=12:
		# {"feature": "Coupon", "instances": 20, "metric_value": 0.8813, "depth": 2}
		if obj[0]<=3:
			# {"feature": "Education", "instances": 14, "metric_value": 0.9403, "depth": 3}
			if obj[1]<=3:
				return 'True'
			elif obj[1]>3:
				return 'False'
			else: return 'False'
		elif obj[0]>3:
			# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 3}
			if obj[1]>0:
				return 'True'
			elif obj[1]<=0:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[2]>12:
		return 'False'
	else: return 'False'
