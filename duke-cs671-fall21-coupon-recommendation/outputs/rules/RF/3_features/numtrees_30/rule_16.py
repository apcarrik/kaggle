def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[0]>1:
		# {"feature": "Occupation", "instances": 22, "metric_value": 0.9457, "depth": 2}
		if obj[2]>3:
			# {"feature": "Education", "instances": 20, "metric_value": 0.971, "depth": 3}
			if obj[1]<=3:
				return 'True'
			elif obj[1]>3:
				return 'True'
			else: return 'True'
		elif obj[2]<=3:
			return 'True'
		else: return 'True'
	elif obj[0]<=1:
		# {"feature": "Occupation", "instances": 12, "metric_value": 0.9183, "depth": 2}
		if obj[2]<=12:
			# {"feature": "Education", "instances": 9, "metric_value": 0.9911, "depth": 3}
			if obj[1]<=2:
				return 'False'
			elif obj[1]>2:
				return 'True'
			else: return 'True'
		elif obj[2]>12:
			return 'False'
		else: return 'False'
	else: return 'False'
