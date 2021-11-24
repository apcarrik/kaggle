def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Coupon", "instances": 85, "metric_value": 0.9465, "depth": 1}
	if obj[0]<=3:
		# {"feature": "Occupation", "instances": 59, "metric_value": 0.9066, "depth": 2}
		if obj[2]<=6:
			# {"feature": "Education", "instances": 34, "metric_value": 0.8338, "depth": 3}
			if obj[1]<=2:
				return 'True'
			elif obj[1]>2:
				return 'True'
			else: return 'True'
		elif obj[2]>6:
			# {"feature": "Education", "instances": 25, "metric_value": 0.971, "depth": 3}
			if obj[1]<=2:
				return 'True'
			elif obj[1]>2:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[0]>3:
		# {"feature": "Occupation", "instances": 26, "metric_value": 0.9957, "depth": 2}
		if obj[2]>1:
			# {"feature": "Education", "instances": 21, "metric_value": 0.9984, "depth": 3}
			if obj[1]>0:
				return 'True'
			elif obj[1]<=0:
				return 'False'
			else: return 'False'
		elif obj[2]<=1:
			# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 3}
			if obj[1]<=0:
				return 'True'
			elif obj[1]>0:
				return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'True'
