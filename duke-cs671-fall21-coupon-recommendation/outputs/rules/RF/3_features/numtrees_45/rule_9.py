def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[0]>1:
		# {"feature": "Occupation", "instances": 17, "metric_value": 0.9774, "depth": 2}
		if obj[2]>1:
			# {"feature": "Education", "instances": 15, "metric_value": 0.9968, "depth": 3}
			if obj[1]<=4:
				return 'False'
			elif obj[1]>4:
				return 'True'
			else: return 'True'
		elif obj[2]<=1:
			return 'True'
		else: return 'True'
	elif obj[0]<=1:
		# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 2}
		if obj[1]<=2:
			return 'False'
		elif obj[1]>2:
			# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[2]>4:
				return 'False'
			elif obj[2]<=4:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'False'
