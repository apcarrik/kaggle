def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[0]>1:
		# {"feature": "Occupation", "instances": 20, "metric_value": 0.8113, "depth": 2}
		if obj[2]>2:
			# {"feature": "Education", "instances": 17, "metric_value": 0.5226, "depth": 3}
			if obj[1]>1:
				return 'True'
			elif obj[1]<=1:
				return 'True'
			else: return 'True'
		elif obj[2]<=2:
			return 'False'
		else: return 'False'
	elif obj[0]<=1:
		# {"feature": "Education", "instances": 14, "metric_value": 0.8631, "depth": 2}
		if obj[1]<=4:
			# {"feature": "Occupation", "instances": 13, "metric_value": 0.7793, "depth": 3}
			if obj[2]>0:
				return 'False'
			elif obj[2]<=0:
				return 'True'
			else: return 'True'
		elif obj[1]>4:
			return 'True'
		else: return 'True'
	else: return 'False'
