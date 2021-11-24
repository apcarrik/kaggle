def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Education", "instances": 23, "metric_value": 0.8281, "depth": 1}
	if obj[1]<=2:
		# {"feature": "Occupation", "instances": 18, "metric_value": 0.9183, "depth": 2}
		if obj[2]<=7:
			# {"feature": "Coupon", "instances": 14, "metric_value": 0.9852, "depth": 3}
			if obj[0]<=3:
				return 'True'
			elif obj[0]>3:
				return 'False'
			else: return 'False'
		elif obj[2]>7:
			return 'False'
		else: return 'False'
	elif obj[1]>2:
		return 'False'
	else: return 'False'
