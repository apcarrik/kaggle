def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Education", "instances": 204, "metric_value": 0.9597, "depth": 1}
	if obj[1]>1:
		# {"feature": "Occupation", "instances": 106, "metric_value": 0.9959, "depth": 2}
		if obj[2]<=20:
			# {"feature": "Coupon", "instances": 104, "metric_value": 0.9933, "depth": 3}
			if obj[0]<=2:
				return 'False'
			elif obj[0]>2:
				return 'True'
			else: return 'True'
		elif obj[2]>20:
			return 'False'
		else: return 'False'
	elif obj[1]<=1:
		# {"feature": "Occupation", "instances": 98, "metric_value": 0.8762, "depth": 2}
		if obj[2]>0:
			# {"feature": "Coupon", "instances": 93, "metric_value": 0.8953, "depth": 3}
			if obj[0]>1:
				return 'True'
			elif obj[0]<=1:
				return 'True'
			else: return 'True'
		elif obj[2]<=0:
			return 'True'
		else: return 'True'
	else: return 'True'
