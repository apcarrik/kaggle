def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[0]<=3:
		# {"feature": "Occupation", "instances": 18, "metric_value": 0.9183, "depth": 2}
		if obj[2]<=6:
			# {"feature": "Education", "instances": 9, "metric_value": 0.9911, "depth": 3}
			if obj[1]>1:
				return 'True'
			elif obj[1]<=1:
				return 'False'
			else: return 'False'
		elif obj[2]>6:
			# {"feature": "Education", "instances": 9, "metric_value": 0.5033, "depth": 3}
			if obj[1]>0:
				return 'True'
			elif obj[1]<=0:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[0]>3:
		# {"feature": "Occupation", "instances": 16, "metric_value": 0.9544, "depth": 2}
		if obj[2]>2:
			# {"feature": "Education", "instances": 11, "metric_value": 0.8454, "depth": 3}
			if obj[1]>0:
				return 'False'
			elif obj[1]<=0:
				return 'True'
			else: return 'True'
		elif obj[2]<=2:
			# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 3}
			if obj[1]>0:
				return 'True'
			elif obj[1]<=0:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
