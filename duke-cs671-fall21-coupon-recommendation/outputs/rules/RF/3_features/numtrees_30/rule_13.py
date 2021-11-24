def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.9367, "depth": 1}
	if obj[0]>1:
		# {"feature": "Education", "instances": 22, "metric_value": 0.684, "depth": 2}
		if obj[1]<=3:
			# {"feature": "Occupation", "instances": 21, "metric_value": 0.5917, "depth": 3}
			if obj[2]>2:
				return 'True'
			elif obj[2]<=2:
				return 'True'
			else: return 'True'
		elif obj[1]>3:
			return 'False'
		else: return 'False'
	elif obj[0]<=1:
		# {"feature": "Occupation", "instances": 12, "metric_value": 0.9183, "depth": 2}
		if obj[2]>5:
			# {"feature": "Education", "instances": 9, "metric_value": 0.5033, "depth": 3}
			if obj[1]>1:
				return 'False'
			elif obj[1]<=1:
				return 'False'
			else: return 'False'
		elif obj[2]<=5:
			return 'True'
		else: return 'True'
	else: return 'False'
