def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Occupation", "instances": 34, "metric_value": 0.9082, "depth": 1}
	if obj[2]>1:
		# {"feature": "Education", "instances": 28, "metric_value": 0.9666, "depth": 2}
		if obj[1]<=3:
			# {"feature": "Coupon", "instances": 26, "metric_value": 0.9829, "depth": 3}
			if obj[0]>1:
				# {"feature": "Distance", "instances": 17, "metric_value": 0.9367, "depth": 4}
				if obj[3]>1:
					return 'True'
				elif obj[3]<=1:
					return 'True'
				else: return 'True'
			elif obj[0]<=1:
				# {"feature": "Distance", "instances": 9, "metric_value": 0.9911, "depth": 4}
				if obj[3]<=2:
					return 'False'
				elif obj[3]>2:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[1]>3:
			return 'True'
		else: return 'True'
	elif obj[2]<=1:
		return 'True'
	else: return 'True'
