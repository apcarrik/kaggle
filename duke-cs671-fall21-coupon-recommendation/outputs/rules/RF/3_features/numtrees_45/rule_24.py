def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Education", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[1]>1:
		# {"feature": "Occupation", "instances": 12, "metric_value": 0.9799, "depth": 2}
		if obj[2]>1:
			# {"feature": "Coupon", "instances": 10, "metric_value": 0.8813, "depth": 3}
			if obj[0]>2:
				return 'False'
			elif obj[0]<=2:
				return 'False'
			else: return 'False'
		elif obj[2]<=1:
			return 'True'
		else: return 'True'
	elif obj[1]<=1:
		# {"feature": "Coupon", "instances": 11, "metric_value": 0.684, "depth": 2}
		if obj[0]>0:
			return 'True'
		elif obj[0]<=0:
			# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[2]<=6:
				return 'False'
			elif obj[2]>6:
				return 'False'
			else: return 'False'
		else: return 'False'
	else: return 'True'
