def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Education", "instances": 85, "metric_value": 0.9831, "depth": 1}
	if obj[1]<=3:
		# {"feature": "Occupation", "instances": 75, "metric_value": 0.9968, "depth": 2}
		if obj[2]>5:
			# {"feature": "Coupon", "instances": 51, "metric_value": 0.9975, "depth": 3}
			if obj[0]<=3:
				return 'True'
			elif obj[0]>3:
				return 'False'
			else: return 'False'
		elif obj[2]<=5:
			# {"feature": "Coupon", "instances": 24, "metric_value": 0.9183, "depth": 3}
			if obj[0]>0:
				return 'True'
			elif obj[0]<=0:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[1]>3:
		# {"feature": "Coupon", "instances": 10, "metric_value": 0.469, "depth": 2}
		if obj[0]>1:
			return 'True'
		elif obj[0]<=1:
			# {"feature": "Occupation", "instances": 4, "metric_value": 0.8113, "depth": 3}
			if obj[2]>1:
				return 'True'
			elif obj[2]<=1:
				return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'True'
