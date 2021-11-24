def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Education", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[1]<=3:
		# {"feature": "Coupon", "instances": 22, "metric_value": 0.9024, "depth": 2}
		if obj[0]<=3:
			# {"feature": "Occupation", "instances": 14, "metric_value": 0.9852, "depth": 3}
			if obj[2]<=19:
				return 'True'
			elif obj[2]>19:
				return 'False'
			else: return 'False'
		elif obj[0]>3:
			# {"feature": "Occupation", "instances": 8, "metric_value": 0.5436, "depth": 3}
			if obj[2]<=6:
				return 'True'
			elif obj[2]>6:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[1]>3:
		return 'False'
	else: return 'False'
