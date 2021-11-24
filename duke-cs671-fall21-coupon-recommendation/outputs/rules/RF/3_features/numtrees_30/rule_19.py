def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[0]>0:
		# {"feature": "Occupation", "instances": 29, "metric_value": 0.9991, "depth": 2}
		if obj[2]<=10:
			# {"feature": "Education", "instances": 17, "metric_value": 0.874, "depth": 3}
			if obj[1]>1:
				return 'True'
			elif obj[1]<=1:
				return 'True'
			else: return 'True'
		elif obj[2]>10:
			# {"feature": "Education", "instances": 12, "metric_value": 0.8113, "depth": 3}
			if obj[1]>0:
				return 'False'
			elif obj[1]<=0:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[0]<=0:
		return 'False'
	else: return 'False'
