def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Education", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[1]>0:
		# {"feature": "Coupon", "instances": 24, "metric_value": 0.9799, "depth": 2}
		if obj[0]>1:
			# {"feature": "Occupation", "instances": 22, "metric_value": 0.994, "depth": 3}
			if obj[2]>4:
				return 'True'
			elif obj[2]<=4:
				return 'False'
			else: return 'False'
		elif obj[0]<=1:
			return 'False'
		else: return 'False'
	elif obj[1]<=0:
		# {"feature": "Occupation", "instances": 10, "metric_value": 0.469, "depth": 2}
		if obj[2]<=10:
			return 'True'
		elif obj[2]>10:
			# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[0]>2:
				return 'False'
			elif obj[0]<=2:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'True'
