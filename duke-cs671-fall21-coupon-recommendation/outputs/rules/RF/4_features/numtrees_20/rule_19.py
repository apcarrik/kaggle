def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9997, "depth": 1}
	if obj[0]>1:
		# {"feature": "Occupation", "instances": 36, "metric_value": 0.9641, "depth": 2}
		if obj[2]<=11:
			# {"feature": "Education", "instances": 27, "metric_value": 0.8256, "depth": 3}
			if obj[1]>0:
				# {"feature": "Distance", "instances": 18, "metric_value": 0.65, "depth": 4}
				if obj[3]>1:
					return 'True'
				elif obj[3]<=1:
					return 'True'
				else: return 'True'
			elif obj[1]<=0:
				# {"feature": "Distance", "instances": 9, "metric_value": 0.9911, "depth": 4}
				if obj[3]<=1:
					return 'True'
				elif obj[3]>1:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[2]>11:
			# {"feature": "Education", "instances": 9, "metric_value": 0.7642, "depth": 3}
			if obj[1]<=2:
				# {"feature": "Distance", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[3]<=2:
					return 'False'
				elif obj[3]>2:
					return 'True'
				else: return 'True'
			elif obj[1]>2:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[0]<=1:
		# {"feature": "Occupation", "instances": 15, "metric_value": 0.8366, "depth": 2}
		if obj[2]<=9:
			# {"feature": "Distance", "instances": 11, "metric_value": 0.4395, "depth": 3}
			if obj[3]<=1:
				# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[1]>0:
					return 'False'
				elif obj[1]<=0:
					return 'False'
				else: return 'False'
			elif obj[3]>1:
				return 'False'
			else: return 'False'
		elif obj[2]>9:
			# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 3}
			if obj[1]>2:
				# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[3]<=1:
					return 'False'
				elif obj[3]>1:
					return 'True'
				else: return 'True'
			elif obj[1]<=2:
				return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'False'
