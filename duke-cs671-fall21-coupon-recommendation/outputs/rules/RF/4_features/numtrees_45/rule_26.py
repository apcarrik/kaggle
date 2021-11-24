def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[0]>1:
		# {"feature": "Education", "instances": 19, "metric_value": 0.8997, "depth": 2}
		if obj[1]<=3:
			# {"feature": "Occupation", "instances": 17, "metric_value": 0.9367, "depth": 3}
			if obj[2]>4:
				# {"feature": "Distance", "instances": 14, "metric_value": 0.8631, "depth": 4}
				if obj[3]<=1:
					return 'True'
				elif obj[3]>1:
					return 'True'
				else: return 'True'
			elif obj[2]<=4:
				# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[3]>2:
					return 'True'
				elif obj[3]<=2:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[1]>3:
			return 'True'
		else: return 'True'
	elif obj[0]<=1:
		# {"feature": "Occupation", "instances": 4, "metric_value": 0.8113, "depth": 2}
		if obj[2]>4:
			return 'False'
		elif obj[2]<=4:
			return 'True'
		else: return 'True'
	else: return 'False'
