def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Occupation", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[2]<=10:
		# {"feature": "Coupon", "instances": 24, "metric_value": 0.9183, "depth": 2}
		if obj[0]>0:
			# {"feature": "Education", "instances": 18, "metric_value": 0.7642, "depth": 3}
			if obj[1]<=0:
				return 'True'
			elif obj[1]>0:
				return 'True'
			else: return 'True'
		elif obj[0]<=0:
			# {"feature": "Education", "instances": 6, "metric_value": 0.9183, "depth": 3}
			if obj[1]<=2:
				return 'False'
			elif obj[1]>2:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[2]>10:
		# {"feature": "Coupon", "instances": 10, "metric_value": 0.7219, "depth": 2}
		if obj[0]>2:
			# {"feature": "Education", "instances": 6, "metric_value": 0.9183, "depth": 3}
			if obj[1]<=1:
				return 'False'
			elif obj[1]>1:
				return 'False'
			else: return 'False'
		elif obj[0]<=2:
			return 'False'
		else: return 'False'
	else: return 'False'
