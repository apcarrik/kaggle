def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[0]<=3:
		# {"feature": "Occupation", "instances": 23, "metric_value": 0.8865, "depth": 2}
		if obj[2]>0:
			# {"feature": "Education", "instances": 22, "metric_value": 0.8454, "depth": 3}
			if obj[1]>1:
				return 'True'
			elif obj[1]<=1:
				return 'True'
			else: return 'True'
		elif obj[2]<=0:
			return 'False'
		else: return 'False'
	elif obj[0]>3:
		# {"feature": "Occupation", "instances": 11, "metric_value": 0.8454, "depth": 2}
		if obj[2]>2:
			# {"feature": "Education", "instances": 8, "metric_value": 0.9544, "depth": 3}
			if obj[1]>0:
				return 'False'
			elif obj[1]<=0:
				return 'False'
			else: return 'False'
		elif obj[2]<=2:
			return 'False'
		else: return 'False'
	else: return 'False'
