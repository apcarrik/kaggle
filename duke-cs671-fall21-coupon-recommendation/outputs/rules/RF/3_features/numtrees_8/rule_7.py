def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Coupon", "instances": 127, "metric_value": 0.9719, "depth": 1}
	if obj[0]>1:
		# {"feature": "Occupation", "instances": 97, "metric_value": 0.9039, "depth": 2}
		if obj[2]<=12:
			# {"feature": "Education", "instances": 83, "metric_value": 0.8515, "depth": 3}
			if obj[1]>1:
				return 'True'
			elif obj[1]<=1:
				return 'True'
			else: return 'True'
		elif obj[2]>12:
			# {"feature": "Education", "instances": 14, "metric_value": 0.9852, "depth": 3}
			if obj[1]<=3:
				return 'False'
			elif obj[1]>3:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[0]<=1:
		# {"feature": "Education", "instances": 30, "metric_value": 0.9183, "depth": 2}
		if obj[1]<=3:
			# {"feature": "Occupation", "instances": 28, "metric_value": 0.9403, "depth": 3}
			if obj[2]>1:
				return 'False'
			elif obj[2]<=1:
				return 'False'
			else: return 'False'
		elif obj[1]>3:
			return 'False'
		else: return 'False'
	else: return 'False'
