def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Occupation", "instances": 51, "metric_value": 0.9367, "depth": 1}
	if obj[2]>2:
		# {"feature": "Coupon", "instances": 41, "metric_value": 0.9789, "depth": 2}
		if obj[0]>1:
			# {"feature": "Education", "instances": 31, "metric_value": 0.9383, "depth": 3}
			if obj[1]>1:
				return 'True'
			elif obj[1]<=1:
				return 'True'
			else: return 'True'
		elif obj[0]<=1:
			# {"feature": "Education", "instances": 10, "metric_value": 0.971, "depth": 3}
			if obj[1]<=0:
				return 'True'
			elif obj[1]>0:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[2]<=2:
		# {"feature": "Coupon", "instances": 10, "metric_value": 0.469, "depth": 2}
		if obj[0]>3:
			# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 3}
			if obj[1]>1:
				return 'True'
			elif obj[1]<=1:
				return 'True'
			else: return 'True'
		elif obj[0]<=3:
			return 'True'
		else: return 'True'
	else: return 'True'
