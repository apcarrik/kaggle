def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Occupation", "instances": 34, "metric_value": 0.7335, "depth": 1}
	if obj[2]>1:
		# {"feature": "Education", "instances": 28, "metric_value": 0.8113, "depth": 2}
		if obj[1]<=3:
			# {"feature": "Coupon", "instances": 25, "metric_value": 0.7219, "depth": 3}
			if obj[0]>0:
				return 'True'
			elif obj[0]<=0:
				return 'True'
			else: return 'True'
		elif obj[1]>3:
			# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[0]>0:
				return 'False'
			elif obj[0]<=0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[2]<=1:
		return 'True'
	else: return 'True'
