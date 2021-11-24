def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.7554, "depth": 1}
	if obj[2]>4:
		# {"feature": "Education", "instances": 16, "metric_value": 0.3373, "depth": 2}
		if obj[1]<=3:
			return 'True'
		elif obj[1]>3:
			# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[0]>2:
				# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[3]<=1:
					return 'False'
				else: return 'False'
			elif obj[0]<=2:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[2]<=4:
		# {"feature": "Coupon", "instances": 7, "metric_value": 0.9852, "depth": 2}
		if obj[0]>1:
			# {"feature": "Distance", "instances": 5, "metric_value": 0.971, "depth": 3}
			if obj[3]>1:
				# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[1]<=2:
					return 'True'
				elif obj[1]>2:
					return 'True'
				else: return 'True'
			elif obj[3]<=1:
				return 'False'
			else: return 'False'
		elif obj[0]<=1:
			return 'False'
		else: return 'False'
	else: return 'False'
