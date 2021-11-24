def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Occupation", "instances": 34, "metric_value": 0.9082, "depth": 1}
	if obj[2]<=8:
		# {"feature": "Distance", "instances": 23, "metric_value": 0.6666, "depth": 2}
		if obj[3]<=1:
			return 'True'
		elif obj[3]>1:
			# {"feature": "Education", "instances": 11, "metric_value": 0.9457, "depth": 3}
			if obj[1]>0:
				# {"feature": "Coupon", "instances": 8, "metric_value": 1.0, "depth": 4}
				if obj[0]>0:
					return 'False'
				elif obj[0]<=0:
					return 'True'
				else: return 'True'
			elif obj[1]<=0:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[2]>8:
		# {"feature": "Coupon", "instances": 11, "metric_value": 0.9457, "depth": 2}
		if obj[0]<=3:
			# {"feature": "Education", "instances": 6, "metric_value": 0.9183, "depth": 3}
			if obj[1]>0:
				# {"feature": "Distance", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[3]<=1:
					return 'True'
				elif obj[3]>1:
					return 'True'
				else: return 'True'
			elif obj[1]<=0:
				return 'False'
			else: return 'False'
		elif obj[0]>3:
			return 'False'
		else: return 'False'
	else: return 'False'
