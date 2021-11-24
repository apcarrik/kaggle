def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[2]<=6:
		# {"feature": "Coupon", "instances": 13, "metric_value": 0.9612, "depth": 2}
		if obj[0]>1:
			# {"feature": "Education", "instances": 9, "metric_value": 0.9911, "depth": 3}
			if obj[1]<=0:
				return 'True'
			elif obj[1]>0:
				return 'True'
			else: return 'True'
		elif obj[0]<=1:
			return 'False'
		else: return 'False'
	elif obj[2]>6:
		# {"feature": "Education", "instances": 10, "metric_value": 0.7219, "depth": 2}
		if obj[1]>1:
			# {"feature": "Coupon", "instances": 6, "metric_value": 0.9183, "depth": 3}
			if obj[0]>1:
				return 'True'
			elif obj[0]<=1:
				return 'True'
			else: return 'True'
		elif obj[1]<=1:
			return 'True'
		else: return 'True'
	else: return 'True'
