def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9931, "depth": 1}
	if obj[0]<=3:
		# {"feature": "Education", "instances": 26, "metric_value": 0.8404, "depth": 2}
		if obj[1]>1:
			# {"feature": "Occupation", "instances": 15, "metric_value": 0.9968, "depth": 3}
			if obj[2]>2:
				return 'False'
			elif obj[2]<=2:
				return 'True'
			else: return 'True'
		elif obj[1]<=1:
			return 'True'
		else: return 'True'
	elif obj[0]>3:
		# {"feature": "Occupation", "instances": 25, "metric_value": 0.9427, "depth": 2}
		if obj[2]<=6:
			# {"feature": "Education", "instances": 14, "metric_value": 0.9852, "depth": 3}
			if obj[1]>0:
				return 'False'
			elif obj[1]<=0:
				return 'True'
			else: return 'True'
		elif obj[2]>6:
			# {"feature": "Education", "instances": 11, "metric_value": 0.4395, "depth": 3}
			if obj[1]>1:
				return 'False'
			elif obj[1]<=1:
				return 'False'
			else: return 'False'
		else: return 'False'
	else: return 'False'
