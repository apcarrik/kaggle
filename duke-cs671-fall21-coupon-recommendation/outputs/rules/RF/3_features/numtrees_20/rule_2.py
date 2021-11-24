def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9864, "depth": 1}
	if obj[0]>0:
		# {"feature": "Occupation", "instances": 43, "metric_value": 0.9103, "depth": 2}
		if obj[2]<=20:
			# {"feature": "Education", "instances": 42, "metric_value": 0.8926, "depth": 3}
			if obj[1]<=3:
				return 'True'
			elif obj[1]>3:
				return 'True'
			else: return 'True'
		elif obj[2]>20:
			return 'False'
		else: return 'False'
	elif obj[0]<=0:
		return 'False'
	else: return 'False'
