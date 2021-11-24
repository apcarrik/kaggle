def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Occupation", "instances": 34, "metric_value": 0.9597, "depth": 1}
	if obj[2]>4:
		# {"feature": "Education", "instances": 26, "metric_value": 0.7793, "depth": 2}
		if obj[1]<=3:
			# {"feature": "Coupon", "instances": 23, "metric_value": 0.6666, "depth": 3}
			if obj[0]>1:
				# {"feature": "Distance", "instances": 18, "metric_value": 0.7642, "depth": 4}
				if obj[3]<=2:
					return 'True'
				elif obj[3]>2:
					return 'True'
				else: return 'True'
			elif obj[0]<=1:
				return 'True'
			else: return 'True'
		elif obj[1]>3:
			# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[0]>0:
				# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[3]<=2:
					return 'True'
				else: return 'True'
			elif obj[0]<=0:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[2]<=4:
		# {"feature": "Distance", "instances": 8, "metric_value": 0.5436, "depth": 2}
		if obj[3]>1:
			return 'False'
		elif obj[3]<=1:
			# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[0]<=0:
				return 'False'
			elif obj[0]>0:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'False'
