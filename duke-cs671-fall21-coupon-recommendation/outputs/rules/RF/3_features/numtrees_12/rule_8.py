def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Education", "instances": 85, "metric_value": 0.9465, "depth": 1}
	if obj[1]>0:
		# {"feature": "Coupon", "instances": 53, "metric_value": 0.9936, "depth": 2}
		if obj[0]>1:
			# {"feature": "Occupation", "instances": 39, "metric_value": 0.9418, "depth": 3}
			if obj[2]<=7:
				return 'True'
			elif obj[2]>7:
				return 'False'
			else: return 'False'
		elif obj[0]<=1:
			# {"feature": "Occupation", "instances": 14, "metric_value": 0.8631, "depth": 3}
			if obj[2]<=8:
				return 'False'
			elif obj[2]>8:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[1]<=0:
		# {"feature": "Occupation", "instances": 32, "metric_value": 0.7579, "depth": 2}
		if obj[2]>3:
			# {"feature": "Coupon", "instances": 24, "metric_value": 0.5436, "depth": 3}
			if obj[0]>0:
				return 'True'
			elif obj[0]<=0:
				return 'True'
			else: return 'True'
		elif obj[2]<=3:
			# {"feature": "Coupon", "instances": 8, "metric_value": 1.0, "depth": 3}
			if obj[0]>0:
				return 'True'
			elif obj[0]<=0:
				return 'False'
			else: return 'False'
		else: return 'False'
	else: return 'True'
