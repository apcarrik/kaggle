def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Occupation", "instances": 34, "metric_value": 0.9597, "depth": 1}
	if obj[2]<=10:
		# {"feature": "Coupon", "instances": 21, "metric_value": 0.7919, "depth": 2}
		if obj[0]<=2:
			# {"feature": "Education", "instances": 15, "metric_value": 0.9183, "depth": 3}
			if obj[1]>1:
				return 'True'
			elif obj[1]<=1:
				return 'False'
			else: return 'False'
		elif obj[0]>2:
			return 'True'
		else: return 'True'
	elif obj[2]>10:
		# {"feature": "Education", "instances": 13, "metric_value": 0.9612, "depth": 2}
		if obj[1]>0:
			# {"feature": "Coupon", "instances": 8, "metric_value": 1.0, "depth": 3}
			if obj[0]>1:
				return 'False'
			elif obj[0]<=1:
				return 'True'
			else: return 'True'
		elif obj[1]<=0:
			# {"feature": "Coupon", "instances": 5, "metric_value": 0.7219, "depth": 3}
			if obj[0]>1:
				return 'False'
			elif obj[0]<=1:
				return 'False'
			else: return 'False'
		else: return 'False'
	else: return 'False'
