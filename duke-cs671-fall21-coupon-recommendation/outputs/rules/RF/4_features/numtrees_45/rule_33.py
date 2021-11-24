def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Education", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[1]>1:
		# {"feature": "Coupon", "instances": 13, "metric_value": 0.7793, "depth": 2}
		if obj[0]>0:
			# {"feature": "Occupation", "instances": 9, "metric_value": 0.5033, "depth": 3}
			if obj[2]<=14:
				return 'False'
			elif obj[2]>14:
				# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[3]<=1:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[0]<=0:
			# {"feature": "Occupation", "instances": 4, "metric_value": 1.0, "depth": 3}
			if obj[2]<=4:
				# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[3]>1:
					return 'False'
				elif obj[3]<=1:
					return 'False'
				else: return 'False'
			elif obj[2]>4:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[1]<=1:
		# {"feature": "Coupon", "instances": 10, "metric_value": 0.469, "depth": 2}
		if obj[0]<=3:
			return 'True'
		elif obj[0]>3:
			# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[2]>1:
				return 'True'
			elif obj[2]<=1:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'True'
