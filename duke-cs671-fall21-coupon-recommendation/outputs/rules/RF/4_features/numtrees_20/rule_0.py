def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9526, "depth": 1}
	if obj[0]<=3:
		# {"feature": "Occupation", "instances": 28, "metric_value": 0.5917, "depth": 2}
		if obj[2]<=7:
			# {"feature": "Education", "instances": 22, "metric_value": 0.684, "depth": 3}
			if obj[1]<=1:
				# {"feature": "Distance", "instances": 12, "metric_value": 0.8113, "depth": 4}
				if obj[3]<=1:
					return 'True'
				elif obj[3]>1:
					return 'True'
				else: return 'True'
			elif obj[1]>1:
				# {"feature": "Distance", "instances": 10, "metric_value": 0.469, "depth": 4}
				if obj[3]>1:
					return 'True'
				elif obj[3]<=1:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[2]>7:
			return 'True'
		else: return 'True'
	elif obj[0]>3:
		# {"feature": "Occupation", "instances": 23, "metric_value": 0.9321, "depth": 2}
		if obj[2]>1:
			# {"feature": "Education", "instances": 20, "metric_value": 0.8113, "depth": 3}
			if obj[1]<=2:
				# {"feature": "Distance", "instances": 16, "metric_value": 0.6962, "depth": 4}
				if obj[3]>1:
					return 'False'
				elif obj[3]<=1:
					return 'False'
				else: return 'False'
			elif obj[1]>2:
				# {"feature": "Distance", "instances": 4, "metric_value": 1.0, "depth": 4}
				if obj[3]>1:
					return 'True'
				elif obj[3]<=1:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[2]<=1:
			return 'True'
		else: return 'True'
	else: return 'False'
