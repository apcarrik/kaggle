def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Coupon", "instances": 85, "metric_value": 0.9975, "depth": 1}
	if obj[0]<=3:
		# {"feature": "Occupation", "instances": 58, "metric_value": 0.9576, "depth": 2}
		if obj[2]<=7:
			# {"feature": "Education", "instances": 38, "metric_value": 0.992, "depth": 3}
			if obj[1]<=3:
				return 'True'
			elif obj[1]>3:
				return 'False'
			else: return 'False'
		elif obj[2]>7:
			# {"feature": "Education", "instances": 20, "metric_value": 0.8113, "depth": 3}
			if obj[1]>1:
				return 'True'
			elif obj[1]<=1:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[0]>3:
		# {"feature": "Occupation", "instances": 27, "metric_value": 0.9183, "depth": 2}
		if obj[2]<=5:
			# {"feature": "Education", "instances": 14, "metric_value": 1.0, "depth": 3}
			if obj[1]<=3:
				return 'False'
			elif obj[1]>3:
				return 'True'
			else: return 'True'
		elif obj[2]>5:
			# {"feature": "Education", "instances": 13, "metric_value": 0.6194, "depth": 3}
			if obj[1]<=2:
				return 'False'
			elif obj[1]>2:
				return 'False'
			else: return 'False'
		else: return 'False'
	else: return 'False'
