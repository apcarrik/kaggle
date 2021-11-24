def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[0]>2:
		# {"feature": "Occupation", "instances": 24, "metric_value": 0.9183, "depth": 2}
		if obj[2]>4:
			# {"feature": "Education", "instances": 17, "metric_value": 0.7871, "depth": 3}
			if obj[1]>1:
				return 'True'
			elif obj[1]<=1:
				return 'True'
			else: return 'True'
		elif obj[2]<=4:
			# {"feature": "Education", "instances": 7, "metric_value": 0.9852, "depth": 3}
			if obj[1]<=3:
				return 'False'
			elif obj[1]>3:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[0]<=2:
		# {"feature": "Occupation", "instances": 10, "metric_value": 0.8813, "depth": 2}
		if obj[2]>1:
			# {"feature": "Education", "instances": 9, "metric_value": 0.7642, "depth": 3}
			if obj[1]>0:
				return 'False'
			elif obj[1]<=0:
				return 'False'
			else: return 'False'
		elif obj[2]<=1:
			return 'True'
		else: return 'True'
	else: return 'False'
