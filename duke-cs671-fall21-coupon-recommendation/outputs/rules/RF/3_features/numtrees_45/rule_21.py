def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[2]<=8:
		# {"feature": "Coupon", "instances": 17, "metric_value": 0.874, "depth": 2}
		if obj[0]>0:
			# {"feature": "Education", "instances": 13, "metric_value": 0.6194, "depth": 3}
			if obj[1]>0:
				return 'True'
			elif obj[1]<=0:
				return 'True'
			else: return 'True'
		elif obj[0]<=0:
			# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 3}
			if obj[1]<=0:
				return 'False'
			elif obj[1]>0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[2]>8:
		# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 2}
		if obj[1]<=1:
			return 'False'
		elif obj[1]>1:
			# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[0]<=4:
				return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'False'
