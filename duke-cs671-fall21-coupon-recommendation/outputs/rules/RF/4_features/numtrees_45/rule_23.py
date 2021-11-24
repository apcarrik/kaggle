def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[0]>1:
		# {"feature": "Education", "instances": 16, "metric_value": 0.8113, "depth": 2}
		if obj[1]>0:
			# {"feature": "Occupation", "instances": 10, "metric_value": 0.469, "depth": 3}
			if obj[2]<=9:
				return 'True'
			elif obj[2]>9:
				# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[3]<=2:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[1]<=0:
			# {"feature": "Occupation", "instances": 6, "metric_value": 1.0, "depth": 3}
			if obj[2]>5:
				# {"feature": "Distance", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[3]<=1:
					return 'True'
				else: return 'True'
			elif obj[2]<=5:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[0]<=1:
		# {"feature": "Occupation", "instances": 7, "metric_value": 0.8631, "depth": 2}
		if obj[2]<=7:
			# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 3}
			if obj[1]>2:
				# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[3]<=1:
					return 'False'
				elif obj[3]>1:
					return 'False'
				else: return 'False'
			elif obj[1]<=2:
				return 'False'
			else: return 'False'
		elif obj[2]>7:
			return 'True'
		else: return 'True'
	else: return 'False'
