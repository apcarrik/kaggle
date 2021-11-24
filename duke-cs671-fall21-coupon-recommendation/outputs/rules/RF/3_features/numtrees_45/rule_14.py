def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[2]>5:
		# {"feature": "Coupon", "instances": 14, "metric_value": 0.8631, "depth": 2}
		if obj[0]>0:
			# {"feature": "Education", "instances": 13, "metric_value": 0.7793, "depth": 3}
			if obj[1]<=2:
				return 'True'
			elif obj[1]>2:
				return 'True'
			else: return 'True'
		elif obj[0]<=0:
			return 'False'
		else: return 'False'
	elif obj[2]<=5:
		# {"feature": "Education", "instances": 9, "metric_value": 0.9183, "depth": 2}
		if obj[1]>0:
			# {"feature": "Coupon", "instances": 5, "metric_value": 0.971, "depth": 3}
			if obj[0]>1:
				return 'False'
			elif obj[0]<=1:
				return 'True'
			else: return 'True'
		elif obj[1]<=0:
			return 'False'
		else: return 'False'
	else: return 'False'
