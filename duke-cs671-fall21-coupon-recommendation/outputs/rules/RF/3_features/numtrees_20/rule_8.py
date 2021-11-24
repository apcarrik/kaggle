def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Occupation", "instances": 51, "metric_value": 0.9367, "depth": 1}
	if obj[2]>3:
		# {"feature": "Coupon", "instances": 43, "metric_value": 0.9808, "depth": 2}
		if obj[0]>1:
			# {"feature": "Education", "instances": 28, "metric_value": 0.9059, "depth": 3}
			if obj[1]<=3:
				return 'True'
			elif obj[1]>3:
				return 'True'
			else: return 'True'
		elif obj[0]<=1:
			# {"feature": "Education", "instances": 15, "metric_value": 0.971, "depth": 3}
			if obj[1]<=2:
				return 'False'
			elif obj[1]>2:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[2]<=3:
		return 'True'
	else: return 'True'
