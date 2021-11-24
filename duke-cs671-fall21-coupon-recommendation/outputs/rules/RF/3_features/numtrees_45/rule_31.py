def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[2]<=18:
		# {"feature": "Education", "instances": 19, "metric_value": 0.9495, "depth": 2}
		if obj[1]>1:
			# {"feature": "Coupon", "instances": 11, "metric_value": 0.684, "depth": 3}
			if obj[0]<=3:
				return 'True'
			elif obj[0]>3:
				return 'True'
			else: return 'True'
		elif obj[1]<=1:
			# {"feature": "Coupon", "instances": 8, "metric_value": 0.9544, "depth": 3}
			if obj[0]<=2:
				return 'False'
			elif obj[0]>2:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[2]>18:
		return 'False'
	else: return 'False'
