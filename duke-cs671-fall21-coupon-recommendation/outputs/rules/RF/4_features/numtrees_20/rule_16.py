def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9931, "depth": 1}
	if obj[0]>0:
		# {"feature": "Occupation", "instances": 42, "metric_value": 0.9587, "depth": 2}
		if obj[2]<=14:
			# {"feature": "Distance", "instances": 37, "metric_value": 0.909, "depth": 3}
			if obj[3]>1:
				# {"feature": "Education", "instances": 21, "metric_value": 0.9852, "depth": 4}
				if obj[1]<=3:
					return 'True'
				elif obj[1]>3:
					return 'True'
				else: return 'True'
			elif obj[3]<=1:
				# {"feature": "Education", "instances": 16, "metric_value": 0.6962, "depth": 4}
				if obj[1]>0:
					return 'True'
				elif obj[1]<=0:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[2]>14:
			# {"feature": "Distance", "instances": 5, "metric_value": 0.7219, "depth": 3}
			if obj[3]<=1:
				return 'False'
			elif obj[3]>1:
				# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[1]>1:
					return 'False'
				elif obj[1]<=1:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'False'
	elif obj[0]<=0:
		# {"feature": "Occupation", "instances": 9, "metric_value": 0.7642, "depth": 2}
		if obj[2]<=6:
			return 'False'
		elif obj[2]>6:
			return 'True'
		else: return 'True'
	else: return 'False'
